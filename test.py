import pandas as pd

df = pd.read_csv('data.csv')
df1 = df.groupby('學校名稱')['總計'].sum()

df2 = pd.DataFrame(df1)
# print("每個隊伍的總得分:")
print(df2)
