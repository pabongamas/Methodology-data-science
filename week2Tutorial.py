import pandas as pd 
# We will always assume that the data file is in a subdirectory called "Data" 
#to read all document , its withe file but doesn't specific index
# data = pd.read_csv("credit.csv") 
#for remove the column index initially , add parameter index_col=0
data = pd.read_csv("credit.csv",index_col=0) 
#put name to index_col "obs"
data.index.name="Obs"
type(data) # type shows the type of any Python object 
data.head() 
# data.tail() 
# data.info() 