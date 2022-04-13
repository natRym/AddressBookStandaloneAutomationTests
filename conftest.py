import os
import xlrd

import pytest

from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application("C:\\Users\\rymar\\PycharmProjects\\rymarava_b30_python\\AddressBookFree\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    if "xl_groups" in metafunc.fixturenames:
        testdata = load_from_xl()
        metafunc.parametrize("xl_groups", testdata, ids=[str(x) for x in testdata])


def load_from_xl():
    groups = []
    rows_count = 5
    project_dir = os.path.dirname(os.path.realpath(__file__))
    xl_data_file = os.path.join(project_dir, "data/groups.xls")
    wb = xlrd.open_workbook(xl_data_file)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)
    for i in range(rows_count):
        groups.append(sheet.
                      cell_value(i, 0))
    return groups
