import json
import os
import sys

from django.test import TestCase

basepath = os.path.dirname(__file__)
filepath = os.path.abspath(os.path.join(basepath, "..", "test.log"))


def assert_items_in_message(line, message=None, status_code=None):
    if 'correlationId' not in line:
        print('AssertionError: correlationId not found in error logs', file=sys.stderr)

    if not line['correlationId']:
        print('AssertionError: correlationId does not have a value found in error logs', file=sys.stderr)

    if 'EXTRA' not in line:
        print('AssertionError: EXTRA context not found in error logs', file=sys.stderr)

    if not line['EXTRA']:
        print('AssertionError: EXTRA context not found in error logs', file=sys.stderr)

    if not line['message']:
        print('AssertionError: Message not present in error logs', file=sys.stderr)

    if message and line['message'] != message:
        print('AssertionError: Message not present in error logs', file=sys.stderr)

    if status_code and line['status_code'] != status_code:
        print('AssertionError: Status code {} not present in error logs'.format(status_code), file=sys.stderr)


class AssertItemsInLoggingStatements(TestCase):
    def setUp(self):
        self.file = open(filepath, 'r')

    def iterate_n_lines(self, no_of_lines, index=1):
        for i in range(no_of_lines):
            if i == index:
                try:
                    line = self.file.readline()
                    return json.loads(line)
                except ValueError:
                    print('Failed to load json logs from file')
            else:
                self.file.readline()
        return ''

    def test_500_present_in_file(self):
        message = 'Exception with status code 500 happened.'
        assert_items_in_message(self.iterate_n_lines(2, 1), message=message)

    def test_404_present_in_file(self):
        assert_items_in_message(self.iterate_n_lines(6, 5), status_code=404)
