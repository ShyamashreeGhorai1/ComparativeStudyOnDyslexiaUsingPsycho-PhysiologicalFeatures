# -*- coding: utf-8 -*-
"""AdaBoost(Mutual_Information_Gain).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DT0sCTU_wK-J99SAu2GbQAUzAb_WpoKN

**Importing Data**
"""

import io
import pandas as pd
from google.colab import files

uploaded = files.upload()

df = pd.read_excel(io.BytesIO(uploaded.get('data analysis.xlsx')))

import numpy as np
pd.pandas.set_option('Display.max_columns',None)
pd.pandas.set_option('Display.max_rows',None)

"""**Data Cleaning**"""

df.isnull().sum()

df.duplicated().sum()

# There is no missing and duplicate value in the dataset.

"""**Data Preparation**"""

df = df.drop('Gender',axis=1)

df = df.drop('Age',axis=1)

import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, f1_score, recall_score,roc_auc_score
from sklearn import metrics
from sklearn.ensemble import AdaBoostClassifier

label_encoder = preprocessing.LabelEncoder()
df['Nativelang']= label_encoder.fit_transform(df['Nativelang'])
df['Otherlang']= label_encoder.fit_transform(df['Otherlang'])
df['Dyslexia']= label_encoder.fit_transform(df['Dyslexia'])

df

df.shape

df.describe()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df.drop(labels=['Dyslexia'],axis=1),df['Dyslexia'],
                                                                                        test_size=0.2,random_state=0)

"""**Feature Selection**"""

from sklearn.feature_selection import mutual_info_classif
# determine the mutual information
mutual_info = mutual_info_classif(x_train, y_train)
mutual_info

mutual_info = pd.Series(mutual_info)
mutual_info.index = x_train.columns
mutual_info.sort_values(ascending=False)

#let's plot the ordered mutual_info values per feature
mutual_info.sort_values(ascending=False).plot.bar(figsize=(15, 5))

from sklearn.feature_selection import SelectKBest
# Now we Will select the  top 100 important features
sel_cols = SelectKBest(mutual_info_classif, k=100)
sel_cols.fit(x_train, y_train)
x_train.columns[sel_cols.get_support()]

"""**Model**"""

classifier = AdaBoostClassifier()
classifier.fit(x_train, y_train)

pred = classifier.predict(x_test)
y_train_predict = classifier.predict(x_train)

print("Training Accuracy", accuracy_score(y_train, y_train_predict))
Accuracy = metrics.accuracy_score(y_test, pred)
print("Testing Accuracy",Accuracy)

from sklearn.metrics import classification_report
print(classification_report(y_test, pred))
pd.crosstab(y_test, pred)

"""**Model Evaluation**"""

from sklearn.metrics import classification_report
print(classification_report(y_test, pred))
pd.crosstab(y_test, pred)

confusion_matrix = metrics.confusion_matrix(y_test, pred)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

cm_display.plot()
plt.show()

Precision = metrics.precision_score(y_test, pred)
print(Precision)

Sensitivity_recall = metrics.recall_score(y_test, pred)
print(Sensitivity_recall)

Specificity = metrics.recall_score(y_test, pred, pos_label=0)
print(Specificity)

F1_score = metrics.f1_score(y_test, pred)
print(F1_score)

from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
ns_probs = [0 for _ in range(len(y_test))]
Ada_probs = classifier.predict_proba(x_test)
# keep probabilities for the positive outcome only
Ada_probs = Ada_probs[:, 1]
# calculate scores
ns_auc = roc_auc_score(y_test, ns_probs)
Ada_auc = roc_auc_score(y_test, Ada_probs)
# summarize scores
print('No Skill: ROC AUC=%.3f' % (ns_auc))
print('AdaBoost: ROC AUC=%.3f' % (Ada_auc))
# calculate roc curves
ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
Ada_fpr, Ada_tpr, _ = roc_curve(y_test, Ada_probs)
# plot the roc curve for the model
plt.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
plt.plot(Ada_fpr, Ada_tpr, marker='.', label='AdaBoost')
# axis labels
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
# show the legend
plt.legend()
# show the plot
plt.show()











classifier = AdaBoostClassifier(
    n_estimators = 2000,
    learning_rate = 0.3,
)
classifier.fit(x_train, y_train)

pred = classifier.predict(x_test)
y_train_predict = classifier.predict(x_train)

print("Training Accuracy", accuracy_score(y_train, y_train_predict))
Accuracy = metrics.accuracy_score(y_test, pred)
print("Testing Accuracy",Accuracy)





clf =AdaBoostClassifier(n_estimators=50,learning_rate=0.5)

model = clf.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

print(confusion_matrix(y_test,y_pred))