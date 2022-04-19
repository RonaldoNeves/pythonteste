# Ordem de precedência de operadores.
# 1° () parênteses
# 2° ** potência
# 3° *, /, //, %, Multiplicação, divisão, divisão inteira, resto da divisão
# 4° +, -, soma e subtração
n1 = int(input('digite um valor'))
n2 = int(input('outro valor'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('o valor da soma é {}, o produto {}, a divisão {:.3f}'.format(s, m, d), end='  ')
print('divisão inteira {}, potencia {}'.format(di, e))




