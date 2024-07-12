import csv
import random

# Generowanie większej ilości danych klientów
def generate_customer_data(num_customers):
    customers_data = []
    for _ in range(num_customers):
        monthly_spend = random.uniform(50, 500)  # Losowe wydatki miesięczne z zakresu 50-500
        purchase_frequency = random.randint(1, 10)  # Losowa ilość dokonanych zakupów z zakresu 1-10
        customers_data.append({"MonthlySpend": monthly_spend, "PurchaseFrequency": purchase_frequency})
    return customers_data

# Zapis do pliku CSV
num_customers = 400  # Określenie ilości klientów
customers_data = generate_customer_data(num_customers)

with open("customers6.csv", "w", newline='') as csvfile:
    fieldnames = ["MonthlySpend", "PurchaseFrequency"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for customer in customers_data:
        writer.writerow(customer)

print(f"Plik 'customers.csv' został wygenerowany z danymi dla {num_customers} klientów.")