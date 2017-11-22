import sys
if sys.version_info < (2, 6):
    print(sys.stderr, "{}: need Python 2.6 or later.".format(sys.argv[0]))
    print(sys.stderr, "Your Python is {}".format(sys.version))
    sys.exit(1)

from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session='test')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name = "django-json-logger",
    version = "0.1",
    url = "https://github.com/harshadbhatia/django-json-logger/",
    license = "BSD",
    description = "A Django app for adding json log formatter",
    author = "Harshad Bhatia",
    author_email = "harshadbhatia2012@gmail.com",
    package_dir = {'': 'django_logger'},
    packages = find_packages("django_logger", exclude="tests"),
    test_suite = "tests.tests",
    install_requires = reqs,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Logging',
    ]
)
