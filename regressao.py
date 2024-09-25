import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy.stats import pearsonr

class AdalineRegressor:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs

    def fit(self, X, y):
        # Inicializando pesos
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        self.cost = []

        for _ in range(self.epochs):
            output = self.activation(X)
            errors = y - output
            # Atualizando os pesos
            self.weights += self.learning_rate * X.T.dot(errors)
            self.bias += self.learning_rate * errors.sum()
            # Calculando o custo (erro quadrático médio)
            cost = (errors**2).sum() / 2.0
            self.cost.append(cost)

    def activation(self, X):
        return np.dot(X, self.weights) + self.bias

    def predict(self, X):
        return self.activation(X)

# Carregar a base de dados
data = {
    'x': [-3.4557427, -3.4822109, -3.1973477, -2.9263939, -1.9737541, -1.9189151, -1.9781052,
          -1.0670384, -1.4996849, -1.1159294, -0.781221, -0.5649162, -0.0050037, 0.1969329,
          0.3321719, 0.8792238, 1.0729627, 1.2940016, 1.4121696, 2.0611459, 2.1194811, 2.9184708,
          2.3294477, 3.0532795, 3.1210985, 3.5576675, 3.7092212, 3.8422916, 4.7783129, 4.4976173,
          4.683564, 5.5428325, 5.2959788, 6.1256565, 6.5558376, 6.4062025, 6.6951968, 7.4498412,
          6.9709788, 7.3426909, 7.9904375, 8.3039034, 8.685398, 9.1763368, 9.0756499, 9.2065044,
          9.530235, 10.350861, 10.663104, 10.343534],
    'y': [-1.6239881, -1.0618243, -1.3302606, -0.8884057, -0.9198156, -0.4542355, -0.2378872,
          -0.451436, -0.1417166, 0.464144, 0.8016596, 0.2934546, 1.1213746, 0.8547785, 1.2483002,
          1.8912561, 1.8531781, 1.9523057, 1.8967559, 2.7176396, 2.2022322, 2.5712507, 3.3505474,
          3.5432877, 3.4236653, 4.0951618, 3.9549787, 4.5025232, 3.7643277, 4.666918, 4.5328549,
          4.9349832, 5.3850333, 4.7989586, 5.7666838, 6.0690915, 5.9136599, 6.1221843, 6.5711131,
          6.0160765, 6.722859, 6.492281, 7.2993508, 7.0432869, 7.5261253, 8.1722142, 8.1273208,
          7.595554, 8.3859757, 8.3096467]
}

df = pd.DataFrame(data)
X = df['x'].values.reshape(-1, 1)
y = df['y'].values

# Treinando o modelo Adaline
adaline = AdalineRegressor(learning_rate=0.0001, epochs=1000)
adaline.fit(X, y)

# Plotando a linha de regressão e os dados
plt.scatter(X, y, color='blue', label='Observações')
plt.plot(X, adaline.predict(X), color='red', label='Linha de Regressão')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regressão Linear com Adaline')
plt.legend()
plt.show()

# Calculando o coeficiente de correlação de Pearson e R²
pearson_corr, _ = pearsonr(df['x'], df['y'])
r2 = r2_score(y, adaline.predict(X))

print(f"Coeficiente de Correlação de Pearson: {pearson_corr}")
print(f"Coeficiente de Determinação (R²): {r2}")