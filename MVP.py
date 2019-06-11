
# coding: utf-8

# In[5]:


import numpy as np
pk=float(input('산의 pKa를 입력해주세요'))
k=10**((-1)*(pk))
c=float(input('산의 농도를 입력해주세요(M)'))
v=float(input('산의 부피를 입력해주세요(mL)'))
cNaOH= float(input('NaOH의 농도를 입력해주세요(M)'))
vNaOH=float(input('NaOH의 부피를 입력해주세요(mL)'))
a=(k/c)**0.5

def dang(x, cNaOH, c, v, k):
    answer = 14 + 0.5* np.log10((10**(-14))*(c*v/(v+x))/k)
    return answer 
a=c*v/cNaOH
print(dang(a, cNaOH, c, v, k)) 

