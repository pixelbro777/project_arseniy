import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('bestsellinggames.csv')
res1 = df['Sales']
res2=df['Initial release date']
res3 = df.groupby(by='Initial release date')['Sales'].mean()

df.plot(kind='scatter', x = 'Platform(s)', y='Sales')
plt.xticks(rotation=20)
plt.show()
res4=df['Sales']
res5=df['Publisher(s)']
df.plot(kind='scatter',x='Developer(s)',y='Sales')
plt.xticks(rotation=45)
plt.show()
res6=df['Sales']
res7=df['Initial release date']
df.plot(kind='scatter',x='Initial release date',y='Sales')
plt.xticks(rotation=45)
plt.show()
#a=df.describe()
#print(a)