# -*- coding: utf-8 -*-

"""
Простой лексический анализатор. (мне лень было писать доку)
дрисня полная если честно, без токенизации и явной последовательности 
выполнения операторов.

"""
print("Доступные операции: +,-,*,/.")
expression = str(input("Введите математическое выражение: ")) or '2*2-4/2-1'


def sum(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b):
	if b != 0: return a / b
	else: return None



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
			sum_index = exp.find('+')
			if sum_index >-1: return sum(lex(exp[:sum_index]), lex(exp[sum_index+1:]))
			
			sub_index = exp.find('-')
			if sub_index >-1: return sub(lex(exp[:sub_index]), lex(exp[sub_index+1:]) )

			mul_index = exp.find('*')
			if mul_index >-1: return mul(lex(exp[:mul_index]), lex(exp[mul_index+1:]) )

			div_index = exp.find('/')
			if div_index >-1: return div(lex(exp[:div_index]), lex(exp[div_index+1:]) )
		except Exception as e:
			pass

	try: # Если строка - число, преобразуем тип и возвращаем значение.
		exp = float(exp)

		return exp
	except Exception as e:

		try: # тут мы находим все скобки, вычисляем их значения и вставляем в исходное выражение
			for i in range(exp.count('(')): 
				braces_indexes = [exp.rfind('('), exp.find(')')] # находим внутренние скобки
				if braces_indexes[0] > -1 and braces_indexes[1] > -1:
					braced_exp = exp[braces_indexes[0]+1:braces_indexes[1]]
					# print(exp) разкомменть для подробного разбора
					exp = exp[:braces_indexes[0]] + str(analize(braced_exp)) + exp[braces_indexes[1]+1:] # Склеиваем
					# print(exp) разкомменть для подробного разбора
			
			return analize(exp)

		except Exception as e:
			pass # Выдает вполне логичный результат при эксепшене

result = lex(expression)
print(f"{expression} = {result}")

input("Введите любую клавишу для выхода.")
