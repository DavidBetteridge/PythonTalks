# Example
# https://www.programiz.com/python-programming/online-compiler/
# https://replit.com/languages/online-python-compiler


#######################################################################
#                     Combining strings
#######################################################################

print("Hello World")


name = input("What is your name?")

print("Hello " + name)

print("Hello", name)

print("Hello %s" % (name))

print(f"Hello {name}")



#######################################################################
#                         Types
#######################################################################

name = "David"

print(type(name))

name = 12

print(type(name))


#######################################################################
#                         If statements 
#######################################################################

if name == "David":   # <- note the :
    print("Hi David")   # <- note the indentation
elif name == "Kevin":
    print("Yo Kevin")
else:
    print("Hello")


#######################################################################
#                         While Loops
#######################################################################

n = 100
while n < 110:
  print(n)
  n += 1



#######################################################################
#                         For Loops
#######################################################################

for n in range(10):   # <- note the :
  print(n)  # <- note the indentation
  print("Next number")
print("Done")  


for n in range(15, 20):
  print(n)


for n in range(20, 15, -2):
  print(n)


#######################################################################
#                            Lists
#######################################################################

colours = ["Red", "Green", "Blue"]
colours.append("Yellow")
print(colours[1])
len(colours)
type(colours)

for colour in colours:
  print(colour)


#######################################################################
#                             Slices
#######################################################################

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# What does mean?
# for letter in letters[::-1][0:5]:

for letter in letters[2:5]:
  print(letter)


# string.join(letters, "-")
"-".join(letters)


#######################################################################
#                       List comprehensions
#######################################################################

# What about linq?
# select aka map,  from,  where

[letter for letter in letters]
[letter.upper() for letter in letters]
[letter.upper() for letter in letters if letter < 'm']
[letter.upper() for letter in letters[::-1] if letter < 'm']


# But we calculate letter.upper() twice
[letter.upper() for letter in letters[::-1] if letter.upper() < 'M']

# := is called the walrus operator
[l for letter in letters[::-1] if (l := letter.upper()) < 'M']



#######################################################################
#                       Dictionaries
#######################################################################

a_dict = { "David": "York",
           "Kevin": "London" }

len(a_dict)

a_dict["David"]
if "David" in a_dict:
  print("David is in the dictionary")


if "Frank" not in a_dict:
  print("Frank is NOT in the dictionary")


for name in a_dict:
  print(name, a_dict[name])

for name, city in a_dict.items():
  print(name, city)

for nc in a_dict.items():
  print(type(nc))

# It's a tuple!

# This returns a list,  but I want a dictionary
a_list = [letter.upper() for letter in letters if letter < 'm']
a_dict = {letter: letter.upper() for letter in letters if letter < 'm'}



#######################################################################
#                       Exercise
#######################################################################


# Number of A,B and Cs in this string
text = "AAAAABBBCCCCAAAABBBCCCCAAABBBCCCC"

# First attempt
counts = dict()
for s in text:
  if s in counts:
    counts[s] += 1
  else:
    counts[s] = 1

print(counts)


# Second attempt
from typing import DefaultDict  #Reference other modules/packages
counts = DefaultDict(int)
for s in text:
  counts[s] += 1

print(counts)

# Third attempt
from collections import Counter
counts = Counter(text)
counts
counts["A"]



#######################################################################

# Functions


def add(a, b):        # naming convention
  return a + b                    # <- note the indentation


add(1, 2)
add("David","Kevin")
add("David",1)


type(add(1, 2))
type(add("David","Kevin"))


#######################################################################
#                             Classes
#######################################################################


class Car:
  pass                    # <- note the indentation.   Must have a body - hence pass


class Car:
  def __init__(self, owner, colour, length_in_meters):
    self.owner = owner
    self.colour = colour
    self.length_in_meters = length_in_meters
  
  def start_engine(self):
    print("Starting engine")
  
  def stop_engine(self):
    print("Stopping engine")

  def __len__(self):
    return self.length_in_meters
  
  def __str__(self):
    return f"{self.owner}'s {self.colour} car"

  def __repr__(self) -> str:
    return self.owner



davids_car = Car("David", "Red", 2)
rebeccas_car = Car("Rebecca", "Blue", 3)
print(davids_car.owner)
len(davids_car)

# lambda syntax (can add args)
# python is dynamic
rebeccas_car.start_engine = lambda: print("Engine broken")
rebeccas_car.start_engine()
# makes mocking easy!


#######################################################################
#                             kwargs
#######################################################################

# *args **kwargs

def a_method(*args, **kwargs):
  for arg in args:
    print(arg)

  for name in kwargs:
    print(name, kwargs[name])

a_method(1,2,3,name="David", City="York")



def another_method(name, age):
  print(f"{name} is {age}")

a_tuple = ("David", 46)
 
another_method(a_tuple[0], a_tuple[1])
 
another_method(*a_tuple)



#######################################################################
#                             Typing hints
#######################################################################

def capital_letters(text):
  return text[0].upper() + text[1:].lower()

print(capital_letters("david"))
print(capital_letters(123))


def capital_letters2(text: str) -> str:
  return text[0].upper() + text[1:].lower()

print(capital_letters2("david"))
print(capital_letters2(123))

# Errors - switch on in settings
# HINTS!



def none_is_blank(text):
  if text is None:
    return ""
  else:
    return text


