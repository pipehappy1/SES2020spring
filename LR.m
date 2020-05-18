clear all;
%标准化数据集
data=importdata('breast.mat');
[di,dj]=size(data);
for i=1:dj-1
   data(:,i+1)=data(:,i+1)./max(data(:,i+1)); 
end
%选取样本
for i=(di-199):di
    test(i-di+200,:)=data(i,:);
end
for i=1:dj-1
    Test(:,i)=test(:,i+1);
end
learn_num=30;
for num=1:4
   number=learn_num*num; 
for Ran=1:100
y=rand(1, di-200);
[ignore,p] = sort(y);
for i=1:number
    x_0(i,:)=data(p(i),:);
end
for i=1:dj-1
    x(:,i)=x_0(:,i+1);
end
%训练算法开始
k=1;
w=1.+zeros(dj-1,1);
w0=0;
while(k<=50)
    p=exp(w0+x*w);
    P=p./(1+p);
    for i=1:dj-1
        w(i)=w(i)+k^-1*sum(x(:,i).*(x_0(:,1)-P));
    end
    w0=w0+k^-1*sum(x_0(:,1)-P);
    k=k+1;
end    
%测试
error=0;
for i=1:200
    p_test=exp(Test(i,:)*w+w0);
    if(p_test/(1+p_test)<0.5&test(i,1)==1)
        error=error+1;
    end
    if(p_test/(1+p_test)>=0.5&test(i,1)==0)
        error=error+1;
    end
end
lev(Ran)=(200-error)/200;
end
w'
level(num)=mean(lev);
clear x x_0 w w0;
end
level