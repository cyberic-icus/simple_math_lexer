# simple_math_lexer
Программа представляет собой простой калькулятор без графического интерфейса.
Принимает математическое выражение в виде строки как входные данные, возваращает значение типа float, либо None, в случае недопустимого значения.

                                                                Она состоит из 2 частей:
Часть 1: Упрощение исходного выражения в более простой вид.--					
В этой части функция lex преобразует входное выражение в удобную для работы екурсивного спуска строку, которую потом примет в качестве аргумента функция analize. 
	
Часть 2: Вычисление значения преобразованного математического выражения.--
Для вычисления значения используется алгоритм, похожий на алгоритм рекурсивного спуска.


Реализация алгоритма вычисления выражения отличается от стандартного алгоритма рекурсивного спуска. 

Usage: прямой запуск, либо из консоли(с 1 аргументом)


