from nose.tools import *
from arithmos.parser import Parser
from arithmos.lexer import Lexer
from arithmos.lexer import Token

def test_3_plus_2_eq_5():
	parser = Parser()
	value = parser.parse("3 + 2")
	print value
	assert value == 5

def test_3_times_2_eq_6():
	parser = Parser()
	value = parser.parse("3 * 2")
	print value
	assert value == 6

def test_3_times_2_plus_5_eq_11():
	parser = Parser()
	value = parser.parse("3 * 2 + 5")
	print value
	assert value == 11

def test_3_times__par_2_plus_5_par_eq_21():
	parser = Parser()
	value = parser.parse("3 * (2 + 5)")
	print value
	assert value == 21
