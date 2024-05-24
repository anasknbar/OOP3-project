from abc import ABC,abstractclassmethod
from typing import Dict,List
import os
from tabulate import tabulate

class Contact:
  def __init__(self,name,job,address,phone_number):
    self.name = name
    self.job = job
    self.address = address
    self.phone_number = phone_number
    
    
 

class Strategy:
  
  @abstractclassmethod
  def contact_book(self,data:List):
    pass
  
  
class Add_contact(Strategy):
  def contact_book(self,data:List):
    csv_file = 'project/contacts.csv'
    with open(csv_file,'a') as file:
      if os.path.getsize(csv_file) > 0:
        name,job,address,phone_number = data
        file.write(f'{name},{job},{address},{phone_number}\n')
      else:
        name,job,address,phone_number = data
        file.write('Name,Job,Address,Phone Number\n')
        file.write(f'{name},{job},{address},{phone_number}\n')
       
class Show_Contacts(Strategy):
  def contact_book(self):
    csv_file = 'project/contacts.csv'
    
    with open(csv_file,'r') as file:
      lines = file.readlines()
      table = []
      for index,line in enumerate(lines[1:],start=1):
        row = line.split(',')
        row = [index]+row 
        table.append(row)
      print(tabulate(table , headers=['ID','Name','Job','Address','Phone Number'], tablefmt="rounded_grid"))
 
class Delete_Contact(Strategy):
    def contact_book(self, line_to_delete):
        csv_file = 'project/contacts.csv'
        
        # Read the lines from the file and filter out the line to delete
        with open(csv_file, 'r') as file:
            lines = file.readlines()
        
        # Skip the header and delete the specified line
        new_content = [line for i, line in enumerate(lines,start=1) if i != line_to_delete+1]
        
        # Write the filtered content back to the file
        with open(csv_file, 'w') as file:
            file.writelines(new_content)
    
class Search_Contact(Strategy):
  def contact_book(self,keyword):
    csv_file = 'project/contacts.csv'
    with open(csv_file, 'r') as file:
      search_result = []
      lines = file.readlines()
      for line in lines:
        if keyword in line.strip().lower():
          search_result.append(line)
      
      table = []  
      for index,line in enumerate(search_result,start=1):
        row = line.split(',')
        row = [index]+row 
        table.append(row)
      GREEN = "\033[32m"
      RESET = "\033[0m"
      print(f'{GREEN}                            Search Result {RESET}')
      print(f"{GREEN}{tabulate(table, headers=['ID', 'Name', 'Job', 'Address', 'Phone Number'], tablefmt='rounded_grid')}{RESET}")
    


class Context:
  def __init__(self,strategy : Strategy ): # strategy determined based on the user choose.
    self._strategy = strategy
    
  def set_strategy(self, strategy : Strategy):
    self._strategy = strategy
    
  def excute_add_contact_strategy(self,data):
    return self._strategy.contact_book(data)
  
  def excute_show_contacts_strategy(self):
    return self._strategy.contact_book()

  def excute_delete_contact_strategy(self,line_to_delete):
    return self._strategy.contact_book(line_to_delete)
  
  def excute_search_contact_strategy(self,keyword):
    return self._strategy.contact_book(keyword)






  