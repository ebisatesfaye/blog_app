import os

db_user = os.environ.get('USER_EMAIL')
db_password = os.environ.get('USER_PASS')

print(db_user)
print(db_password)