from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score as f1
from sklearn.metrics import recall_score as recall
from sklearn.metrics import confusion_matrix as cm

'''导入数据'''
X,y = datasets.load_breast_cancer(return_X_y=True)

'''分割训练集与验证集'''
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.7,test_size=0.3)

'''初始化逻辑回归分类器，这里对类别不平衡问题做了处理'''
cl = LogisticRegression(class_weight='balanced')

'''利用训练数据进行逻辑回归分类器的训练'''
cl = cl.fit(X_train,y_train)

'''打印训练的模型在验证集上的正确率'''
print('逻辑回归的测试准确率：'+str(cl.score(X_test,y_test))+'\n')

'''打印f1得分'''
print('F1得分：'+str(f1(y_test,cl.predict(X_test)))+'\n')

'''打印召回得分'''
print('召回得分（越接近1越好）：'+str(recall(y_test,cl.predict(X_test)))+'\n')

'''打印混淆矩阵'''
print('混淆矩阵：'+'\n'+str(cm(y_test,cl.predict(X_test)))+'\n')