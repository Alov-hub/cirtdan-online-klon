"""
Django settings for django_salam project.
"""

import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Projenin ana dizinini belirler
BASE_DIR = Path(__file__).resolve().parent.parent

# Geliştirme aşaması için güvenlik anahtarı
SECRET_KEY = 'django-insecure-w_&y5a(2l8)1v!n_r+2@6j6z4$t$9b#77p$v(h*w$*4z'

# Sunucuda test ederken hata detaylarını görmek için True
DEBUG = True

# VPS'inin IP adresinden dışarıdan erişilebilmesi için her hosta izin veriyoruz
ALLOWED_HOSTS = ['*']


# ==========================================
# UYGULAMALAR (APPS)
# ==========================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Kendi yarattığımız ana uygulama
]

# ==========================================
# ARA YAZILIMLAR (MIDDLEWARE)
# ==========================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # DİL DEĞİŞTİRME İÇİN ŞART (Session'dan hemen sonra olmalı)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_salam.urls'

# ==========================================
# ŞABLONLAR (TEMPLATES - HTML)
# ==========================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # HTML dosyalarımızın aranacağı klasör
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n', # Dil context'i
            ],
        },
    },
]

WSGI_APPLICATION = 'django_salam.wsgi.application'

# ==========================================
# VERİTABANI (DATABASE)
# ==========================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Şifre Doğrulayıcılar
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# ==========================================
# ÇOKLU DİL (INTERNATIONALIZATION - i18n)
# ==========================================
LANGUAGE_CODE = 'az' # Ana dil Azerbaycanca

TIME_ZONE = 'Asia/Baku' # Bakü zaman dilimi

USE_I18N = True # Çeviri sistemi aktif

USE_TZ = True # Zaman dilimi aktif

# Sitede desteklenecek diller (Orijinal sitedeki gibi ayarlanabilir)
LANGUAGES = [
    ('az', _('Azerbaijani')),
    ('en', _('English')),
    ('ru', _('Russian')),
]

# gettext ile oluşturulacak çeviri sözlüklerinin (django.po) bulunacağı klasör
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# ==========================================
# STATİK DOSYALAR (CSS, JS, RESİMLER)
# ==========================================
STATIC_URL = 'static/'

# Wget ile indirdiğin dosyaların bulunacağı klasörü sisteme tanıtıyoruz
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Gelecekte collectstatic komutu ile toplanacak ana dizin
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Oyunları iframe ile eklersek engellenmemesi için aynı domaine izin
X_FRAME_OPTIONS = 'SAMEORIGIN'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'