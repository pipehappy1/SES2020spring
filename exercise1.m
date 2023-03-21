clear 
clc
% 预先对数据表进行处理，去除第一行，把M表示为1，B表示为0
M=csvread('datanew.csv',0,1);%从数据表的第1行第2列开始读取数据到矩阵M
%归一化
M=mapminmax(M',0,1);
M=M';
X=M(:,2:31);
Y=M(:,1);
%将数据集分为训练集X1,Y1（前500行）和测试集X2,Y2（后69行）
X1=X(1:500,:);
Y1=Y(1:500,:);
X2=X(501:569,:);
Y2=Y(501:569,:);
[m1,n1]=size(X1);
[m2,n2]=size(X2);
m=size(X1,2);
delta=0.01;%学习率
theta1=rand(m,1);
%训练模型
num=100;%迭代次数
while(num)
    dt=zeros(m,1);
    for i=1:m1
        xx=X1(i,1:m)';
        yy=Y1(i,1);
        h=1/(1+exp(-(theta1' * xx)));
        dt=dt+(yy-h) * xx;
    end
    theta2=theta1-1/m1*delta*dt;
    theta1=theta2;
    num=num-1;
end
%测试数据
cc=1;
for i=1:m2
    xx=X2(i,1:m)';
    yy=Y2(i);
    ans=1/(1+exp(-theta2' * xx));
    if ans>0.5 && yy==1
        cc=cc+1;
    end
    if ans<=0.5 && yy==0
        cc=cc+1;
    end
end
cc/m2


%最终得到测试结果：准确率为：0.7681