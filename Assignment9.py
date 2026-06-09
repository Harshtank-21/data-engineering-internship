# Assignment 9
import re
import pandas as pd

email = "test@example.com"
print(bool(re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)))

mobile = "9876543210"
print(bool(re.match(r'^[6-9]\d{9}$', mobile)))

print(pd.Timestamp.now())
print(pd.date_range("2026-01-01", periods=5))

df = pd.DataFrame({"A":[1,None,3],"B":[4,5,None]})
print(df.fillna(df.mean()))
