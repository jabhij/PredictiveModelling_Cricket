"""
    Labels : Lost, Draw, Won [-1,0,1]
    
    Features -
    ==========
        Toss(Lost,Won) = [-1,1]
        Bat(First, Second) = [-1,1]
"""

# Import SVC
from sklearn.svm import SVC

# Import Numpy 
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support as score

# Assigning Features
features = np.genfromtxt('Trained_Data.csv',delimiter=',',usecols=(1,2),dtype=int)
labels = np.genfromtxt('Trained_Data.csv',delimiter=',',usecols=(0),dtype=int)

features_test = np.genfromtxt('Test.csv',delimiter=',',usecols=(1,2),dtype=int)
labels_test = np.genfromtxt('Test.csv',delimiter=',',usecols=(0),dtype=int)

# Create a SVM Classifier
model = SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
            decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
            max_iter=-1, probability=True, random_state=None, shrinking=True,
            tol=0.001, verbose=False
            )

# Train the model using the training sets
model.fit(features, labels)
# print(model.get_params())

# Prediction
predicted = model.predict(features_test)
print(predicted)

acc = accuracy_score(labels_test,predicted)
print(acc)
