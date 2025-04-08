import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Rastgele veri oluşturma
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, 100)

# Veriyi Pandas DataFrame'e dönüştürme
data = pd.DataFrame({'X': x, 'Y': y})

# Veriyi görselleştirme
plt.figure(figsize=(10, 6))
plt.scatter(data['X'], data['Y'], label='Veri')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Basit Veri Analizi')
plt.legend()
plt.grid(True)

# Regresyon çizgisi ekleme
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x,p(x),"r--", label='Regresyon Çizgisi')

plt.legend()
plt.show()
