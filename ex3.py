from sympy import Symbol, Integral # importando a biblioteca para cálculo

matricula = 1833 # num da matricula
c = matricula%10 # calculo de c baseado no material
x = Symbol('x') # definindo x como uma variável matemática

def forca(x, c): # criando a função do exercício
    return (x**2)/5 + x**(4/5) + (c+3)*x - 10

# calcula o trabalho por meio da integral definida da função que define a força variável
trabalho = Integral(forca(x,c), (x, 1, 12)).doit()

print('\n'*100) # limpa o console para facilitar a visualização
print("O trabalho realizado pela força entre 1 m e 12 m é de {:.2f}".format(trabalho),"[J]") # saída