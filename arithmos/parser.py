from lexer import Lexer
from lexer import Token

class Parser:

	def parse(self, exp):
		self.lexer = Lexer(exp)

		expression_value = self.expression()

		token = self.lexer.get_next_token()

		if token.kind == Token.End:
			return expression_value
		else:
			raise Error("Error while parsing expression. Couldn't find expression tail.")


	def expression(self):
		component1 = self.factor()
		additive_operators = [Token.Plus, Token.Minus]

		token = self.lexer.get_next_token()

		while token.kind in additive_operators:
			component2 = self.factor()

			if token.kind == Token.Plus:
				component1 = component1 + component2
			else:
				component1 = component1 - component2

			token = self.lexer.get_next_token()

		self.lexer.revert()

		return component1

	
	def factor(self):
		factor1 = self.number()

		multiplicative_operators = [Token.Multiply, Token.Divide]

		token = self.lexer.get_next_token()

		while token.kind in multiplicative_operators:
			factor2 = self.number()

			if token.kind == Token.Multiply:
				factor1 = factor1 * factor2
			else:
				factor1 = factor1 / factor2

			token = self.lexer.get_next_token()

		self.lexer.revert()

		return factor1

	def number(self):
		token = self.lexer.get_next_token()

		if token.kind == Token.LeftParenthesis:
			value = self.expression()

			expected_token = self.lexer.get_next_token()
			if expected_token.kind != Token.RightParenthesis:
				raise Error("Unable to find close parenthesis.")
		elif token.kind == Token.Number:
			value = token.value
		else:
			raise Error("Unknown expression element")

		return value

