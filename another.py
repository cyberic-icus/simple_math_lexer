# -*- coding: utf-8 -*-
print("Доступные операции: +,-,*,/.")
expression = str(input("Введите математическое выражение без скобок: ")) or '2*2-4/2-1'

def sum(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b):
	if b != 0: 
		return a / b
	else: return 0 



def lex(exp):
	"""
	Простой лексический анализатор простых(без скобок, возведения в степень и извлечения корня и т.д.)
	математических выражений. 

	Input: str 
	Output: float

	Алгоритм : рекурсивный спуск 

	Input: 2*2-4/2-1
	2*2-4/2-1= sub(2*2-4/2, 1) = sub(sub(2*2,4/2), 1) = sub(sub(mul(2,2),div(4,2)), 1) 
	Output: 1.0

	"""

	try: # Если строка - число, преобразуем тип и возвращаем значение.
		exp = float(exp)
		return exp
	except Exception as e: 
		# Именно данная последовательность нахождения мат. операторов
		# позволяет получить правильную последовательность выполнения
		# мат. операций.

		# Функция rfind возвращает -1 при отсутствии оператора.
		try:
			sum_index = exp.rfind('+')
			if sum_index >-1: return sum(lex(exp[:sum_index]), lex(exp[sum_index+1:]))
			
			sub_index = exp.rfind('-')
			if sub_index >-1: return sub(lex(exp[:sub_index]), lex(exp[sub_index+1:]) )

			mul_index = exp.rfind('*')
			if mul_index >-1: return mul(lex(exp[:mul_index]), lex(exp[mul_index+1:]) )

			div_index = exp.rfind('/')
			if div_index >-1: return div(lex(exp[:div_index]), lex(exp[div_index+1:]) )
		except Exception as e:
			pass # Выдает вполне логичный результат


		

result = lex(expression)
print(f"{expression} = {result}")

input("Введите любую клавишу для выхода.")