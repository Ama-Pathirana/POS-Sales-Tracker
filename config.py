import os

username = 'root'
password = 1234
host = 'localhost'
port = 3306
database_name = 'pos_sales_tracker'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+mysqlconnector://<username>:<password>@<host>:<port>/<database_name>'
SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key' # For authentication