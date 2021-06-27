
```
urlpatterns = [
    path('home/', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('new/', new, name='new23'),
    path('newpar/<int:id>', newpar, name='newparid')
]

```
```
In [1]: from django.urls import reverse

In [2]: reverse('index')
Out[2]: '/home/'

In [3]: reverse('new23')
Out[3]: '/new/'

In [4]: reverse('newparid', kwargs={'id': 3452})
Out[4]: '/newpar/3452'
```

```
In [10]: from django.http import Http404, HttpResponseRedirect

In [11]: HttpResponseRedirect( reverse('index'))
Out[11]: <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/home/">

In [12]: HttpResponseRedirect(reverse('newparid', kwargs={'id': 3452}))
Out[12]: <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/newpar/3452">

In [13]: HttpResponseRedirect('/some/url/')
Out[13]: <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/some/url/">
```


```

In [6]: redirect('index')
Out[6]: <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/home/">

In [7]: redirect('newparid', id = 345)
Out[7]: <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/newpar/345">

In [8]: redirect('/some/url/')
Out[8]: <HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/some/url/">

In [9]: redirect('https://example.com/', permanent=True)
Out[9]: <HttpResponsePermanentRedirect status_code=301, "text/html; charset=utf-8", url="https://example.com/">

```

