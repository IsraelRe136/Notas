import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("archivos\\graficos\\cofla_ingresos.csv")
print(df)

sns.barplot(x="fuente",y="ingresos",data=df)
total_ingresos=df['ingresos'].sum()
print(total_ingresos)
plt.show()