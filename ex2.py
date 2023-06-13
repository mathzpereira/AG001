from sympy import Derivative, Symbol, S # importando a biblioteca para cálculo

matricula = 1833 # num da matricula
c = matricula%10 # calculo de c baseado no material
t = Symbol('t') # definindo t como uma variável matemática

def funcao(t, c): # criando a função do exercício
    return (t**(1/3)/5) + ((c+1)/(t**3)) - ((c+2)*(t**2)) - 15

eqVel = Derivative(funcao(t,c),t).doit() # derivando a posição para ter a velocidade
vel7 = Derivative(funcao(t,c),t).doit().subs({t:7}) # calculando a velocidade no ponto t = 7s
eqAce = Derivative(funcao(t,c),t,2).doit() # derivando a posição duas vezes para ter a aceleração
ace2 = Derivative(funcao(t,c),t,2).doit().subs({t:2}) # calculando a aceleração no ponto t = 2s

print('\n'*100) # limpa o console para facilitar a visualização

# mostrando a saída
print("Equação da velocidade:", eqVel)
print("Velocidade em t = 7s= {:.2f} m/s".format(vel7))
print("Equação da aceleração:", eqAce)
print("Aceleração em t = 2s= {:.2f} m/s".format(ace2))