"""
This is an outdated file to specify the fitness functions we want.

Author:
- Isaac Mierow
"""

import abc
from typing import Callable

class FitnessFunction:
    """
    This is a function that Is used as an abstract class
    to link relevant fitness functions.

    This class is not ment to be used directly.
    """
    
    @classmethod
    @abc.abstractmethod
    def verify(cls,version:str)->bool:
        pass
    
    
    @classmethod
    @abc.abstractmethod
    def evaluate(cls,*args,**kwargs):
        pass


class FooFitnessFunction(FitnessFunction):
    @classmethod
    def verify(cls,version:str)->bool:
        return True
    
    @classmethod
    def evaluate(cls, number: int) -> int:
        return number%12

print("------------ First Method -----------------")
print(FooFitnessFunction.verify("verion info"))
print(FooFitnessFunction.evaluate(20))

## --------------------- Using Instantiated Classes --------------------------
class FitnessFunction:
    
    @abc.abstractmethod
    def verify(self,version:str)->bool:
        pass
    
    @abc.abstractmethod
    def evaluate(self,*args,**kwargs):
        pass

class OtherClass:
    def test():
        return True

class FitnessFunctionListToInt(FitnessFunction):
    
    @abc.abstractmethod
    def verify(self,version:str)->bool:
        pass
    
    @abc.abstractmethod
    def evaluate(self,input:list[int])->float:
        pass

class FooFitnessFunction(FitnessFunctionListToInt,OtherClass):
    def verify(cls)->bool:
        return True
        isinstance(my_Selection_method, Selection_Method)

    def evaluate(cls, number: int) -> int:
        return number%12

print("------------ Second Method -----------------")
fit_func = FooFitnessFunction()
print(fit_func.verify())
print(fit_func.evaluate(20))

## --------------------- Using Functions -----------------------------

def fitness_function(value:int)->int:
    return value % 5

fitness_function.verify = lambda x: True

print("-------------- Third Method ---------------")
print(fitness_function(6))
print(fitness_function.verify(3))

## --------------------- Using Decorators --------------------------

# The decorator instantiated
def verified_by(verify_function:Callable):
    "This is a decorator to attatch a verified function to it."
    def verifier(func:Callable):
        verified = func
        verified.verify = verify_function
        # We could also potentially put this funtion into a list for testing.
        return verified
    return verifier

def verification_thing(value:str)->bool:
    return True

@verified_by(verification_thing)
def fitness_func(value:int)->int:
    return value % 4

#fitness_func.verify = verification_thing

print("-------------- Fourth Method ---------------")
print(fitness_func(6))
print(fitness_func.verify("version"))


if False:
    FooFitnessFunction.verify("verion info")
    FooFitnessFunction.evaluate(20)

    fit_func = FooFitnessFunction()
    fit_func.verify("verion info")
    fit_func.evaluate(20)

    fitness_function(6)
    fitness_function.verify(3)

    fitness_func(6)
    fitness_func.verify("version")

class file_test_verify_class():
    def print(self):
        print("file from test_verify.py")