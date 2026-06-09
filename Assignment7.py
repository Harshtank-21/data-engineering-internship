# Assignment 7
import pandas as pd

s1 = pd.Series({"A":1,"B":2})
s2 = pd.Series([10,20,30])
print(s1, s2)
print(s2[0])

df1 = pd.DataFrame([[1,"A"],[2,"B"]], columns=["ID","Name"])
df2 = pd.DataFrame({"ID":[1,2],"Marks":[90,80]})
df3 = pd.DataFrame([(1,"X"),(2,"Y")], columns=["ID","Grade"])
df4 = pd.DataFrame([{"ID":1,"City":"Jaipur"}])

for index,row in df2.iterrows(): print(row)
print(df2[df2["Marks"]>85])
print(df2.iloc[0])
df2.loc[len(df2)] = [3,70]
print(df2.values.tolist())
