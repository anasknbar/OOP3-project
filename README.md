# OOP3-project

# Contact Management System

This project is a simple contact management system that allows you to add, show, delete, and search for contacts. It follows the Strategy Design Pattern to implement different functionalities.

## Project Structure

- **strategy.py**: Contains the main logic for adding, showing, deleting, and searching contacts using different strategies.
- **main.py**: Provides a command-line interface to interact with the contact management system.

## Files and Classes

### strategy.py

#### Classes:

- **Contact**: Represents a contact with name, job, address, and phone number.
- **Strategy (ABC)**: Abstract base class for different contact management strategies.
  - **Add_contact**: Implements the strategy to add a contact to the contact book.
  - **Show_Contacts**: Implements the strategy to display all contacts in a tabular format.
  - **Delete_Contact**: Implements the strategy to delete a contact from the contact book by line number.
  - **Search_Contact**: Implements the strategy to search for a contact in the contact book by a keyword.

#### Context Class:

- **Context**: Manages the strategy and executes the appropriate method based on user choice.
  - **set_strategy(strategy: Strategy)**: Sets the strategy to be used.
  - **excute_add_contact_strategy(data: List)**: Executes the add contact strategy.
  - **excute_show_contacts_strategy()**: Executes the show contacts strategy.
  - **excute_delete_contact_strategy(line_to_delete: int)**: Executes the delete contact strategy.
  - **excute_search_contact_strategy(keyword: str)**: Executes the search contact strategy.

### main.py

Provides the command-line interface for the user to interact with the contact management system.

#### Functions:

- **main()**: The main loop of the program, providing options to add, show, delete, or search contacts.
- **add_contact()**: Collects user input and adds a new contact.
- **show_contacts()**: Displays all contacts.
- **delete_contact(line_to_delete: int)**: Deletes a contact based on the provided line number.
- **search_contact(keyword: str)**: Searches for a contact based on the provided keyword.

## How to Use

1. **Add a Contact**: 
   - Run the program and select option `1` to add a contact.
   - Enter the required details: Name, Job, Address, and Phone Number.

2. **Search for a Contact**: 
   - Select option `2` to search for a contact.
   - Enter a keyword to search for a specific contact.

3. **Delete a Contact**: 
   - Select option `3` to delete a contact.
   - Enter the Contact ID (line number) of the contact you want to delete.



4. **Exit**: 
   - Select option `4` to exit the program.



