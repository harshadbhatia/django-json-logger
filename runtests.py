#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    """
    The test uses django test runner to create a django app with settings value defined 
    and does the following:
    1. Create a test.log file and makes 404 and 500 request to the server
    2. Read the file and look for the values if logged as desired.
    """
    basepath = os.path.dirname(__file__)
    filepath = os.path.abspath(os.path.join(basepath, "test.log"))
    log_file = open(filepath, 'w')
    original_out = sys.stdout
    original_error = sys.stderr

    sys.stderr = open(filepath, 'w')
    sys.stdout = open(filepath, 'w')

    os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
    django.setup()
    TestRunner = get_runner(settings)
    test_runner = TestRunner()
    failures = test_runner.run_tests(["tests.test_log_to_file"])
    log_file.close()
    failures = test_runner.run_tests(["tests.test_logging"])

    log_file = open(filepath, 'r')
    lines = log_file.readlines()

    sys.stderr = original_error
    sys.stdout = original_out

    for line in lines:
        if 'FAILED' in line:
            assert False, 'FAILED: Failed tests '
        if 'AssertionError' in line:
            assert False, 'AssertionError: Fields are not present in json log'

    print('All tests passed')
    os.remove(filepath)  # Remove the file after use
    sys.exit(True)
