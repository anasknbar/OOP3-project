import os
import pytest
from unittest.mock import mock_open, patch

from strategy import Add_contact,Delete_Contact  

@pytest.fixture
def add_contact():
    return Add_contact()

def test_contact_book_append(add_contact):
    data = ["John Doe", "Engineer", "1234 Elm St", "555-5555"]
    
    mock_file = mock_open()
    
    with patch('strategy.open', mock_file), \
         patch('strategy.os.path.getsize', return_value=100):
        add_contact.contact_book(data)
    
    mock_file.assert_called_once_with('project/contacts.csv', 'a')
    mock_file().write.assert_any_call('John Doe,Engineer,1234 Elm St,555-5555\n')

def test_contact_book_write_header(add_contact):
    data = ["Jane Smith", "Doctor", "5678 Oak St", "555-1234"]
    
    mock_file = mock_open()
    
    with patch('strategy.open', mock_file), \
         patch('strategy.os.path.getsize', return_value=0):
        add_contact.contact_book(data)
    
    mock_file.assert_called_once_with('project/contacts.csv', 'a')
    mock_file().write.assert_any_call('Name,Job,Address,Phone Number\n')
    mock_file().write.assert_any_call('Jane Smith,Doctor,5678 Oak St,555-1234\n')


@pytest.fixture
def delete_contact():
    return Delete_Contact()

def test_contact_book_delete(delete_contact):
    line_to_delete = 2  
    mock_file_content = [
        'Name,Job,Address,Phone Number\n',
        'John Doe,Engineer,1234 Elm St,555-5555\n',
        'Jane Smith,Doctor,5678 Oak St,555-1234\n',
        'Alice Brown,Teacher,9101 Maple Ave,555-6789\n'
    ]
    
    mock_file = mock_open(read_data=''.join(mock_file_content))
    
    with patch('strategy.open', mock_file):
        delete_contact.contact_book(line_to_delete)
    
  
    mock_file.assert_called_with('project/contacts.csv', 'w')
    

    expected_content = [
        'Name,Job,Address,Phone Number\n',
        'John Doe,Engineer,1234 Elm St,555-5555\n',
        'Alice Brown,Teacher,9101 Maple Ave,555-6789\n'
    ]
    mock_file().writelines.assert_called_once_with(expected_content)