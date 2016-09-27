# encoding: utf-8
"""
Django settings for blog_project project.

Generated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, '../weblog/apps'))
sys.path.append(os.path.join(BASE_DIR, '../weblog/config'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_lho^m33w-!qkhmqe2n2cwovcouiw(l++%&^(w5x@171pbm7_4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    #   'suit',          #pip install django-suit==0.2.21
    #'grappelli',    #pip install django-grappelli
    #'bootstrap_admin',  #一定要放在`django.contrib.admin`前面
    'django.contrib.admin',
    'registration',  # should be immediately above 'django.contrib.auth'
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'markdown_deux',
    'django_comments',
    'notifications',
    'haystack',
    'likes',
    'blog',
    'comments',
    'accounts',
    #'social_login',
]

SITE_ID = 1

COMMENTS_APP = 'comments'  # for custom django-contrib-comments framework

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'weblog.config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.sidebar',  # for sidebar information
                'social_login.context_processors.social_sites',  # for social login
            ],
        },
    },
]

WSGI_APPLICATION = 'weblog.config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'database/db.sqlite3'),
#     }
# }

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',                      
        'USER': 'postgres',
        'PASSWORD': '7494994',
        'HOST': '',
        'PORT': '',
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/


LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES = 'weblog/static/'
#STATICFILES = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    ]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT ='weblog/static/'

# Markdown settings
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
            "fenced-code-blocks": None,
            "codehilite": None,
        },
        "safe_mode": "escape",
    },
}

AUTH_USER_MODEL = 'accounts.BlogUser'

# pinax likes
PINAX_LIKES_LIKABLE_MODELS = {
    "blog.Article": {},
    "comments.CommentWithParent": {},  # can override default config settings for each model here
}

AUTHENTICATION_BACKENDS = [
    'likes.auth_backends.CanLikeBackend',
]

LOGIN_URL = '/login/'

#图片路径
#MEDIA_ROOT = 'mysite/media/'
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# social user settings
SOCIALOAUTH_SITES = (
    ('weibo', 'socialoauth.sites.weibo.Weibo', '新浪微博',
     {
         'redirect_uri': 'http://zmrenwu.pythonanywhere.com',
         'client_id': '3072222160',
         'client_secret': '9b06ed28d7598a91ee72bc38e4f067b2',
     }
     ),
)
SOCIAL_LOGIN_ERROR_REDIRECT_URL = 'errors/'

# haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 自动更新索引
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# registration
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True

# Email settings

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = '218.17.227.203'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'zhangyuan@szkingdom.com'  # add your own accounts for local test
# EMAIL_HOST_PASSWORD = '&$94994zy'
# EMAIL_USE_TLS = False

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'zhangyuan19870129@gmail.com'  # add your own accounts for local test
EMAIL_HOST_PASSWORD = 'zhangyuan596387'
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = ['zhangyuan@szkingdom.com']
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

#网站域名
SITES_HOST = "127.0.0.1:8000"