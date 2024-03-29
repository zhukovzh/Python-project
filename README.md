# Python-project
Это программа-калькулятор. Суть программы в следующем. На вход подаётся строка, являющаяся математическим выражением, 
а программа должна ее корректно распарсить и вывести результат. Кроме того, программа умеет строить графики
заданных ей функций.
Более подробно:

1) Программа просит на вход единственную строку. 
Это строка может быть математическим выражением содержащим вещественные числа, арифметические операции,
а также функции exp, ln, sin, cos, sqrt, a^x. Если строка является коректным математическим выражением, то программа выводит
единственное число - результат выражения.
Примеры работы:
Input: (2 + (3 * (4 + 2))) / (2 * (20 + 5))
Output: 0.4

Input: (2^3 + exp(0) - ln(exp(10))) / (sin(pi/6) + cos(pi/3))
Output: -1

Также программа обрабатывает некорректные выражения следующих видов:
  a) Ноль в знаменателе (в любом виде)
  b) Неправильные скобочные последовательности 1 + (2 + (3 + 4)
  с) Выражения вида 3 * / 4
  
2) Кроме того программа может строить график функции. Для этого в единственной входной строке 
надо написать слово 'curve' и функцию от переменной x, содержащую арифметические операции и функции, указанные выше.
Например,   'curve x + ln(37* x - 3) + 50 * sin(x / 50)'.
График строится на координатной плоскости с ограничениями на x и y [-500; 500].
