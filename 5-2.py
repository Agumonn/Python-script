'''

Exercise 5-2: Inheritance

Create a Worker class which inherits a Person class. 
Worker has two own properties: 
* contractType: FullTime or PartTime
* salary: amount of monthly salary
+ all properties from the Person base class (see Exercise I)


Add Worker class objects into the list and print them out:

persons = list()
persons.append(Worker("Bill","FullTime", 4500))
persons.append(Worker("John","PartTime", 2900))
persons.append(Worker("Calle","FullTime", 3900))
persons.append(Worker("Mary","Hourly", 2600))
persons.append(Worker("Jill","FullTime", 4100))
persons.append(Worker("Ann","Hourly", 3300))

Output:

[('Bill', 'FullTime', 4500), ('John', 'PartTime', 2900), ('Calle', 'FullTime', 3900), ('Mary', 'Hourly', 2600), ('Jill', 'FullTime', 4100), ('Ann', 'Hourly', 3300)]
'''
class Worker:
   def __init__(self,name,contract,salary):
      self.name=name
      self.contract=contract
      self.salary=salary
   def __repr__(self):
      return repr((self.name, self.contract, self.salary))
      

 
persons = list()
persons.append(Worker("Bill","FullTime", 4500))
persons.append(Worker("John","PartTime", 2900))
persons.append(Worker("Calle","FullTime", 3900))
persons.append(Worker("Mary","Hourly", 2600))
persons.append(Worker("Jill","FullTime", 4100))
persons.append(Worker("Ann","Hourly", 3300))

print(persons)
