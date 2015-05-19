from nose.tools import *
from arithmos.lexer import Lexer
from arithmos.lexer import Token

def assert_valid_token(token, kind, value):
	assert token is not None
	assert token.unknown is not True
	assert token.kind == kind
	assert token.value == value

def assert_invalid_token(token, kind, value):
	#print token, kind, value
	#print token, token.kind, token.value

	assert token is not None
	assert token.unknown
	assert token.kind == kind
	assert token.value == value

def test_create_lexer():
	lexer = Lexer("10")
	assert lexer.input == "10"
	assert lexer.previous_token is None
	assert lexer.return_prev_token is False

def test_match_number():
	lexer = Lexer("10")
	token = lexer.get_next_token()
	assert_valid_token(token, Token.Number, 10.0)

def test_match_plus():
	val = "+"
	lexer = Lexer(val)
	token = lexer.get_next_token()
	assert_valid_token(token, Token.Plus, val)

def test_match_minus():
	val = "-"
	lexer = Lexer(val)
	token = lexer.get_next_token()
	assert_valid_token(token, Token.Minus, val)

def test_match_multiply():
	val = "*"
	lexer = Lexer(val)
	token = lexer.get_next_token()
	assert_valid_token(token, Token.Multiply, val)

def test_match_divide():
	val = "\\"
	lexer = Lexer(val)
	token = lexer.get_next_token()
	assert_valid_token(token, Token.Divide, val)

def test_match_left_parenthesis():
	val = "("
	lexer = Lexer(val)
	token = lexer.get_next_token()
	assert_valid_token(token, Token.LeftParenthesis, val)

def test_match_right_parenthesis():
	val = ")"
	lexer = Lexer(val)
	token = lexer.get_next_token()
	assert_valid_token(token, Token.RightParenthesis, val)

def test_match_end():
	val = ""
	lexer = Lexer(val)
	token = lexer.get_next_token()
	assert_valid_token(token, Token.End, val)

def test_match_end_spaced():
	val = " "
	lexer = Lexer(val)
	token = lexer.get_next_token()
	assert_valid_token(token, Token.End, "")

#def test_match_unknown_chars():
#	val = "ABC"
#	lexer = Lexer(val)
#	token = lexer.get_next_token()
#	assert_invalid_token(token, Token.Unknown, val)

#def test_match_unknown_new_line():
#	val = "\n"
#	lexer = Lexer(val)
#	token = lexer.get_next_token()
#	assert_invalid_token(token, Token.Unknown, "")

#def test_match_unknown_tab():
#	val = "\t"
#	lexer = Lexer(val)
#	token = lexer.get_next_token()
#	assert_invalid_token(token, Token.Unknown, "")

