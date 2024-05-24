## How Strategy pattern built:
from abc import ABC,abstractclassmethod

# 1- Strategy Interface
class Strategy(ABC):

  @abstractclassmethod
  def do_math(self,num1:int ,num2:int) -> int: # sometime instead of num1 and num2 you need to implement a class, this class thould located outside of the Strategy method.
    pass
  
  
# 2- Concrete Classes

class Addtion(Strategy):
  def do_math(self,num1,num2):
    return num1 + num2
  
class Multiplication(Strategy):
  def do_math(self,num1,num2):
    return num1 * num2
  
class Substraction(Strategy):
  def do_math(self,num1,num2):
    return num1 - num2
  
class Division(Strategy):
  def do_math(self,num1,num2):
    return num1 / num2 
  
# 3- context class

class Context:
  def __init__(self,strategy : Strategy ): # strategy determined based on the user choose.
    self._strategy = strategy
    
  def set_strategy(self, strategy : Strategy):
    self._strategy = strategy
    
  def excute_strategy(self,num1,num2):
    return self._strategy.do_math(num1,num2) # do math will be one of the initialized object from the do_math class.
    

# 4- usage

context = Context(Addtion()) # >> the choose of the strategy determined based on the user 
print(context.excute_strategy(90,10))
  
# if you want to change the context strategy you can use the set_strategy, this way you are using the same instance.

context.set_strategy(Multiplication())
print(context.excute_strategy(90,10))







##### this python file only used for referencing, it does not have any functionallty in the this project

