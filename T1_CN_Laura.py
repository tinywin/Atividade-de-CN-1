import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x + 2

# Definindo o intervalo inicial [a, b] e a tolerância
a = -2
b = 0
tolerancia = 10**-3
iteracao_maxima = 100

# Lista para armazenar os dados de cada iteração
dados = []

# Encontrando a raiz pelo método da bisseção
x0 = a
iteracao_atual = 0
while (b - a) / 2 > tolerancia and iteracao_atual < iteracao_maxima:
    x1 = (a + b) / 2
    fx1 = f(x1)
    iteracao_atual += 1
    dados.append([iteracao_atual, a, b, x1, fx1, abs(b-a)/2])
    
    if fx1 == 0 or abs(x1 - x0) < tolerancia:
        break
    
    if f(a) * fx1 < 0:
        b = x1
    else:
        a = x1
    
    x0 = x1

# Imprimindo a tabela
print("n    a_n         b_n         x_n         f(x_n)       epsilon")
for i, (n, an, bn, xn, fxn, epsilon) in enumerate(dados):
    print(f"{n:<5}{an:<12}{bn:<12}{xn:<12}{fxn:<12}{epsilon:<12}")

# Definindo um intervalo mais amplo para a visualização do gráfico
x_vals = np.linspace(-2, 2, 1000)
y_vals = f(x_vals)

plt.figure(figsize=(10, 5))

# Plotando a função com a linha azul
plt.plot(x_vals, y_vals, label='f(x)', color='blue')

# Linha y=0 (eixo x)
plt.axhline(0, color='black', lw=0.5)

# Pontos de aproximação da raiz
for ponto in dados:
    plt.plot(ponto[3], ponto[4], 'ro')  # Ponto da raiz aproximada

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da função e aproximações da raiz pelo Método da Bisseção')
plt.legend()
plt.grid(True)
plt.show()
