# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

        #QUESTIONS
        #How does this solution ensure data immutability?
        #it cant ensure data immutability because the attributes of podracer, anakinspod, and sebulbaspod cna be changed directly

        #Is this solution a pure function? Why or why not?
        # i dont think its a pure function because the solution does not involve a function that operates solely on its input

        #Is this solution a higher order function? Why or why not?
        #i dont think it is because this solution does not involve high order functions

        #Would it have been easier to# solve this problem using a different programming style?
        #i think python is a good because its the simplest form to write

        #Why in particular is functional programming a helpful paradigm when solving this problem?
        #functional programming is a helpful paradigm in this solution because it has variables that are passed as arguments and return other functions


# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  # Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"
    
# Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price)
  def boost(self):
    self.max_speed *= 2
    
# Define another class that inherits Podracer and call this one SebulbasPod. 
# This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
  
    def flame_jet(self, podracer):
        podracer.condition = "trashed"


        #QUESTIONS

        #How does this solution demonstrate the four pillars of OOP?
        #Encapsulation--Podracer, AnakinsPod, and SebulbasPod has its own attributes and methods, keeping the implementation details hidden from external entities
       
        #Abstraction--classes only need to know the essential details, such as calling methods like repair(), boost(), or flame_jet() to perform specific actions on the objects so abstraction is not potrayed
        
        #Inheritance--AnakinsPod and SebulbasPod both inherit from the Podracer like the max_speed, condition, and price attributes from Podracer and can access and modify them as needed
        
        #Polyphorphism-- AnakinsPod and SebulbasPod can be treated as Podracer objects because they inherit from the base class
        
        #Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
        #I dont think so because using the OOP approach can provide a clear and structured solution

        #How in particular did Object Oriented Programming assist in the solving of this problem?
        #By allowing the creation of distinct classes like Podracer, AnakinsPod, SebulbasPod with their own attributes, behaviors, and code organization
        

