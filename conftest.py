import importlib
import os
import pandas as pd

import pytest

from fixture.application import Application


fixture = None
target = None



@pytest.fixture(scope='session')
def app(request):
    fixture = Application("C:\\Users\\rymar\\PycharmProjects\\rymarava_b30_python\\AddressBookFree\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[3:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("xl_"):
            testdata = load_from_xl(fixture[3:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_xl(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\\%s.xls" % file), encoding='latin-1') as f:
        return f.read()
