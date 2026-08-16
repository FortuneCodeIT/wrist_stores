import os
import django

print("🚀 Starting create_superuser.py script...")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wrist_store.settings')
django.setup()

from django.contrib.auth.models import User

username = 'admin'
email = 'admin@example.com'
password = 'admin123'

print("📊 Checking if user exists...") 

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superuser '{username}' created successfully!")
else:
    print(f"Superuser '{username}' already exists.")