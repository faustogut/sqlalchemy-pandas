from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///chinook.db')
df = pd.read_sql("SELECT * FROM albums limit 10", engine)
print (df)
