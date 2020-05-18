#another way to insert data of breast cancer
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
#show the data's format, so that we can deal with data
#print(cancer.data.shape)
#print(cancer.target.shape)
#show details of data
#print(cancer.DESCR)
#malignant = 0, benign = 1 if you wish, use print(cancer.target)
#split the train and test dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.25, random_state=42)
# train_data：所要划分的样本特征集
# train_target：所要划分的样本结果 此处为Benign or malignant
# test_size：样本占比，如果是整数的话就是样本的数量
# random_state：是随机数的种子。随机抽取，random_state 保证每次数据可以重复。
# 随机数种子：其实就是该组随机数的编号，在需要重复试验的时候，保证得到一组一样的随机数。比如你每次都填1，其他参数一样的情况下你得到的随机数组是一样的。但填0或不填，每次都会不一样。
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
pred = log_reg.predict(X_test)
acc_score = log_reg.score(X_test, y_test)
print(acc_score)
list(cancer.target_names)
import pandas as pd
d = {'predictions': pred, 'real values': y_test}
data = pd.DataFrame(data=d)
print(data)
data.predictions == data['real values']
wrong_predictions= []
for i in range(0,143):
    if data.predictions[i] != data['real values'][i]:
        wrong_predictions.append(data.predictions[i])
        print("wrongly diagnosed patient number:", i, 'as', wrong_predictions[-1])
    i=i+1