name = None
print(none_is_blank(name))


# What do we add for the typing hints?  str gives an error

def none_is_blank(text: Optional[str]) -> str:
  if text is None:
    return ""
  else:
    return text

# Optional is really Union[None, str]



def assign_address_to_person(person_id: int, address_id: int):
  print("Person", person_id)
  print("Address", address_id)


david = 1234
york = 5678

assign_address_to_person(york, david)


from typing import NewType

AddressId = NewType("AddressId", int)
PersonId = NewType("PersonId", int)


def assign_address_to_person(person_id: PersonId, address_id: AddressId):
  print("Person", person_id)
  print("Address", address_id)

david = PersonId(1234)
york = AddressId(5678)

assign_address_to_person(york, david)

assign_address_to_person(david, york)

print(type(david))
print(type(york))


#######################################################################
#                             Interfaces
#######################################################################
from typing import Protocol

class DatabaseAccess(Protocol):
  def get_person(self, person_id: int) -> str:
    ...


def do_something(db: DatabaseAccess, person_id: int):
  name = db.get_person(person_id)
  print(name)


class MemoryAccess():
  def get_person(self, person_id: int) -> str:
    return "David"

do_something(MemoryAccess(), 1234)    

# rename get_person to get an error message



#######################################################################
#                             Generics
#######################################################################

from typing import TypeVar

T = TypeVar('T')
def coalesce(first: T, second: T) -> T:
  return first if first is not None else second

# Bit limited,  as restrictions cannot be applied,  ie can't do where T is int


#######################################################################
#                             Decorators
#######################################################################

#1
def six():
  return 6

def double(x: int) -> int:
  return x * 2

print(double(six()))


# 2
from typing import Callable

def double(fn: Callable) -> int:
  return fn() * 2

print(double(six))


# 3
def fn_builder():
  def double(x: int) -> int:
    return x * 2
  return double

print(fn_builder()(6))


#4

def six():
  return 6

def double(func):
  def wrapper():
    return func() * 2
  return wrapper

double_six = double(six)

print(double_six())

#5

@double
def seven():
  return 7

print(seven())




#######################################################################
#                             Exceptions
#######################################################################


try:
  print(1/0)
except ZeroDivisionError:
  print("Cannot divide by zero")
  

def must_be_positive(func):
  def wrapper(a,b):
    result = func(a,b)
    if result < 0:
      raise Exception(f"Result of calculation must be positive. {a}-{b} is {result}")
    return result
  return wrapper


@must_be_positive
def sub(a,b):
  return a - b

print(sub(10, 5))
print(sub(10, 50))




#######################################################################
#                   data classes
#######################################################################
class Car:
  def __init__(self, owner, colour, length_in_meters):
    self.owner = owner
    self.colour = colour
    self.length_in_meters = length_in_meters

car0 = Car("David", "Red", 2)
print(car0.owner)
print(car0)



import dataclasses

@dataclasses.dataclass
class Car:
  owner: str
  colour: str
  length_in_meters: int

car1 = Car("David", "Red", 2)
print(car1.owner)
print(car1)

car1.colour = "Blue"



# Immutable
@dataclasses.dataclass(frozen=True)
class Car:
  owner: str
  colour: str
  length_in_meters: int

car1 = Car("David", "Red", 2)
car1.colour = "Blue"


@dataclasses.dataclass()
class Car:
  owner: str = dataclasses.field(init=False)  # Note the types!
  colour: str = dataclasses.field(repr=False)  # Note the types!
  length_in_meters: int

car1 = Car("Red", 2)

print(type(car1.colour))


#######################################################################
#                   Scoping
#######################################################################


class BusinessLogic:

  def __init__(self):
    self.__cache = {}
    self.cache_size = 0

  def __add_to_cache(self, x, result):
      self.__cache[x] = result
      self.cache_size += 1

  def double(self, x):
    if x in self.__cache:
      return self.__cache[x]
    else:
      result = x * 2
      self.__add_to_cache(x, result)
      return result

logic = BusinessLogic()
print(logic.double(5))
print(logic.cache_size)
print(logic.double(5))
print(logic.cache_size)
print(logic.double(6))
print(logic.cache_size)


logic.__add_to_cache(7, 10)   # Don't work
print(logic.double(7))
print(logic.cache_size)

logic.__cache[7] = 10        # Don't work
print(logic.double(7))
print(logic.cache_size)


print(dir(logic))
logic._BusinessLogic__cache[7] = 10
print(logic.double(7))
print(logic.cache_size)

# So __ means private,  what about protected?

#######################################################################
#                      #if Directives
#######################################################################

name = "David"

if name == "David":
  def town():
    print("London")
else:
  def town():
    print("Paris")

town()

#######################################################################
#                      New Objects
#######################################################################
import random


class MissingHouse():
  def __str__(self):
    return f"There is no house"


class House():
  def __init__(self, address):
    self.address = address

  def __str__(self):
    return f"House at {self.address}"



class BaseHouse():
  def __new__(cls, address):
    if random.random() < 0.5:
      print("Creating instance of house")
      return House(address)
    else:
      print("Creating instance of MissingHouse")
      return MissingHouse()




h = BaseHouse("123 Main Street")
print(h)





# modules
# performce c code
# packages pip
# web flask
# generators
# with statements