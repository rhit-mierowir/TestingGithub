from typing import Callable, Any, Iterable 
import pytest
"""
This file includes examples of the following things:
	1. Writing Basic Tests and Type Annotations
	2. Types for Functions Returning functions (Callables)
	3. Using Parameterize to test simple variations, adding comments to asserts
	4. Typing Lists and Tupples
	5. Testing for Exceptions & Errors

	TODO: Iterable, Protocols, Dataclasses
	TODO: Try out useing the interface idea that I thought of over break to test common interfaces for simple actions

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