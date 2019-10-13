# 필요한 라이브러리 불러오기
import numpy as np
import sys
import matplotlib.pyplot as plt 
%matplotlib inline

def acid_pH(x, cNaOH, c, v, k):
    acidmmol = c * v
    l = [] # 적정에 따른 pH를 저장할 List
    for i in range(len(x)):
        if x[i] == 0 :
            answer = round((-0.5) * np.log10(c * k), 2) # 약산 근사법 사용 ([H+]^2 = c * k 이므로 0.5를 곱한다.)
            l.append(answer)
        elif acidmmol > x[i] * cNaOH:
            basemmol = cNaOH * x[i]
            answer = round(pk + np.log10(basemmol / (acidmmol - basemmol)), 2) # pH 계산 위해 Henderson 식 사용
            l.append(answer)
        elif acidmmol == x[i] * cNaOH:
            answer = round(14 + 0.5 * np.log10((10 ** (-14)) * (c * v / (v + x[i])) / k), 2) # 당량점에서 : 염의 가수분해 고려!
            l.append(answer)
        else :  # 당량점 이후
            otherNaOH = cNaOH * x[i] - c * v
            answer = round(14 + np.log10(otherNaOH / (v + x[i])), 2)
            l.append(answer)
    return l

def bases_pH(x, cHCl, c, v, kb, ka):
    basemmol = c * v
    l = [] #적정에 따른 pH를 저장할 List
    for i in range(len(x)):
        if x[i] == 0 :
            answer = 14 - (-0.5) * np.log10(c * kb) #약산 근사법 사용 
            l.append(answer)
        elif basemmol > x[i] * cHCl:
            acidmmol = cHCl * x[i]
            answer = (14 - pk) + np.log10((basemmol - acidmmol) / acidmmol) #pH 계산 위해 Henderson 식 사용
            l.append(answer)
        elif acidmmol == x[i] * cHCl:
            answer = 0.5 * np.log10(ka * (c * v / (v + x[i]))) #당량점에서 : 염의 가수분해 고려!
            l.append(answer)
        else :
            otherHCl = cHCl * x[i] - c * v
            answer = -np.log10(otherHCl / (v + x[i]))
            l.append(answer)
    return l # pH 값들을 담은 배열을 반환

def acid_dang(x, cNaOH, c, v, k):
    answer = round(14 + 0.5 * np.log10((10 ** (-14)) * (c * v / (v + x)) / k), 2)
    return answer

def bases_dang(x, cHCl, c, v, ka):
    answer = 14 + 0.5 * np.log10(ka * (c * v / (v + x)))
    return answer

#적정의 종류 입력받기
t = int(input('2가지 적정 종류 중 선택해 주세요.\n 1) 약산을 강염기로 적정   2) 약염기를 강산으로 적정 \n숫자로 입력해 주세요 : \n'))
if t == 1:
    print('약산 강염기 적정을 시작합니다.')
    pk = float(input('① 약산의 pKa를 입력해주세요 : '))
    k = 10 ** ((-1) * (pk))

    if k < 10 ** (- 6):
        print('약산의 Ka 값이 작아서 지시약 적정에 사용할 수 없습니다. 다른 산을 골라주세요.')
        sys.exit(1)
    c = float(input('② 약산의 농도를 입력해주세요(M) : '))
    v = float(input('③ 약산의 부피를 입력해주세요(mL) : '))
    cNaOH = float(input('④ NaOH의 농도를 입력해주세요(M) : '))
    vNaOH = float(input('⑤ NaOH의 부피를 입력해주세요(mL) : '))
    a = (k / c) ** 0.5
        
    x1 = np.arange(0, vNaOH, 0.001).tolist()
    y1 = acid_pH(x1, cNaOH, c, v, k)

    plt.plot(x1,y1, 'r-')
    plt.show()
    a = c * v / cNaOH #당량점까지의 첨가해야할 약산 부피
    b = acid_dang(a, cNaOH, c, v, k) #당량점의 pH 저장
    print(int(a), 'mL를 넣었을 때 당량점 입니다. 이때 pH는', float(b), '입니다.')
    print('약산의 초기 pH는', y1[0],'입니다.')

else: # t == 2
    print('약염기 강산 적정을 시작합니다.')
    pk = float(input('① 약염기의 pKb를 입력해주세요 : '))
    kb = 10 ** ((-1) * (pk))
    ka = 10 ** (-14) / kb

    if kb<10**(-6):
        print('약염기의 Kb 값이 너무 커서 지시약 적정에 사용할 수 없습니다. 다른 염기를 골라주세요.')
        sys.exit(1)

    c = float(input('② 염기의 농도를 입력해주세요(M) : '))
    v = float(input('③ 염기의 부피를 입력해주세요(mL) : '))
    cHCl = float(input('④ HCl 의 농도를 입력해주세요(M) : '))
    vHCl = float(input('⑤ HCl 의 부피를 입력해주세요(mL) : '))
    a = (k / c) ** 0.5
        
    x1 = np.arange(0, vHCl, 0.001).tolist()
    y1 = bases_pH(x1, cHCl, c, v, kb, ka)

    plt.plot(x1, y1, 'r-')
    plt.show()

    a = c * v / cHCl #당량점까지의 첨가해야할 약산 부피
    b = bases_dang(a, cHCl, c, v, ka) #당량점|의 pH 저장
    print('HCl', round(a, 1), 'mL를 넣었을 때 당량점 입니다. 이때 pH는', round(b, 2), '입니다.')
    print('약염기의 초기 pH는', y1[0],'입니다.')
