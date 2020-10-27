# -*- coding: utf-8 -*-
"""
Программа представляет собой простой калькулятор.
																Она состоит из 2 частей:
1) Упрощение исходного выражения в более простой вид.								| 2) Вычисление значения преобразованного математического выражения.
	В этой части функция lex преобразует входное выражение в удобную для работы		|	  Для вычисления значения используется алгоритм, похожий на алгоритм рекурсивного спуска.
строку, которую потом примет в качестве аргумента функция analize. 					|

Реализация алгоритма вычисления выражения отличается от стандартного алгоритма рекурсивного спуска. Доку допишу завтра.


"""
import math
import sys



def sum(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b):
	if b != 0: return a / b
	else: return None

def cos(a): return math.cos(a)
def sin(a): return math.sin(a)
def tg(a): return math.tan(a)
def ctg(a): return math.atan(a)


def lex(exp):
	"""
	Лексический анализатор математических выражений. Принимает строку-мат. выражение как входные данные
	и считает его значение

	Input: str 
	Output: float

	Самый дебильный алгоритм рекурсивного спуска: значения из скобок вручную вставляются в выражение. 
	Однако эта херня работает.

	"""
	def analize(exp):
		"""
		Фактический анализатор простых математических выражений

		Input: str 
		Output: float

		Input: 2*2-4/2-1
		2*2-4/2-1= sub(2*2-4/2, 1) = sub(sub(2*2,4/2), 1) = sub(sub(mul(2,2),div(4,2)), 1) ---переписать надо бы
		Output: 1.0
		"""

		# Именно данная последовательность нахождения мат. операторов
		# позволяет получить правильную последовательность выполнения
		# мат. операций.

		# Функция find возвращает -1 при отсутствии оператора, иначе индекс
		try:
			# ===================================================================== #
			# Реализация рекурсивного спуска для бинарных операторов 
			sum_index = exp.find('+')
			if sum_index >-1: return sum(lex(exp[:sum_index]), lex(exp[sum_index+1:]))
			
			sub_index = exp.find('-')
			if sub_index >-1: return sub(lex(exp[:sub_index]), lex(exp[sub_index+1:]) )

			mul_index = exp.find('*')
			if mul_index >-1: return mul(lex(exp[:mul_index]), lex(exp[mul_index+1:]) )

			div_index = exp.find('/')
			if div_index >-1: return div(lex(exp[:div_index]), lex(exp[div_index+1:]) )

			# ===================================================================== #
			# Реализация рекурсивного спуска для функций 
			sin_index = exp.find('#')
			if sin_index >-1: return sin(lex(str(exp[sin_index+1:len(exp)])))

			cos_index = exp.find('$')
			if cos_index >-1: return cos(lex(exp[cos_index+1:len(exp)]))

			tg_index = exp.find('@')
			if tg_index >-1: return tg(lex(exp[tg_index+1:len(exp)]))

			ctg_index = exp.find('!')
			if ctg_index >-1: return ctg(lex(exp[ctg_index+1:len(exp)]))

			# ===================================================================== #
			if type(float(exp)) is float or type(exp) is int: 
				return str(exp)

		except Exception as e:
			pass



	exp = exp.replace('sin', '#')
	exp = exp.replace('cos', '$')
	exp = exp.replace('tg', '@')
	exp = exp.replace('ctg', '!')

	exp = exp.replace('pi', f'{math.pi}')
	exp = exp.replace('e', f'{math.e}')
	

	try: # Если строка - число, преобразуем тип и возвращаем значение.
		exp = float(exp)
		return exp
	except Exception as e:
		try: # тут мы находим все скобки, вычисляем их значения и вставляем в исходное выражение print(f'{}')
			for _ in range(exp.count('(')): 
				braces_indexes = [exp.rfind('('), exp.find(')', exp.rfind('('))] # находим внутренние скобки
				if braces_indexes[0] > -1 and braces_indexes[1] > -1:
					braced_exp = exp[braces_indexes[0]+1:braces_indexes[1]]
					exp = exp[:braces_indexes[0]] + str(analize(braced_exp)) + exp[braces_indexes[1]+1:] # Склеиваем
					
			
			return analize(exp)

		except Exception as e:
			pass # Выдает вполне логичный результат при эксепшене



if __name__ == '__main__':
	print("Доступные операции: +,-,*,/.")
	expression = sys.argv[1] or str(input()) # Можно сделать переменное число аргументов
	result = lex(expression)
	print(f"{expression} = {result}")

