import pytest

from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application("C:\\Users\\rymar\\PycharmProjects\\rymarava_b30_python\\AddressBookFree\\AddressBook.exe")
    request.addfinalizer(fixture.destroy)
    return fixture
