## THis is all files From my first django practicise


## static and media settings 
https://docs.djangoproject.com/en/3.2/howto/static-files/

```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]

```


https://stackoverflow.com/questions/5517950/django-media-url-and-media-root

```
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```



```
STATIC_DIR = BASE_DIR / 'static'
MEDIA_DIR = BASE_DIR / 'media'

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
```
