import os
from dotenv import load_dotenv  
import dj_database_url
load_dotenv()

db_user = os.environ.get('USER_EMAIL')
db_password = os.environ.get('USER_PASS')


print(db_user)
print(db_password)
# "dest": "django_blog/wsgi.py"
db_url = os.getenv('DATABASE_URL')
print(db_url)
print('   \n')
database_url = dj_database_url.config(default=os.getenv('DATABASE_URL'))
print(database_url)

