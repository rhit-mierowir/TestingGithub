# Ideas:
# 1. Manually test Every Interface Implementation
# 2. Manually build a list containing all Fitness functions, and check which interfaces they implement and run associated Tests
#       This is highly vulnerable to new developers not bothering or knowing to add it to the list.
# 3. Implement all fitness functions as instances of an abstract "Fitness Function" Class,
#       import the entire codebase (to declare all subclasses) and use __subclasses__ to find all fitness functions.
#       This could be enfoced by ensuring .verify() also checked it was a subclass of the base "Fitness Function" Class so 
#       new developers would be informed of this and ensure all Fitness Functions are tested.
#       The .verify() could have an "In progress" return type so tests can be performed using xfail or something so the results
#       are run, but not flagged as problems.
# For 2 & 3: It may be hard to inividually specify tests that you want to run. Need further investigation.

class A_Base:
    def print(self):
        print("A_Base")

class B_A(A_Base):
    def print(self):
        print("B_A")

class C_A(A_Base):
    def print(self):
        print("C_A")

class D_B_A(B_A):
    def print(self):
        print("D_B_A")

# ----------- Testing -----------
print("------------- Testing Submodule ---------------")
A_Base().print()
B_A().print()
C_A().print()

# --------- Try Using Submodules ----------
print(A_Base.__subclasses__())
print(C_A.__subclasses__())
A_Base.__subclasses__()[0]().print() #Testing we actually have the classes
print(type(A_Base))
print(isinstance(A_Base,type))


def find_subclasses(parent):
    subclasses:list = parent.__subclasses__()
    for c in subclasses.copy():
        subclasses.extend(find_subclasses(c))
    return subclasses

print(find_subclasses(A_Base))
print("------------- End Testing Submodule ---------------")

# -------------------- Try to read Everything available ----------------------------
# ---------------------- Try Importing Everything -----------------------------------

from inspect import getmembers, ismodule, getmodule
import types
import src
#import src.af.a
from src.af import *
from src.af.bf import *
# https://julienharbulot.com/python-dynamical-import.html
# Dynamically import all classes in python submodule
 

def get_all_classes():
    objects_to_search = globals().values()
    classes_found:list[type] = [x for x in objects_to_search if isinstance(x,type)] # Python Classes are of type "type"
    modules_found:list = [x for x in objects_to_search if ismodule(x)]
    builtin_module = getmodule(ValueError)
    while len(modules_found) > 0:
        module_searching = modules_found.pop()
        members = map(lambda x: x[1] ,getmembers(module_searching)) # extracts the values from getmembers
        classes_found.extend([x for x in members if isinstance(x,type) and not (builtin_module == getmodule(x))])
        modules_found.extend([x for x in members if ismodule(x) and not (builtin_module == getmodule(x))])
    return classes_found

# Allows us to see what classes we have imported
print(get_all_classes())

# I am having trouble importing a.py and b.py
