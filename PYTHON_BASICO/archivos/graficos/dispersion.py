import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("archivos\\graficos\\dispersion.csv")
print(df)

sns.scatterplot(x="tiempo",y="dinero",data=df)

plt.show()