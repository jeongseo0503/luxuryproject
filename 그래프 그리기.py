import numpy as np

pk=float(input('산의 pKa를 입력해주세요'))
k=10**((-1)*(pk))
c=float(input('산의 농도를 입력해주세요(M)'))
v=float(input('산의 부피를 입력해주세요(mL)'))
cNaOH= float(input('NaOH의 농도를 입력해주세요(M)'))
vNaOH=float(input('NaOH의 부피를 입력해주세요(mL)'))
a=(k/c)**0.5

def pH(x, cNaOH, c, v, k):
    acidmmol=c*v
    l=[]
    for i in range(len(x)):
        if x[i]==0 :
            answer = (-0.5)*np.log10(c*k)
            l.append(answer)
        elif acidmmol>x[i]*cNaOH:
            basemmol = cNaOH * x[i]
            answer = pk + np.log10(basemmol/(acidmmol - basemmol))
            l.append(answer)
        elif acidmmol==x[i]*cNaOH:
            answer = 14 + 0.5* np.log10((10**(-14))*(c*v/(v+x[i]))/k)
            l.append(answer)
        else :
            otherNaOH = cNaOH*x[i]-c*v
            answer = 14+ np.log10(otherNaOH/(v+x[i]))
            l.append(answer)
    return l

import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
x1= np.arange(0, vNaOH, 0.001).tolist()
y1= pH(x1, cNaOH, c, v, k)
plt.plot(x1,y1)
plt.show()

a=c*v/cNaOH
b=lambda(c,v,k:14 + 0.5* np.log10((10**(-14))*(c*v/(v+x))/k))
print(int(a), 'mL를 넣었을 때 당량점 입니다. 이때 pH는',float(b), '입니다.')
