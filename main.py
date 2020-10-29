# -*- coding: utf-8 -*-

import functions

info = {
	'+':': Сложение.',
	'-':': Вычитание.',
	'*':': Умножение.',
	'/':': Деление.',
	'cos(<выражение>)':':  косинус.',
	'sin(<выражение>)':': синус.',
	'tg(<выражение>)':': тангенс.',
	'ctg(<выражение>)':': котангенс.',
	'ceil(<выражение>)':'округление до ближайшего большего числа.',
	'fabs(<выражение>)':'модуль <выражение>.',
	'factorial(<выражение>)':'факториал числа <выражение>.',
	'floor(<выражение>)':'округление вниз.',
	'trunc(<выражение>)':'усекает значение <выражение> до целого.',
	'exp(<выражение>)':'e в степени <выражение>.',
	'log10(<выражение>)':'логарифм <выражение> по основанию 10.',
	'log2(<выражение>)':'логарифм <выражение> по основанию 2.',
	'sqrt(<выражение>)':'квадратный корень из <выражение>.',
	'acos(<выражение>)':'арккосинус <выражение>. В радианах.',
	'asin(<выражение>)':'арксинус <выражение>. В радианах.',
	'atan(<выражение>)':'арктангенс <выражение>. В радианах.',
	'degrees(<выражение>)':'конвертирует радианы в градусы.',
	'radians(<выражение>)':'конвертирует градусы в радианы.',
	'cosh(<выражение>)':'вычисляет гиперболический косинус.',
	'sinh(<выражение>)':'вычисляет гиперболический синус.',
	'tanh(<выражение>)':'вычисляет гиперболический тангенс.',
	'acosh(<выражение>)':'вычисляет обратный гиперболический косинус.',
	'asinh(<выражение>)':'вычисляет обратный гиперболический синус.',
	'atanh(<выражение>)':'вычисляет обратный гиперболический тангенс.',
	'gamma(<выражение>)':'гамма-функция <выражение>.',
	'lgamma(<выражение>)':'натуральный логарифм гамма-функции <выражение>.',
	'Число pi':': 3.141592653589793',
	'Число e':': 2.718281828459045',
}

def recursive_descent(exp):
	"""
	В этой функции реализован алгоритм рекурсивного спуска. 

	Input: str 
	Output: float
	Input: 2*2-4/2-1
	2*2-4/2-1 = sub(2*2, 4/2-1) = sub(mul(2,2), sub(4/2,1))= sub(mul(2,2),sub(div(4,2),1))
	Output: 1.0

	"""
	try:
		# ===================================================================== #
		# Реализация рекурсивного спуска для бинарных операторов 

		for operator, function in functions.binary_operators.items():
			if exp.find(operator) > -1: return function(calculate(exp[:exp.find(operator)]), calculate(exp[exp.find(operator)+1:]))

		# ===================================================================== #
		# Реализация рекурсивного спуска для функций
		for func_symbol, function in functions.actions_dict.items():
			if exp.find(func_symbol) > -1:
				return function(calculate(exp[exp.find(func_symbol)+1:len(exp)]))

		if type(float(exp)) is float or type(exp) is int: 
					return str(exp)

	except Exception as e:
		pass

def calculate(exp):
	"""
	Функция преобразования выражения. Заменяет слова функций на символы для удобства работы,
	преобразует в выражение без скобок, с готовыми для работы данными.

	Input: str 
	Output: float

	"""
	# Преобразуем выражение в более удобный вид.
	exp = functions.replacer(exp)
	
	try: # Если строка - число, преобразуем тип и возвращаем значение.
		exp = float(exp)
		return exp
	except Exception as e:
		try: # тут мы находим все скобки, вычисляем их значения и вставляем в исходное выражение print(f'{}')
			for _ in range(exp.count('(')): 
				braces_indexes = [exp.rfind('('), exp.find(')', exp.rfind('('))] # находим внутренние скобки
				if braces_indexes[0] > -1 and braces_indexes[1] > -1:
					braced_exp = exp[braces_indexes[0]+1:braces_indexes[1]]
					exp = exp[:braces_indexes[0]] + str(recursive_descent(braced_exp)) + exp[braces_indexes[1]+1:] # Склеиваем
					
			return recursive_descent(exp)

		except Exception as e:
			pass # Выдает вполне логичный результат при эксепшене

if __name__ == '__main__':
	print("Доступные операции:")
	for item in info.items():
		print(' ',item[0], item[1])
	expression = str(input('>>> '))
	result = calculate(expression)
	print(f"{expression} = {result}")
	input("Нажмите любую кнопку для выхода.")