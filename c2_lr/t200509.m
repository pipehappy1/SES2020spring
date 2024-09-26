clear
clc
filename='C:\Users\12510\Desktop\data.csv';
%二分类 由癌症数据中取出两列。 共560个数据  每个数据2个特征
%data=1*rand(560,2);
Bcancer=csvread(filename,1,2,[1,2,560,11]);
Bcancer_sample(:,1)=Bcancer(:,1); %在这里选择要分析哪两个维度
Bcancer_sample(:,2)=Bcancer(:,2);
%归一化
data=mapminmax(Bcancer_sample',0,1);
data=data';

label=zeros(560,1);
label((data(:,2)+data(:,1)>1))=1;
%在data上加常数特征项；
data=[data,ones(size(data,1),1)];
%打乱循序
randIndex = randperm(size(data,1));
data_new=data(randIndex,:);
label_new=label(randIndex,:);

%70%训练  30%测试
k=0.7*size(data,1);
X1=data_new(1:k,:);
Y1=label_new(1:k,:);
X2=data_new(k+1:end,:);
Y2=label_new(k+1:end,:);

[m1,n1] = size(X1);
[m2,n2] = size(X2);
Features=size(data,2); %特征个数

% 开始训练
%设定学习率为0.01
delta=1;  
lamda=-1.8; %正则项系数

theta1=rand(1,Features); 
%theta1=[.5,.5];

%梯度下降算法求解theta
num = 560; %最大迭代次数
L=[];
while(num)
    dt=zeros(1,Features);
    loss=0;
    for i=1:m1
        xx=X1(i,1:Features);
        yy=Y1(i,1);
        h=1/(1+exp(-(theta1 * xx')));
        dt=dt+(h-yy) * xx;
        loss=loss+ yy*log(h)+(1-yy)*log(1-h);%损失函数
    end
    loss=-loss/m1;
    L=[L,loss];
    
    theta2=theta1 - delta*dt/m1 - lamda*theta1/m1;%梯度下降与正则化
    theta1=theta2;
    num = num - 1;
    
    if loss<0.01
        break;
    end
end
figure
subplot(1,2,1)
plot(L)
title('loss')

subplot(1,2,2)
x=0:0.1:10;
y=(-theta1(1)*x-theta1(3))/theta1(2);
plot(x,y,'linewidth',2)
hold on
plot(data(label==1,1),data(label==1,2),'ro')
hold on
plot(data(label==0,1),data(label==0,2),'go')
axis([0 1 0 1])


% 测试数据
acc=0;
for i=1:m2
    xx=X2(i,1:Features)';
    yy=Y2(i);
    finil=1/(1+exp(-theta2 * xx));
    if finil>0.5 && yy==1
        acc=acc+1;
    end
    if finil<=0.5 && yy==0
        acc=acc+1;
    end
end
acc/m2  %准确率，这个数据集中，健康数据有明显的聚集中心，而不健康数据则往各个方向发散
        %所以准确率不是很高，大概在92%附近
        %还有这么高的原因是大部分数据是健康的，如果健康不健康数据比例变小，那么误差会变大。
        %如果用多维度的分类，效果可能会好一些
