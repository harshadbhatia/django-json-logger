Overview
=======
This library is pluggable django app which allows all logging to be outputted as JSON which and allows easily addition of custom fields
==========
Pip:

    pip install <TBD>

Pypi:

  <TBD>

Manual:

    python setup.py install

Usage
=====

### Add `django-logger` to your django app in `INSTALLED_APPS`

```python
    INSTALLED_APPS = (
    ...
    'django_logger',
)
```

### Add logger middleware to your `MIDDLEWARE` django settings file

```python
    MIDDLEWARE = [
    # ...
    'django_logger.middleware.CidMiddleware',
]
)
```

### Add `CID_GENERATE` to your django settings file

```python
    CID_GENERATE = True
)
```

### To add extra values to logging 

In django settings file add `LOG_EXTRA_METHOD` method definition as string value. The method should always return a dictionary.

```python
    LOG_EXTRA_METHOD = 'my_module.my_method'
)
```


### Runserver using `python manage.py runserver`

The app should automatically now log data as JSON output. Current structure is:
```json
{
"timestamp": "2017-11-22T05:56:49.916432Z",
"level": "WARNING",
"name": "django.request",
"message": "Not Found: /test/",
"status_code": 404,
"USER": "harshad",
"DJANGO_SETTINGS_MODULE": "my_app.settings.prod",
"REQUEST_METHOD": "GET",
"PATH_INFO": "/test/",
"HTTP_HOST": "127.0.0.1:8000",
"REMOTE_ADDR": "127.0.0.1",
"QUERY_STRING": "",
"HTTP_USER_AGENT": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
"REQUEST_BODY": "b''"
}


```
