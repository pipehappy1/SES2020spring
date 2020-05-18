clear 
clc
% Ԥ�ȶ����ݱ���д���ȥ����һ�У���M��ʾΪ1��B��ʾΪ0
M=csvread('datanew.csv',0,1);%�����ݱ�ĵ�1�е�2�п�ʼ��ȡ���ݵ�����M
%��һ��
M=mapminmax(M',0,1);
M=M';
X=M(:,2:31);
Y=M(:,1);
%�����ݼ���Ϊѵ����X1,Y1��ǰ500�У��Ͳ��Լ�X2,Y2����69�У�
X1=X(1:500,:);
Y1=Y(1:500,:);
X2=X(501:569,:);
Y2=Y(501:569,:);
[m1,n1]=size(X1);
[m2,n2]=size(X2);
m=size(X1,2);
delta=0.01;%ѧϰ��
theta1=rand(m,1);
%ѵ��ģ��
num=100;%��������
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
%��������
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


%���յõ����Խ����׼ȷ��Ϊ��0.7681