from typing import Callable, Any, Iterator, Iterable, Generator, Protocol
from dataclasses import dataclass, field
import pytest
"""
This file includes examples of the following things:
	1. Writing Basic Tests and Type Annotations
	2. Types for Functions Returning functions (Callables)
	3. Using Parameterize to test simple variations, adding comments to asserts
	4. Typing Lists and Tupples
	5. Testing for Exceptions & Errors
	6. Typing Generators & Pytest Fixtures
	7. Protocols
	8. Dataclasses

	TODO: Try out useing the interface idea that I thought of over break to test common interfaces for simple actions
	TODO: @overload (typing.overload) https://docs.python.org/3/library/typing.html#typing.overload

Other Notes:
	For more information, see https://docs.python.org/3/library/typing.html
		1. This shows you how to create generic types

Guidelines for Testing:
	1. Values in tests should be hardcoded and not derrived at runtime. 
		To test if add() works properly, write "assert 12 == add(10,2)" and NOT "assert 10+2 == add(10,2)"
	2. Every function should be tested thuroughly.
		To make sure the code works, select values that verify most if not all parts of what a function does so we can detect if behaviors change
		- Test normal behavior: Test a couple random values for what your function should handle
		- Test edge cases: Try some extreme values to verify you handled edge cases correctly. These are typically at the edges of valid ranges, 
			or require special logic to differentiate from the general case.
		- Test errors: Make sure you get errors when you expect to get them. (eg. Try to insert an element outside of a list and verify you get an error)
	3. Build Tests before you write code.
		Clarify what you want the code to do before you write it by clearly writing down what you want the code to do in tests before writing it.
		- This helps you brainstorm what the function should do near edge cases.
		- This helps you write the function so it can be easily used because you design the function's interface in the test when you are trying to use it.
			This means it is likely that you make it easy to use rather than easy to create.
		- This stops you from creating supurfluous logic or trying to imagine how exactly you plan to call the function because you did that writing tests.
		- This makes it clear when your code works, and can verify when it breaks.
		- Are you really going to want to write tests after you write the code? Really?
	4. Use Dependancy injection.
		Pass in what you want to use into the function. This means that when you are testing, you can pass in fake versions of those things and test that
			your code is interacting with them properly without having to do crazy workarounds that will break if you so much as touch the code again.
			This is called mocking.
	5. Only test ONE THING a.k.a. it should be clear why a test fails.
		Each test should only verify one action is working properly, and should be named in a manner to make it clear what that was.
			"Given ____ When _____ Then _____" statements are a good way to clarify what a test is soposed to be covering.
		- If you are given a list of tests that failed, it should be reasonably easy to see what issue whould have arized to cause the problems,
			even before you look into the code or test logic.
		- If you find it challenging to write the "Given ___ When ____ Then ___" statement, you may be testing multiple things in one test, which should be separated.
	6. Tests don't prove your software works, only that you don't know how it could fail
		Make sure you have thurough tests to make it more likely it fails when it is broken, even for things that seem certain to work correctly.
		- If you encounter a bug that you fix, write a test that covers that bug by reproducing it in a failed test, fixing the code, and verifying the test passes.

Guidelines for Typing:
	1. Everything should have type annotations, especially if it is permanent in the code base
	2. Make types as general as possible, but as specific as required.
		If you need an integer use the "int" type, but if you only need a number "int|float" would be better.
		This should allow us to easily be able to tell what datatypes a program works properly for, and help communicate when reuse can happen.
	

"""


## 1. Basic Tests and Type Annotations
# "test_" tells pytest the funciton is a test
# assert statements 
def add_one(x: int)->int:
	return x+1

def test_add_one()->None:
	assert add_one(5) == 6
	assert add_one(10) == 11



## 2. Functions returning Callables
# Callable[[argT0,argT1,argT2,], outT] specifies it will output a function with arguments with the types in "[argT0,argT1,ArgT2]"" and has an output of type "outT"
# Callable[...,outT] means that any arguments are allowed and it has an output of type "outT"
def add_number_function(n: int)->Callable[[int],int]:
	def add_number(x:int)->int:
		return x+n
	return add_number

def generate_excited_greeting(greeting:str) -> Callable[[int],str]:
	def greet(n:int)->str:
		return (n*(greeting+"! "))
	return greet



