import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    data = response.json()  
    print(data)  
else:
    print(f"Error: {response.status_code}")



import pandas as pd

data = pd.read_csv('data.csv') 

print(data.describe())  
print(data.head())     



import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y, marker='o')
plt.title("Простой график")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()  
