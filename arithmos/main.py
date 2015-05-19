import argparse

from parser import Parser
from lexer import Lexer
from lexer import Token


if __name__ == '__main__':
	arg_parser = argparse.ArgumentParser(description='Arithmos is a simple math expression parser for the command line')
	arg_parser.add_argument('-e','--expression', help='expression', required=True)
	args = arg_parser.parse_args()

	parser = Parser()
	value = parser.parse(args.expression)
	print value