## 3. Using Parameterize to test simple variations, adding comments to asserts
# Parametarize seeks the names in the first list, and assigns the values in the second list to those named variables.
# It is fine to create many variations on simple functions, but avoid complex tables or many argumetnts. 
# Above all, it should be simple to see what is happening in the test.
# All values being tested should be hard-coded and not derrived, so write "[7, 8, 15]" instead of "[7, 8, 7+8]" so tests are more certain.
#
# Adding comments to asserts was domonstrated below, and this text is rendered and shown whenever the assert fails.
# The error message shows you the numbers that lead to the assert failing, so the "!=" part of test_add_number_function is redundant.
# Whenever a test fails, it should be clear why, and this is one simple way to communicate that to someone investigating why the test failed.
@pytest.mark.parametrize(["internal","external","result"],[
						[0, 0, 0],
						[1, 2, 3],
						[3, 2, 5],
						[7, 8, 15]
						 ])
def test_add_number_function(internal:int, external:int, result:int)->None:
	addnumFunc = add_number_function(internal)
	assert addnumFunc(external) == result, f"FAILED TEST: {internal} + {external} = {addnumFunc(external)} != {result}"

@pytest.mark.parametrize(["greeting","repeat_count","result"],[
	["Hello",			3, "Hello! Hello! Hello! "],
	["Hi",				5, "Hi! Hi! Hi! Hi! Hi! "],
	["*Intense Anger*",	0, ""]
])
def test_exceited_greeting(greeting:str, repeat_count:int, result:str)->None:
	greet = generate_excited_greeting(greeting)
	assert greet(repeat_count) == result, "Repeated Greeting failed"


## 4. Typing Lists and Tupples
# Most lists and types assume that the entire list will be of one type, and will error out if any other type is specified or provided.
# 	list[int]  		a list containing only integers
#	list[int, str]	INVALID TYPE, only one type can be specified
# Tupples commonly have different types for each elements, so they can be typed specifying the exact size of the tupple and the type of each element
# 	tupple				any tupple (same as tupple[any,...])
# 	tupple[int,int]		a tupple containing two elements which are both integers
# 	tupple[int,str]		a tupple containing two elements where the 1st is an integer and the 2nd is a string
#	tupple[int,...]		a tupple containing any number of elements, which all must be integers
	
def test_lists_and_tupples_work_as_expected():
	# Note typing isn't checked at runtime, so no exception is raised for the "Bad Ones"

	# Good
	a: list[int] = [3,1,4,1,5,9,2,6]

	# Bad
	b: list[int, str] = [3,"magic number"]
	a: list[int] = ["This is not an int", "4", "crazy"]

	#Good
	c: tuple[int] = (5)
	c: tuple[int,int] = (7,5)
	d: tuple[str,int] = ("string",5)
	e: tuple[int,Any,str] = (4,True,"Happiness")
	f: tuple[int,...] = (5,2,4,1,4,5,2,3,7)

	#Bad
	c: tuple[int] = (7,5)
	f: tuple[int,...] = (5,2,"text me")


## 5. Testing for Exceptions & Errors
# When you want to test that an exception is thrown and fail if no exception is thrown.
# This will test that the Exception class is it or a subclass of the one you specify.
# You can specify it with further assert statements:
#	assert exec_info.type=ExactException
#	assert "Error description" in exec_info.value
# For more information: https://docs.pytest.org/en/latest/how-to/assert.html#assertions-about-expected-exceptions

def test_asserting_errors_raised()-> None:
	# Uncomment the following lines to 
	#raise ValueError("Test that errors make tests fail.")
	pass

	# Show a simple use of this way to test for Exceptions
	with pytest.raises(ArithmeticError):
		raise FloatingPointError("This is a subclass of ArighmeticError.")


	# A more complex example of catching Exceptions
	with pytest.raises(ValueError) as excinfo: 				#Assert the contents of this raises an Exception that is ValueError or its subclass
		raise ValueError("Verify this message")
	
	assert "Verify this message" in str(excinfo.value)		#Assert that the Exception's message contains the string.
	assert excinfo.type is ValueError 						#Assert that the type is exactly ValueError, not a subclass

