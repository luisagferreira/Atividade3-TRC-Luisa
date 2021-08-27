### DADOS DO EXEMPLO 5.11 (pág. 569 incropera) ###


q1=1*10^(7);
q2=2*10^(7);
alfa=5*10^(-6);
L=0.01;
k=30;
Tinf=250;
h=1100;
deltax=0.002; #m

## CALCULANDO O VALOR DO Bi ##

Bi=(h*deltax)/k;

## CRITÉRIO DE ESTABILIDADE ##

F0 =(1/2)/(1+Bi);

deltat=0.3;
#deltat=((F0*(deltax)^2)/alfa)
#fprintf(deltat)

T5=Tinf+(((10^(7))*0.01)/h);

### CALCULANDO AS TEMPERATURAS INICIAIS ###

for i=1:6
    x=(i-1)*deltax;
    T(i,1)=q1*L^2/(2*k)*(1-x^2/(L^2))+T5;
  
end

### REGISTRANDO AS TEMPERATURAS NODAIS ###

p=1;
t=0;
tfinal=1.5;

while t<tfinal
    p=p+1;
    t=0.3*(p-1);

for i=1:6
    x=(i-1)*deltax;
      if i==1
        T(i,p) =F0*(2*T(i+1,p-1)+q2*deltax^2/k)+(1-2*F0)*T(i,p-1);

    elseif i==6
        T(i, p) = 2*F0*(T(i - 1, p - 1) + Bi*Tinf+ q2 * deltax^2 /(2*k))+(1 - 2 * F0-2*Bi*F0)*T(i, p - 1);

      else
        T(i, p) = F0*(T(i - 1, p - 1) +T(i + 1, p - 1)+ q2 * deltax^2 / k) + (1 - 2 * F0)*T(i, p - 1);
    end
end
end


T_i=T';

Time=(0:deltat:tfinal);
disp("       Tempo     Nó 1     Nó 2      Nó 3      Nó 4       Nó 5        Nó 6\n")

tab=[Time',T'];
disp(tab)
        
        
        
        
        