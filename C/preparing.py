from CodeGen import *

cpp = CppFile("index.h")

cpp('#ifndef CMAKEEXAMPLE_INDEX_H')
cpp('#define CMAKEEXAMPLE_INDEX_H\n')

cpp('/*!')
cpp('\\brief Алгоритм Евклида')
cpp('\param a,b Два числа, чей наибольший делитель мы хотим найти')
cpp('\return Наибольший общий делитель a, b')
cpp('')
cpp('Данная функция реализует алгоритм Евклида, при помощи которого')
cpp('находится наибольшее общее кратное у двух чисел.')
cpp('*/')

with cpp.block("int gcd(int a, int b)"):
    cpp('return b ? gcd(b, a % b) : a;')
cpp('#endif //CMAKEEXAMPLE_INDEX_H')

cpp.close()