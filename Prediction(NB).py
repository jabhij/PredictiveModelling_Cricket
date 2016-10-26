"""
    Labels : Lost, Draw, Won [-1,0,1]

    Features --
    ==========
        Toss(Lost,Won) = [-1,1]
        Bat(First, Second) = [-1,1]
"""

# Import Library - Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Import Numpy
import numpy as np
from sklearn.metrics import precision_recall_fscore_support as score


# Assigning Features
features = np.genfromtxt('Trained_Data.csv',delimiter=',',usecols=(1,2),dtype=int)
labels = np.genfromtxt('Trained_Data.csv',delimiter=',',usecols=(0),dtype=int)

features_test = np.genfromtxt('Test.csv',delimiter=',',usecols=(1,2),dtype=int)
labels_test = np.genfromtxt('Test.csv',delimiter=',',usecols=(0),dtype=int)

# Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(features, labels)

# Prediction
predicted = model.predict(features_test)
# print(predicted)

acc = accuracy_score(labels_test,predicted)
print(acc)
