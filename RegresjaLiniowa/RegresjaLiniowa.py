import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
#print(data)

def gradient_descent(m_now, b_now, data, L):
    m_gradient = 0
    b_gradient = 0

    n = len(data)

    for i in range(n):
        x = data.iloc[i].x
        y = data.iloc[i].y

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * L
    b = b_now - b_gradient * L
    return m, b

m = 0
b = 0
L = 0.0001
epochs = 300

for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m, b = gradient_descent(m,b,data,L)

print(m,b)

#utworzenie wykresu 
plt.scatter(data.x, data.y)
plt.xlabel("doświadczenie (w miesiącach)")
plt.ylabel("zarobek (w tysiącach)")
plt.plot(list(range(0,50)), [m * x + b for x in range(0,50)], color = "red")
plt.show()