import requests
from bs4 import BeautifulSoup
from .models import News
import os

def download_image(image_url, save_directory, image_name):
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    image_path = os.path.join(save_directory, image_name)
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                else:
                    break
    return image_path
def scrape_imdb_news():
    url = 'https://www.imdb.com/news/movie/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    news_items = soup.find_all('div', class_='ipc-list-card--border-line')
    for item in news_items:
        title_element = item.find('a', class_='ipc-link ipc-link--base sc-ed7ef9a2-3 eDjiRr')
        description = item.find('div', class_='ipc-html-content-inner-div')
        image = item.find('img', class_='ipc-image')
        image_path = None
        
        if image:
            image_name = title_element.text.strip().replace(' ', '_') + '.jpg'
            image_path = download_image(image['src'], 'downloads', image_name)
        
        
        title = title_element.text.strip() if title_element else "No title"
        description = description.text.strip() if description else "No description"
        image_url = image['src'] if image else "No image"
        external_link = item.find('a', class_='ipc-link ipc-link--base sc-ed7ef9a2-3 eDjiRr')['href']
        
        news = {
            'title': title,
            'description': description,
            'image': image_url,
            'external_link': external_link
        }
        News.objects.create(**news)
        
    

scrape_imdb_news()
