Overview
=======
This library is pluggable django app which allows all logging to be outputted as JSON and addition of extra context through method definition.
==========

Pip:

    pip install <TBD>

Pypi:

  <TBD>

Manual:

    python setup.py install

Usage
=====

### Remove `Logging` setting from your Django project.


### Add `django-logger` to your Django app in `INSTALLED_APPS`

```python
    INSTALLED_APPS = [
    ...
    'django_logger',
]
```

### Add logger middleware to your `MIDDLEWARE` Django settings file

```python
    MIDDLEWARE = [
    # ...
    'django_logger.middleware.CidMiddleware',
]
```

### Add `CID_GENERATE` to your Django settings file

```python
    CID_GENERATE = True
```

### Method to add extra values to logging

In Django settings file add `LOG_EXTRA_METHOD` method definition as string value. The method should always return a dictionary.

```python
    LOG_EXTRA_METHOD = 'my_module.my_method'
)
```


### Sample logging output

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


### Running tests
In the project directory run the following command to execute tests
```python
python runtests.py
```

Currently the tests create a test.log file in the folder when running tests. It logs all the statements for 404 and 500 error codes and once completed. Looks for the logging statements presence in the file. Any errors are outputted to the console.
