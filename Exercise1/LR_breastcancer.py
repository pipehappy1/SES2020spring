from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,SGDRegressor,Ridge,LogisticRegression
from sklearn.metrics import mean_squared_error, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

def logistic():
    """
    逻辑回归做二分类进行乳腺癌预测，用数据集的0.7作为训练集，用数据集的0.3作为测试集。Pytorch进行二分类要分每个维度分别进行，这里有sklearn内置逻辑回归函数对数据进行分类。首先读取在线数据集，然后进行数据分割，按0.7/0.3分割为训练集和测试集。
    """
    # 构造列标签名字
    column = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape',
              'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli',
              'Mitoses', 'Class']
    # 读取在线数据集
    data = pd.read_csv(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
        names=column)
    # print(data)
    # 对存在缺失值进行处理，替换为nan
    data = data.replace(to_replace='?', value=np.nan)
    data = data.dropna()
    # 输出data的数据量和维度。
    print(data.shape)
    print(data)
    # 进行数据的分割
    x_train, x_test, y_train, y_test = train_test_split(data[column[1:10]], data[column[10]], test_size=0.3)
    # 输出训练样本的数量和类别分布。
    print(y_train.value_counts())
    # 输出测试样本的数量和类别分布。
    print(y_test.value_counts())
    # 进行标准化处理
    std = StandardScaler()
    x_train = std.fit_transform(x_train)
    x_test = std.transform(x_test)
    # 逻辑回归来对训练集求系数
    lg = LogisticRegression(C=1.0)
    # 求得训练集X的均值、方差、最大值、最小值等固有属性
    lg.fit(x_train, y_train)
    print('回归系数\n', lg.coef_)
    # 训练后返回预测结果
    y_predict = lg.predict(x_test)
    # 输出预测结果计算出的决定系数R^2
    print("拟合优度：", lg.score(x_test, y_test))
    # classification_report函数用于显示主要分类指标．显示每个类的精确度，召回率，F1值等
    print("分类指标：", classification_report(y_test, y_predict, labels=[2, 4], target_names=["良性", "恶性"]))

if __name__ == "__main__":
        logistic()