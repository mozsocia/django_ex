## THis is all files From my first django practicise


## static and media settings 

```
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```
