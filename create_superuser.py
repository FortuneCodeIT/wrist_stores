import os
import django

print("🚀 Creating admin user...")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wrist_store.settings')
django.setup()

from django.contrib.auth.models import User

# Admin credentials
username = 'admin'
email = 'admin@example.com'
password = 'admin123'

# Check if user exists
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"✅ Superuser '{username}' created successfully!")
    print(f"🔑 Password: {password}")
else:
    print(f"ℹ️ Superuser '{username}' already exists.")

print("🏁 Admin creation complete.")