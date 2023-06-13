from sympy import Limit, Symbol, S # importando a biblioteca para cálculo

matricula = 1833 # num da matricula
c = matricula%10 # calculo de c baseado no material
x = Symbol('x') # definindo x como uma variável matemática

def funcao(x, c): # criando a função do exercício
    return (((c+1) - x**0.5)/((c+1)**2 - x))

# resultado do limite para cada valor da tendencia de x
res1 = Limit(funcao(x,c),x,(c+1)**2).doit() 
res2 = Limit(funcao(x,c),x,S.Infinity).doit()
res3 = Limit(funcao(x,c),x,-S.Infinity).doit()

print('\n'*100) # limpa o console para facilitar a visualização

# mostrando na saída
print('O valor do limite para x-->(c+1)² é de {}'.format(res1))
print('O valor do limite para x-->+oo é de {}'.format(res2)) 
print('O valor do limite para x-->-oo é de {}'.format(res3)) 