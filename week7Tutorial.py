 # Import necessary modules 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris 
import numpy as np 
import matplotlib.pyplot as plt


# load the dataset
irisData = load_iris() 
# Create feature and target arrays 
X = irisData.data # features
y = irisData.target # labels
print(irisData)

# Split into training and test set; training_set=80%, testing_set=20% 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)


neighbors = np.arange(1, 9) # Checking for K=1,2,3,4,5,6,7,8,9
train_accuracy = np.empty(len(neighbors)) # To store the model trainig accuracy for different value of K
test_accuracy = np.empty(len(neighbors))  # To store the model testing accuracy for different value of K


# Loop over the K values 
for i, k in enumerate(neighbors): 
    knn = KNeighborsClassifier(n_neighbors=k) 
    knn.fit(X_train, y_train)     
    # Compute training and test data accuracy and store it in the previously defined arrays
    train_accuracy[i] = knn.score(X_train, y_train) 
    test_accuracy[i] = knn.score(X_test, y_test)
    
# Generate plot 
plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy') 
plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy') 
plt.legend() 
plt.xlabel('n_neighbors') 
plt.ylabel('Accuracy') 
plt.show()
