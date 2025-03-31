#web: gunicorn django_blog.wsgi


import os
from dotenv import load_dotenv  
import dj_database_url
load_dotenv()
# import environ 
# env = environ.Env()
db_user = os.environ.get('USER_EMAIL')
db_password = os.environ.get('USER_PASS')


print(db_user)
print(db_password)

db_url = os.getenv('DATABASE_URL')
print(db_url)
print('   \n')
default = os.getenv('DATABASE_URL')
print(default)


database_url = dj_database_url.config(default=os.getenv('DATABASE_URL'))
print(database_url)

# "dest": "django_blog/wsgi.py"

    #  "build": {
    #        "env": {
    #          "PG_CONFIG": "/usr/local/bin/pg_config"
    #        }
    #     } 