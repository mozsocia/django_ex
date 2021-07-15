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


https://docs.djangoproject.com/en/3.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development
```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```


#### for sending image in form always use :- enctype = "multipart/form-data"    in form
