from sqlalchemy import create_engine
engine = create_engine('mssql+pymssql://sa:1equinbd.@localhost\saga/saga')
import pandas as pd

df = pd.read_sql("select * from _ver", engine)
print (df)
