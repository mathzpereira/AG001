from sympy import Symbol, exp, solve, sin # importando a biblioteca para cálculo

matricula = 1833 # num da matricula
c = matricula%10 # calculo de c baseado no material
x = Symbol('x') # definindo x como uma variável matemática

# definindo as equações a serem resolvidas
def equacao_1(x):
    return exp(-x-1) + exp(-x-3) + exp(x) + 5*(c+1)

def equacao_2(x):
    return (c+2)*x**3 - (c+1)*x**2 - 5*x + 4*c

def equacao_3(x):
    return 2*sin(4*(c-3)*x) - 10

primeira_equacao = equacao_1(x)
segunda_equacao = equacao_2(x)
terceira_equacao = equacao_3(x)

# resolvendo as das equações
solucao_1 = solve(primeira_equacao)
solucao_2 = solve(segunda_equacao)
solucao_3 = solve(terceira_equacao)

# mostrando os resultados
print("Equação 1: ", solucao_1, "\n")
print("Equação 2: ", solucao_2, "\n")
print("Equação 3: ", solucao_3, "\n")