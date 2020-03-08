clear
m=5;
r=0;
e=0.001;
Px=2*rand(1,m)-1;
Py=2*rand(1,m)-1;
U(2,m)=0;
Dijx=0;
Dijy=0;
while abs((4-m*pi*r*r)/4)>0.1
for i=1:m
    for j=1:m
        if i~=j
        dijx=(Px(i)-Px(j))/abs(Px(i)-Px(j))*max(2*r-sqrt((Px(i)-Px(j))^2+(Py(i)-Py(j))^2),0);
        dijy=(Py(i)-Py(j))/abs(Py(i)-Py(j))*max(2*r-sqrt((Px(i)-Px(j))^2+(Py(i)-Py(j))^2),0);
        Dijx=Dijx+dijx;%各圆形之间的弹性势能
        Dijy=Dijy+dijy;
        end
    end
    X_dijboundary=-max(Px(i)+r-1,0)+max(-(Px(i)-r+1),0);
    Y_dijboundary=-max(Py(i)+r-1,0)+max(-(Py(i)-r+1),0);
    %上述为某圆形对边界的弹性势能
    U(1,i)=Dijx+X_dijboundary;%弹性势能，包括各圆形之间和边界之间
    U(2,i)=Dijy+Y_dijboundary;
end
if U<0.0001
    r=r+0.00001;
end
for i=1:m
    Px(i)=Px(i)+e*U(1,i);
    Py(i)=Py(i)+e*U(2,i);
end
end
theta=0.01:0.01:2*pi;
for i=1:m
    plot(Px(i)+r*sin(theta),Py(i)+r*cos(theta),'Linewidth',1);
    hold on;
end
A=[1,1,-1,-1,1;1,-1,-1,1,1];
plot(A(1,:),A(2,:))
