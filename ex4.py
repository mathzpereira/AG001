from sympy import Symbol, solve # importando a biblioteca para cálculo

matricula = 1833 # num da matricula
c = matricula%10 # calculo de c baseado no material
i1 = Symbol('i1') # definindo i1 como uma variável matemática
i2 = Symbol('i2') # definindo i2 como uma variável matemática
i3 = Symbol('i3') # definindo i3 como uma variável matemática
v1 = 7 + (2*c)
v2 = 12 + (2*c)

def malha1(v1, i1, i3): # criando a equação malha 1
    return -v1 + 25*i1 + 10*i1 + 10*i3

def malha2(v2, i1, i3): # criando a equação malha 2
    return -v2 + 20*i3 + 10*i3 + 10*i1

# resolvendo o sistema de equações
f = malha1(v1, i1, i3)
g = malha2(v2, i1, i3)
res = solve((f,g))
i2 = -(res[i1] + res[i3]) # as correntes entram no nó e são somadas (sinal negativo por causa do sentido)

print('\n'*100) # limpa o console para facilitar a visualização

# mostrando a saída
print("Corrente I1:", res[i1], "[A]")
print("Corrente I2:", i2, "[A]")
print("Corrente I3:", res[i3], "[A]")