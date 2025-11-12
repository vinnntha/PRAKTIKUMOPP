import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('nilai_siswa.csv')
data.info()
data.head()
data.describe()

print("Rata-rata:", data['Nilai'].mean())
print("Median:", data['Nilai'].median())
print("Modus:", data['Nilai'].mode()[0])


matematika = data[data['Matpel'] == 'Matematika']
print(matematika)


rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-Rata Nilai per Matpel')
plt.xlabel('Mata pelajaran')
plt.ylabel('Nilai rata-rata')
plt.show()


sns.boxplot (x='Matpel', y='Nilai', data=data)
plt.title('Sebaran Nilai per Mata Pelajaran')
plt.show

