"""

В этом модуле хранятся математические функции.

"""
import math

def sum(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b):
	if b != 0: return a / b
	else: return None

def sqrt(a): return math.sqrt(a)
def sin(a): return math.sin(a)
def cos(a): return math.cos(a)
def tg(a): return math.tan(a)
def ctg(a): return math.atan(a)
def ceil(a): return math.ceil(a)
def fabs(a): return math.fabs(a)
def factorial(a): return math.factorial(a)
def floor(a): return math.floor(a)
def trunc(a): return math.trunc(a)
def exp(a): return math.exp(a)
def expm1(a): return math.expm1(a)
def log1p(a): return math.log1p(a)
def log10(a): return math.log10(a)
def log2(a): return math.log2(a)
def sqrt(a): return math.sqrt(a)
def acos(a): return math.acos(a)
def asin(a): return math.asin(a)
def atan(a): return math.atan(a)
def degrees(a): return math.degrees(a)
def radians(a): return math.radians(a)
def cosh(a): return math.cosh(a)
def sinh(a): return math.sinh(a)
def tanh(a): return math.tanh(a)
def acosh(a): return math.acosh(a)
def asinh(a): return math.asinh(a)
def atanh(a): return math.atanh(a)
def gamma(a): return math.gamma(a)
def lgamma(a): return math.lgamma(a)

binary_operators = {
	'+' : sum,
	'-' : sub,
	'*' : mul,
	'/' : div,
}
actions_dict = {
	'#' : sin,
	'$' : cos,
	'@' : tg,
	'!' : ctg,
	'a' : ceil,
	'b' : fabs,
	'c' : factorial,
	'd' : floor,
	'e' : trunc,
	'f' : exp,
	'g' : expm1,
	'h' : log1p,
	'i' : log10,
	'j' : log2,
	'k' : sqrt,
	'l' : acos,
	'm' : asin,
	'n' : atan,
	'o' : degrees,
	'p' : radians,
	'q' : cosh,
	'r' : sinh,
	's' : tanh,
	't' : acosh,
	'u' : asinh,
	'v' : atanh,
	'y' : gamma,
	'z' : lgamma,
}

def replacer(exp):
	"""
	Заменяет слова-обозначения функций на удобные в обращении символы

	input: str
	output: str

	cos(1) --> $(1)

	"""
	exp = exp.replace('pi', '3.141592653589793').replace('e', '2.718281828459045')
	for symbol, function in actions_dict.items():
		exp = exp.replace(f'{function.__name__}', f'{symbol}', )
		
	return exp



def recursive_descent(exp):
	"""
	"""
	try:
		# ===================================================================== #
		# Реализация рекурсивного спуска для бинарных операторов 
		for operator, function in binary_operators.items():
			if exp.find(operator) > -1: return function(lex(exp[:exp.find(operator)]), lex(exp[exp.find(operator)+1:]))

		# ===================================================================== #
		# Реализация рекурсивного спуска для функций
		for func_symbol, function in actions_dict.items():
			if exp.find(func_symbol) > -1:
				return function(lex(exp[exp.find(func_symbol)+1:len(exp)]))


	except Exception as e:
		print(e)
		pass



