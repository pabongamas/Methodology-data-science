import pandas as pd
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix


data=pd.read_csv('credit.csv',index_col=0)
data.index.name='Obs'
# print(data.info)
# Dimension of dataset, i.e, rows and columns
# print(data.shape)

# Statistical summary of the dataset
# print(data.describe())



# To find the number of instances (rows) that belong 
#to each class. Can be done for any nominal variable
print(data.groupby('Married').size())

 # box and whisker plots
data.plot(kind='box', subplots=True, layout=(2,4), sharex=False, sharey=False)
plt.show()

# histograms
data.hist()
plt.show()

 # scatter plot matrix
scatter_matrix(data)
plt.show()

married_counts=data['Married'].value_counts()
print(married_counts)
married_counts.plot(kind='bar',color=['skyblue','salmon','green'])
plt.title('Distribution of married column')
plt.xlabel('married?')
plt.ylabel('Count')
plt.show()