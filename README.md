# FlaskDBSearch 🖥️

FlaskDBSearch is a simple Flask application that allows you to search through files in a directory (`data`) and its subdirectories. It provides a web interface to perform searches and view results paginated.

## Features

- Search functionality to find text within files in the `data` directory.
- Pagination of search results.
- Minimalistic Flask application setup.
- User authentication functionality (removed from this version).
- Supports almost all file extensions.

## Requirements

- Python 3.x
- Flask
- Flask-Bcrypt
- Flask-Login
- Flask-WTF

## Installation
1. ### Install requirements:
   ```bash
   pip install Flask Flask-Bcrypt Flask-Login Flask-WTF

2. ### Clone the repository:
   ```bash
   git clone https://github.com/netnsher/FlaskDBSearch.git
   cd FlaskDBSearch/Engine
2. ### Execute the script 
   ```bash
   python3 app.py
