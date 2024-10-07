# News Display Web App

A Django-based web application to display the latest news, including title, description, image, and external links.

## Features

- Display the latest news with title, description, image, and a "Read More" external link.
- Responsive design for news items.
- Easily extendable with new features such as news categories, filters, or pagination.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Django 3.x or later
- A virtual environment setup (optional but recommended)

### Installation

1. **Clone the repository**:

   ```
   git clone https://github.com/yourusername/news-display-app.git
   ```
2. **Navigate into the project directory**:
```
cd news-display-app
```

3. **Create a virtual environment (optional but recommended)**:

```
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
4. **Install the required dependencies**:
```
pip install -r requirements.txt
```
5. **Run database migrations:**
```
python manage.py migrate
```
6. **Create a superuser (admin)**:
```
python manage.py createsuperuser
```
7. **Run the development server**:
```
python manage.py runserver
```
Access the app by navigating to:
http://127.0.0.1:8000/
