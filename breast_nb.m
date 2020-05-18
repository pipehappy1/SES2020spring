clear all;
%标准化数据集
data=importdata('breast.mat');
[di,dj]=size(data);
learn_num=30;%采样的基数
for num=1:4
   number=learn_num*num;
for Ran=1:100 %随即选取number个样本100次
y=rand(1, di-200);
[ignore,p] = sort(y);
for i=1:number
    x_0(i,:)=data(p(i),:);%随即选择了number个样本
end
index_1=find(x_0(:,1)==1);
len_1=length(index_1);%计算其中属于第一类的编号和数量
index_2=find(x_0(:,1)==2);
len_2=length(index_2);%计算其中属于第二类的标号和数量
for i=1:len_1
    x_1(i,:)=x_0(index_1(i),:);%第一类归到x_1中
end
for i=1:len_2
    x_2(i,:)=x_0(index_2(i),:);%第二类归到x_2中
end
clear x_0 index_1 index_2;
for i=(di-199):di
    test(i-di+200,:)=data(i,:);%选取最后100个作为测试样本
end
%训练开始        
for i=2:dj
    [x1,y1]=sort(x_1(:,i));
    k=x1(1);
    z_1(1,1)=x1(1);
    z_1(2,1)=1;
    j=1;
    for I=2:len_1
        if(x1(I)==k)
            z_1(2,j)=z_1(2,j)+1;
        end
        if(x1(I)~=k)
            k=x1(I);
            j=j+1;
            z_1(1,j)=k;
            z_1(2,j)=1;
        end
    end 
    [n,step_1]=size(z_1);
    [x2,y2]=sort(x_2(:,i));
    k=x2(1);
    z_2(1,1)=x2(1);
    z_2(2,1)=1;
    j=1;
    for I=2:len_2
        if(x2(I)==k)
            z_2(2,j)=z_2(2,j)+1;
        end
        if(x2(I)~=k)
            k=x2(I);
            j=j+1;
            z_2(1,j)=k;
            z_2(2,j)=1;
        end
    end
    [n,step_2]=size(z_2); 
  %对该特征的测试样本的概率  
    for t=1:200
        for j=1:step_1
            dis1(j)=abs(test(t,i)-z_1(1,j));
        end
        dis_1=find(dis1==min(dis1));
        P_1(t,i-1)=z_1(2,dis_1(1))/len_1;
        for j=1:step_2
            dis2(j)=abs(test(t,i)-z_2(1,j));
        end
        dis_2=find(dis2==min(dis2));
        P_2(t,i-1)=z_2(2,dis_2(1))/len_2;
    end
    clear x1 x2 y1 y2 z_1 z_2 dis1 dis2 dis_1 dis_2;
end
clear x_1 x_2;
error=0;               
for s=1:200
    P1=1;
    P2=1;
    for j=1:dj-1
        P1=P1*P_1(s,j);
    end
    P1=P1*len_1/number;
    for j=1:dj-1
        P2=P2*P_2(s,j);
    end
    P2=P2*len_2/number;
    if(P1>P2&test(s,1)==2)
        error=error+1;
    end
    if(P1<P2&test(s,1)==1)
        error=error+1;
    end
end
lev(Ran)=(200-error)/200;
end
level(num)=mean(lev)
end