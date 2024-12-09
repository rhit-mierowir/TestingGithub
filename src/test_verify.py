# class FitnessFunction:
    
#     @abc.abstractmethod
#     def verify(self,version:str)->bool:
#         pass
    
#     @abc.abstractmethod
#     def evaluate(self,*args,**kwargs):
#         pass

# class FitnessFunctionListToInt(FitnessFunction):
    
#     @abc.abstractmethod
#     def verify(self,version:str)->bool:
#         pass
    
#     @abc.abstractmethod
#     def evaluate(self,input:list[int])->float:
#         pass

# class FooFitnessFunction(FitnessFunctionListToInt):
#     def verify(cls)->bool:
#         return True
#         isinstance(my_Selection_method, Selection_Method)

#     def evaluate(cls, number: int) -> int:
#         return number%12
    
from typing import Protocol, runtime_checkable
from random import Random

# ----------------- A Definition of Protocols In Another File ----------------------------
@runtime_checkable
class FitnessFunction(Protocol):
    """
    This is an Protocol (Abstract Class with fancy syntax) for defining a Fitness Function of any type.
    """
    def __init__(self,*args,**kwargs) -> None:
        ...
    def verify(self)->bool:
        """
        Verify that the functions that use this 

        Returns
        -------
        bool
            True if all of its arguments are of the correct type.
        """
        ...
    def evaluate(self,*args,**kwargs)-> any:
        ...

@runtime_checkable
class FitnessFunctionPercentageOut(FitnessFunction,Protocol): # The protocol is also required to note that this is abstract and can't be implemented
    """
    This is a Fitness Function that has an output that will always be a percentage between 0 and 1 inclusive.
    """
    def evaluate(self,*args, **kwargs) -> float:
        ...

@runtime_checkable
class FitnessFunctionRandom(FitnessFunction,Protocol):
    """
    This is a Fitness Function that includes any randomness in it.
    """
    Randomizer: Random
    def __init__(self,Randomizer:Random,*args,**kwargs) -> None:
        ...

@runtime_checkable
class FitnessFunctionIntegerListIn(FitnessFunction,Protocol):
    """
    This is a Fitness function that has an input which is only a list of integers.
    """
    def evaluate(self,Integer_List:list[int]) -> any:
        ...

# ----------------- In the Implementation File ----------------------------

class FitnessFunctionAvgAmpPercentOfMax(FitnessFunctionIntegerListIn,FitnessFunctionPercentageOut):
    """
    This finds the percentage of the average amplitude in a list as a percentage of the maximum amplitude.
    """
    def evaluate(self,Integer_List: list[int]) -> float:
        av = sum([abs(i) for i in Integer_List])/len(Integer_List)
        max_int = max([abs(i) for i in Integer_List])
        return av/max_int
    
    def verify(self) -> bool:
        # There are no internal dependancies. If remove this, need to remove None
        return True
    

# ------------------------------ Examples & Testing ---------------------------------------------

ff_obj = FitnessFunctionAvgAmpPercentOfMax()
print(ff_obj.evaluate([1,3,4]))
print(ff_obj.verify())

print(f"Is instance of Fitness Function: {isinstance(ff_obj,FitnessFunction)}")
print(f"Is instance of Percent Out: {isinstance(ff_obj,FitnessFunctionPercentageOut)}")
print(f"Is instance of Random FF: {isinstance(ff_obj,FitnessFunctionRandom)}")
print(f"Is instance of Integer List In: {isinstance(ff_obj,FitnessFunctionIntegerListIn)}")

class SelectionMethodExample:
    def __init__(self,fitness_function:FitnessFunction) -> None:
        self.fitness_function: FitnessFunction = fitness_function

    def verify(self) -> bool:
        return isinstance(self.fitness_function,FitnessFunctionPercentageOut) \
            and isinstance(self.fitness_function,FitnessFunctionIntegerListIn) \
            and True
            #and isinstance(self.fitness_function,FitnessFunctionRandom) \
            

print(f"Verified Selection Method: {SelectionMethodExample(FitnessFunctionAvgAmpPercentOfMax()).verify()}")