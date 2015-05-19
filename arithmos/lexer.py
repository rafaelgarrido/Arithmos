import re

class Lexer:
	"""Arithmos Lexer"""

	def __init__(self, exp_input):
		self.input = exp_input
		self.return_prev_token = False
		self.previous_token = None
		self.token_handlers = [
			(r'\A\+', Token.Plus),
			(r'\A\-', Token.Minus),
			(r'\A\*', Token.Multiply),
			(r'\A\\', Token.Divide),
			(r'\A\(', Token.LeftParenthesis),
			(r'\A\)', Token.RightParenthesis),
			(r'\A\d+(\.\d+)?', Token.Number),
			(r'', Token.End)
		]

	def get_next_token(self):
		if self.return_prev_token is True:
			self.return_prev_token = False
			return self.previous_token

		self.input = self.input.lstrip()

		token = self.fetch_token()

		self.previous_token = token

		return token

	def revert(self):
		self.return_prev_token = True

	def fetch_token(self):
		
		for regex, kind, in self.token_handlers:
			match = re.match(regex, self.input)
		
			if match:
				value = match.group()
				token = Token.create(kind, value)
				self.input = self.input.replace(value, "", 1)
				return token
		
		return Token.create(Token.Unknown, self.input)


class Token:
	"""Arithmos Tokens"""
	
	Plus, Minus, Multiply, Divide, Number, LeftParenthesis, RightParenthesis, End, Unknown = range(0, 9)

	def __init__(self, kind, value):
		self.kind = kind
		self.value = value

	def unknown(self):
		return self.kind == Token.Unknown

	def create_token(kind, value):
		class NumberToken(Token):
			pass
		class OperatorToken(Token):
			pass
		class EndToken(Token):
			pass
		class UnknownToken(Token):
			pass

		if kind == Token.Number:
			return NumberToken(kind, float(value))
		elif kind == Token.End:
			return EndToken(kind, value)
		elif kind == Token.Unknown:
			return UnknownToken(kind, value)
		else:
			return OperatorToken(kind, value)

	# static methods
	create = staticmethod(create_token)

