import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generowanie sztucznych danych z 3 klastrami
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.6, random_state=0)

# Zapis danych do pliku CSV
data = pd.DataFrame(X, columns=["Feature 1", "Feature 2"])
data.to_csv("generated_data.csv", index=False)

# Wyświetlenie wygenerowanych danych
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title('Wygenerowane dane')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

# Inicjalizacja i dopasowanie modelu k-średnich
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Wyświetlenie wyników klastryzacji
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=50, cmap='viridis')

# Wyświetlenie centrów klastrów
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
plt.title('Klasterowanie metodą k-średnich')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()