## 6. Typing Generators & Pytest Fixtures
# Generators return multiple values, for example providing the values in a list when queried. 
# These intermediate values are produced with a yeild statement, which pauses the execution of this code which resumes when another value is requested.
# After this, it can optionally also return a value using the standard return syntax.
# There are ways to send information to it which I will not go in depth on.
# For information on sending: https://stackoverflow.com/questions/19302530/what-is-the-purpose-of-the-send-function-on-python-generators
#
# There are two ways to type generators, the first is more thurough but usually superfluous:
# Generator[YieldType, SendType, ReturnType]
#
# The second verson only communicates the yield type, but that is generally all you care about for most generators:
# Iterator[YieldType]
# Iterable[YieldType]
#
# One notable use of these are pytest Fixtures which provide startup code to generate some object for testing, yield it for use in tests, then 
#	when the test finishes, it returns to the fixture which will close or remove what was generated to make sure you reach the deactivation logic.
# This allows you to automatically generate useful objects for testing your code and reuse them in multiple tests.

@pytest.fixture
def example_fixture_generator() -> Iterator[Generator[int,None,str]]:
	def generator_to_create()->Generator[int,None,str]:
		for i in range(5):
			yield i
		return "done"
	
	yield generator_to_create

	## add teardown code here (automatically run after test.)
	# If this connected to database, this is where you close that connection

#pass in a the results of a fixture by putting the fixture name as an argument, and the result of the yield statement is put there
def test_example_fixture(example_fixture_generator:Generator[int,None,str])->None:

	#save the generator
	generator = example_fixture_generator()

	assert next(generator) == 0
	assert next(generator) == 1
	assert next(generator) == 2
	assert next(generator) == 3
	assert next(generator) == 4

	with pytest.raises(StopIteration) as execinfo:
		next(generator)
	assert str(execinfo.value) == "done"


## 7. Protocols 
# These are interfaces for structural typing. This is a type is fulfilled by anything that has the quantities specified in the protocol declaration.
# This only clarify what the function needs to run properly, and should be as general as possible withoug being meaningless
# This is useful because it allows you to generalize a function to only what is necessary for it to work, so it is easier to reuse and interpret.

# Create the Protocol
class Readable(Protocol):
	title:str
	author:str

	def read()->None:
		...

# Create class that implements protocol
class Book:
	def __init__(self,title,author) -> None:
		self.title = title
		self.author = author
	
	def read(self)->None:
		print(f"reading '{self.title}' by: {self.author}")

# Function that references protocol
def read_if_title_contains_word(text: Readable, word: str)->int:
	if (word.lower() in text.title.lower()):
		text.read()
		return 1
	return 0

def test_useing_protocols()->None:
	badbook = Book("Bad Book","Dr. Evil")
	goodbook = Book("Good Book", "Dr. Good")
	assert read_if_title_contains_word(badbook,"good") == 0
	assert read_if_title_contains_word(goodbook, "good") == 1

## 8. Data Classes
# These classes are a concise way of creating classes that primarily hold data.
# the = signs indicate default values, and assigns the same item to each created object.
# If you want to create different items for each initialized item (assign different empty list to each), you need to create a factory to generate them.
# More Info At: https://docs.python.org/3/library/dataclasses.html
# You might want to look into KW_ONLY if you want to have keyword only values: https://docs.python.org/3/library/dataclasses.html#dataclasses.KW_ONLY
# Look into Post-init to have some values generated from others, not provided on initialization: https://docs.python.org/3/library/dataclasses.html#dataclasses.__post_init__
	
@dataclass
class Report:
	"""Class for storing information to identify a report."""
	id: int
	title: str
	authors: list[str] = field(default_factory=list) #This data class queries this factory to get a new version of the item needed

	def print_report_data(self)->str:
		return f"Report ID: {self.id} TITLE: '{self.title}' AUTHORS: {self.authors}"
	
def test_Report()->None:
	report1 = Report(0,"Report 1")
	report2 = Report(1,"Report 2")
	print(report1.print_report_data())
	
	report1.authors.append("R1A1")
	report1.authors.append("R1A2")
	report2.authors.append("R2A1")
	report2.authors.append("R2A2")

	assert report1.title == "Report 1"
	assert report1.id == 0
	assert "R1A1" in report1.authors
	assert "R1A2" in report1.authors
	assert "R2A1" not in report1.authors
	assert "R2A2" not in report1.authors