
# coding: utf-8

# In[5]:

#강산의 적정곡선과 약산의 적정곡선도 그려 비교(강산의 그래프 그리는 방법과 동일)
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
def dang(x, cNaOH, c, v, k):
    answer = 14 + 0.5* np.log10((10**(-14))*(c*v/(v+x))/k)
    return answer
def first(cNaOH, c, v, k):
    answer = (-0.5)*np.log10(c*k)
    return answer
def strongacid(x, cNaOH, c, v):
    acidmmol=c*v
    k=[]
    for i in range(len(x)):
        if acidmmol>cNaOH*x[i]:
            answer=(-1)*np.log10((c*v-cNaOH*x[i])/(x[i]+v))
            k.append(answer)
        elif acidmmol < cNaOH*x[i]:
            answer=(-1)*np.log10((-c*v+cNaOH*x[i])/(x[i]+v))
            real=14-answer
            k.append(real)
        else:
            k.append(7)
    return k
     
#파란색은 약산의 적정곡선, 빨간색은 강산의 적정곡선인 그래프를 한 번에 그림
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
x1= np.arange(0, vNaOH, 0.001).tolist()
y1= pH(x1, cNaOH, c, v, k)
x2= np.arange(0, vNaOH, 0.001).tolist()
y2= strongacid(x2, cNaOH, c, v)
plt.plot(x1,y1,x2,y2, 'r-')
plt.show()
a=c*v/cNaOH
b= dang(a, cNaOH, c, v, k)
c= first(cNaOH, c, v, k)
print('붉은색 그래프는 같은 농도, 부피인 강산의 적정곡선입니다. 약산과 비교해보세요^^')
print(int(a), 'mL를 넣었을 때 당량점 입니다. 이때 pH는',float(b), '입니다.')
print('약산의 초기 pH는', float(c),'입니다')
if k<10**(-6):
    print('약산의 Ka 값이 작아서 지시약 적정에 사용할 수 없습니다. 다른 산을 골라주세요^^')

