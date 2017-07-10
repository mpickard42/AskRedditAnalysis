# import sys
# print sys.path 
# import sklearn 
# print sklearn
from sklearn import tree
from sklearn.cross_validation import train_test_split
import numpy as np
import pandas as pd

def train(clf, features, labels):
    return clf.fit(features, labels)

def predict(clf, features):
    return clf.predict(features)

input_file = "AskRedditData.csv"

df = pd.read_csv(input_file, header=0)

original_headers = list(df.columns.values)
original_headers = original_headers[1:]
print original_headers
df = df._get_numeric_data()
# print df
numeric_headers = list(df.columns.values)
numeric_headers = numeric_headers[1:]
# print numeric_headers
numpy_array = df.as_matrix()
print numpy_array
X = numpy_array[:, 1:3]
print X
y = numpy_array[:, 0]
print y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25)

my_classifier = tree.DecisionTreeClassifier()

my_classifier = train(my_classifier, X_train, y_train)
predictions = predict(my_classifier, X_test)

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)

from sklearn.externals.six import StringIO
import pydot as pydot
  
import os
os.path 
os.pathsep
os.environ["PATH"] += os.pathsep + '/Users/marjoriepickard/anaconda2/pkgs/graphviz-2.38.0-4/bin'
  
target_names = ['low', 'mid', 'high']
  
dot_data = StringIO()
tree.export_graphviz(my_classifier, out_file=dot_data, feature_names=original_headers, class_names=target_names, filled=True, rounded=True, impurity=False)
  
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("testPDF.pdf")
