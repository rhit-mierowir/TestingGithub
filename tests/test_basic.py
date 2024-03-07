
import pytest

def add_one(x: int):
	return x+1

def test_add_one():
	assert add_one(5) == 6
	assert add_one(10) == 11
