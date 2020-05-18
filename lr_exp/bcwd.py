# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.linear_model import LogisticRegression

# 导入数据集
data_set = datasets.load_breast_cancer()
X=data_set.data
y=data_set.target

# 输出数据集的几个要素
print ('Data fields data set:')
print (data_set.feature_names)

# 输出分类
print ('\nClassification outcomes:')
print (data_set.target_names)

# 划分训练集和测试集
X_train,X_test,y_train,y_test=train_test_split(
        X,y,test_size=0.25, random_state=0)

# 初始化一个归一化的标量
sc=StandardScaler() 
sc.fit(X_train)

# 对输入进行归一化
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)


# 用sklearn的logistic regression
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(C=100,random_state=0)
lr.fit(X_train_std,y_train)

# 预测
y_pred=lr.predict(X_test_std)

# 计算准确率
correct = (y_test == y_pred).sum()
incorrect = (y_test != y_pred).sum()
accuracy = correct / (correct + incorrect) * 100

print('\nPercent Accuracy: %0.1f' %accuracy)


# 预测的结果
prediction = pd.DataFrame()
prediction['actual'] = data_set.target_names[y_test]
prediction['predicted'] = data_set.target_names[y_pred]
prediction['correct'] = prediction['actual'] == prediction['predicted']

print ('\nDetailed results for first 20 tests:')
print (prediction.head(20))