import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Kroki 1 i 2: Wczytanie danych i standaryzacja
data = pd.read_csv("customers.csv")

# Wyświetlenie danych
plt.figure(figsize=(8, 6))
plt.scatter(data["MonthlySpend"], data["PurchaseFrequency"], s=50)
plt.title('Dane klientów sklepu internetowego')
plt.xlabel('Wydatki miesięczne')
plt.ylabel('Ilość dokonanych zakupów')
plt.show()

# Standaryzacja danych
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Kroki 3: Klastrowanie danych
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(scaled_data)
clusters = kmeans.predict(scaled_data)
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)

# Wyświetlenie wyników klastryzacji
plt.figure(figsize=(8, 6))
plt.scatter(data["MonthlySpend"], data["PurchaseFrequency"], c=clusters, cmap='viridis', s=50)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200, alpha=0.75, label='Centra klastrów')
plt.title('Klastrowanie klientów sklepu internetowego')
plt.xlabel('Wydatki miesięczne')
plt.ylabel('Ilość dokonanych zakupów')
#plt.colorbar(label='Klaster')
plt.legend()
plt.show()
