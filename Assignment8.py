# Assignment 8
import pandas as pd

dates = pd.to_datetime(["2026-01-01","2026-01-02"])
print(dates)

df1 = pd.DataFrame({"ID":[1,2],"Name":["A","B"]})
df2 = pd.DataFrame({"ID":[1,3],"Marks":[90,80]})
print(pd.merge(df1,df2,on="ID",how="inner"))
print(pd.merge(df1,df2,on="ID",how="left"))
print(pd.merge(df1,df2,on="ID",how="right"))

df3 = pd.DataFrame({"ID":[1,2],"City":["X","Y"]})
combined = pd.concat([df1,df1])
print(pd.merge(combined,df3,on="ID"))
