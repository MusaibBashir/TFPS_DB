import os
from pathlib import Path
import dj_database_url  # 📦 Make sure it's in your requirements.txt

# 📍 Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# 🎩 Secret key from environment
SECRET_KEY = os.environ.get('SECRET_KEY', 'super-insecure-dev-key')

# 🚨 Debug (off in production!)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# 🌐 Hosts allowed
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# 🧩 Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'equipment',
    'events',
]

# ⚙️ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🧭 URLs
ROOT_URLCONF = 'tfps_project.urls'

# 🎨 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚂 WSGI
WSGI_APPLICATION = 'tfps_project.wsgi.application'

# 🐘 Database (Render-style, env-based)
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# 🔐 Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 🌍 Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # or change to your preference
USE_I18N = True
USE_TZ = True

# 🗃️ Static files (e.g. CSS, JS)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 🧹 Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
