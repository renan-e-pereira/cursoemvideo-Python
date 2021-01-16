n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('soma: {}\nmultiplicaçaõ: {}\ndivisão: {:.3f}'
      '\ndivisão inteira: {}\npotência: {}'
      .format(s, m, d, di, e))
