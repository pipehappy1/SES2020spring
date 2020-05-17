clear
clc
filename='C:\Users\12510\Desktop\data.csv';
%������ �ɰ�֢������ȡ�����С� ��560������  ÿ������2������
%data=1*rand(560,2);
Bcancer=csvread(filename,1,2,[1,2,560,11]);
Bcancer_sample(:,1)=Bcancer(:,1); %������ѡ��Ҫ����������ά��
Bcancer_sample(:,2)=Bcancer(:,2);
%��һ��
data=mapminmax(Bcancer_sample',0,1);
data=data';

label=zeros(560,1);
label((data(:,2)+data(:,1)>1))=1;
%��data�ϼӳ��������
data=[data,ones(size(data,1),1)];
%����ѭ��
randIndex = randperm(size(data,1));
data_new=data(randIndex,:);
label_new=label(randIndex,:);

%70%ѵ��  30%����
k=0.7*size(data,1);
X1=data_new(1:k,:);
Y1=label_new(1:k,:);
X2=data_new(k+1:end,:);
Y2=label_new(k+1:end,:);

[m1,n1] = size(X1);
[m2,n2] = size(X2);
Features=size(data,2); %��������

% ��ʼѵ��
%�趨ѧϰ��Ϊ0.01
delta=1;  
lamda=-1.8; %������ϵ��

theta1=rand(1,Features); 
%theta1=[.5,.5];

%�ݶ��½��㷨���theta
num = 560; %����������
L=[];
while(num)
    dt=zeros(1,Features);
    loss=0;
    for i=1:m1
        xx=X1(i,1:Features);
        yy=Y1(i,1);
        h=1/(1+exp(-(theta1 * xx')));
        dt=dt+(h-yy) * xx;
        loss=loss+ yy*log(h)+(1-yy)*log(1-h);%��ʧ����
    end
    loss=-loss/m1;
    L=[L,loss];
    
    theta2=theta1 - delta*dt/m1 - lamda*theta1/m1;%�ݶ��½�������
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


% ��������
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
acc/m2  %׼ȷ�ʣ�������ݼ��У��������������Եľۼ����ģ�������������������������ɢ
        %����׼ȷ�ʲ��Ǻܸߣ������92%����
        %������ô�ߵ�ԭ���Ǵ󲿷������ǽ����ģ�����������������ݱ�����С����ô������
        %����ö�ά�ȵķ��࣬Ч�����ܻ��һЩ
