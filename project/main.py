from strategy import Context,Strategy,Add_contact,Contact,Show_Contacts,Delete_Contact,Search_Contact
import sys
import subprocess



def main():
  while True:
    # subprocess.run('clear', shell=True)
    show_contacts()
    
    user_input = input('1. Add contact\n2. Search\n3. Delete contact\n4. Exit\n>>> ').lower().strip()
    if user_input == '1':
      subprocess.run('clear', shell=True)
      add_contact()
      # show_contacts()
    
    elif user_input == '2':
      
      
      # show_contacts()
      search_contact(input('Search for: ').lower().strip())
      
      
      
    
      
      
    elif user_input == '3':
      subprocess.run('clear', shell=True)
      show_contacts()
      
      delete_contact(int(input('Enter Contact ID: ').lower().strip()))
      # show_contacts()
      

    elif user_input == '4':
      sys.exit()
    else:
      RED = "\033[31m"
      RESET = "\033[0m"
      
      print(f'\n{RED}:( Wrong Input, try again!{RESET}\n')
    
      
      




def add_contact():
  name = input('Name: ')
  job = input('Job: ')
  Address = input('Address: ')
  phone_number = input('Phone Number: ')
  # contact = Contact()
  
  context = Context(Add_contact())
  context.excute_add_contact_strategy([name,job,Address,phone_number])
  
def show_contacts():
  context = Context(Show_Contacts())
  context.excute_show_contacts_strategy()
  
def delete_contact(line_to_delete):
  context = Context(Delete_Contact())
  context.excute_delete_contact_strategy(line_to_delete)
  
def search_contact(keyword):
  context = Context(Search_Contact())
  context.excute_search_contact_strategy(keyword)
if __name__ == '__main__':
  main()