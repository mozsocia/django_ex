
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

