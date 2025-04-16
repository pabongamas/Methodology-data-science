 #Load the Credit dataset and perform the train-test data split as follows.
 # Load the dataset
import pandas as pd
# compare algorithms
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv('credit.csv',index_col=0)
data.index.name = "Obs"

# Split-out validation dataset
y=data["Limit"]
# print(y)
x=data.drop("Limit",axis=1)
# print(x)




# print(X_train)

# print("-----------------")
# print(X_validation)

le = LabelEncoder()

data['Student']=le.fit_transform(data["Student"])
data['Gender']=le.fit_transform(data["Gender"])
data['Married']=le.fit_transform(data["Married"])
data['Ethnicity']=le.fit_transform(data["Ethnicity"])



X_train, X_validation, Y_train, Y_validation = train_test_split(x, y, test_size=0.20, random_state=1, shuffle=True)
# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))


print(data)

knn=KNeighborsClassifier()
knn.fit(X_train,Y_train)
# prediction=knn.predict(X_validation)


# print(prediction)