import pytest
from phonebook import Phonebook

'''
You can use the tmpdir fixture which will provide a temporary directory unique to the test invocation, created in the base temporary directory.
'''
@pytest.fixture #Setup
def phonebook(tmpdir):
    "Provides an empty Phonebook"
    phonebook = Phonebook(tmpdir)
    return phonebook

def test_add_and_lookup_entry(phonebook):
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")

    
def test_phonebook_gives_access_to_names_and_numbers(phonebook):
    phonebook.add("Alice", "12345")
    phonebook.add("Bob", "123")
    assert set(phonebook.names()) == {"Alice", "Bob"}
    assert "12345" in phonebook.numbers()
    
#Checks to see if given error/exception is raised.
def test_missing_entry_raises_KeyError(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("missing")

#This test is skipped
def test_add_and_lookup_entry_skip():
    pytest.skip("WIP")
    phonebook.add("Bob", "123")
    assert "123" == phonebook.lookup("Bob")