import pandas as pd
data=pd.read_csv('Credit.csv',index_col=0)
data.index.name = "Obs"
#the head are the first 5 rows in this case of the column 'income'
#Selecting a column by label
data['Income'].head()
#selecting multiple columns by label
# data[['Income','Education']].head()
#this one is the same to the next lines
columnsToShow=['Income','Education']
data[columnsToShow].head()
#show head specific index
data.iloc[:,[0]].head(30)
# show head specific range , shold be specified not int array , just separated by ,
#the range is gonna be 0 to 5, this is for multiple columns
data.iloc[:,0:5].head(30)


## select by rows  by labels, in this gonna be showed the row 1,2, 5
#with all his columns
data.loc[[1,2,5],:]
#this one shows the same but in a range of the row 1 up to row 5
data.loc[1:5,:]





