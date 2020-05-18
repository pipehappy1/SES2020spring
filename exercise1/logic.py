#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
def logistic():
    #加载数据集
    names = ['Sample code number',' Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape',
             'Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin',
             'Normal Nucleoli','Mitoses','Class']
    data = pd.read_csv('breast-cancer-wisconsin.data',names=names)

    #数据集预处理，缺失值删除
    data = data.replace(to_replace='?',value=np.nan)
    data = data.dropna()

    #进行数据的分割
    x_train,x_test,y_train,y_test = train_test_split(data.loc[:,'Sample code number':'Mitoses'],data.loc[:,'Class'],test_size=0.7)

    #特征值的标准化
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)

    #使用逻辑回归进行预测
    lr = LogisticRegression(C=1.0)
    lr.fit(x_train,y_train)
    print(lr.coef_)
    y_predict = lr.predict(x_test)

    #输出准确率
    print("accuracy：",lr.score(x_test,y_test))

    #输出召回率
    print(classification_report(y_test,y_predict,labels=[2,4],target_names=["benign","malignant"]))

    return None

if __name__ == "__main__":
    logistic()


# In[ ]:




