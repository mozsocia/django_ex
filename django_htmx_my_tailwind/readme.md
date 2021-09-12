https://justdjango.com/blog/dynamic-forms-in-django-htmx

add

Crispy Forms
The go-to package for better forms is django-crispy-forms. We're going to use the TailwindCSS template pack for styling.

Install both packages:

```
pip install django-crispy-forms crispy-tailwind
```

Configure the package in settings.py:

```
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_tailwind",
    ...
)
```

```
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

```

Now in book_form.html load the tailwind filters at the top:

```
{% load tailwind_filters %}
```

And make the form crispy:

```
{{ form|crispy }}
```
