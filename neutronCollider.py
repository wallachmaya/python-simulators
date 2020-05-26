import math
from scipy.constants import Planck, alpha, e, epsilon_0, speed_of_light, m_p, m_n, c
#for neutrons
def SEMF(Z, N):
    aV, aS, aC, aA, delta = 15.75, 17.8, 0.711, 23.7, 11.18
    Z, N = np.atleast_1d(Z), np.atleast_1d(N)
    A = Z + N
    sgn = np.zeros(Z.shape)
    if Z%2 ==0 and N%2 ==0:
        sgn=-1
    else:
        sgn = +1
    E = (aV - aS / A**(1/3) - aC * Z**2 / A**(4/3) -
         aA * (A-2*Z)**2/A**2 + sgn * delta/A**(3/2))
    if Z.shape[0] == 1:
        return float(E)
    return E

def sig_np(R,wav,e,V0):
    h = Planck/(2*math.pi)
    M = m_n
    k = ((2*M*e)**0.5)/h
    K = ((2*M*(e+V0))**0.5)/h
    sig2 = math.pi*((R+wav)**2)*((4*k*K)/((k+K)**2))
    C = 0.02
    a = 12
    eby = 300
    Q = eby - e
    w = C*math.exp(2*math.sqrt(a*(eby-e)))
    Fp = ((2*1.2)/h**2)*(((e+Q)*sig2*w*eby)-((e)*sig2*w*0))
    Fn = ((2*1)/h**2)*(((e)*sig2*w*eby)-((e+Q)*sig2*w*0))
    Fa = ((2*4)/h**2)*(((e+Q)*sig2*w*eby)-((e+Q)*sig2*w*0))
    sig = sig2*(Fp/(Fa+Fn+Fp))
    return sig,sig2

def sig_cap_av(R,l,e,V0):
    h = Planck/(2*math.pi)
    M = m_n
    k = ((2*M*e)**0.5)/h
    K = ((2*M*(e+V0))**0.5)/h
    x = k*R
    X = K*R
    vl = (x**(2*l))/(math.factorial(math.factorial(2*l - 1))**2)
    Di = 70
    rad = 0.17
    e1 = 50*((rad/Di)**2)
    sig = ((4*math.pi*(2*l + 1))/k*K)*(vl/(1+ ((e/e1)**0.5)*vl))
    return sig

def sig_n2n(R,e,V0):
    Sn = SEMF(A/2, A/2)
    ec = e - Sn
    a = 12
    temp = (e/a)**0.5
    n2n = math.pi*(R**2)*(1 - (1+(ec/temp))*math.exp(-(ec/temp)))
    return n2n


#secondary rea
def sec_re(crosss,N,Z,e,R,react):
    h = Planck/(2*math.pi)
    eby = 300
    Sep = SEMF(Z,N)
    ec = eby-Sep
    a = 12
    temp = (eby/a)**0.5
    C = 0.02
    w = C*math.exp(2*math.sqrt(a*(eby-e)))
    Q = eby - e
    r = 1*(10**30)
    V = 0
    sig = math.pi*R*(1 - (V/e))
    Fp = ((2*1.2)/h**2)*(((e+Q)*sig*w*eby)-((e)*sig*w*0))
    Fn = ((2*1)/h**2)*(((e)*sig*w*eby)-((e+Q)*sig*w*0))
    Fnn = ((2*2)/h**2)*(((e+Q)*sig*w*eby)-((e+Q)*sig*w*0))
    Fa = ((2*4)/h**2)*(((e+Q)*sig*w*eby)-((e+Q)*sig*w*0))
    bindp = Fp/(Fp+Fn+Fa+Fnn)
    binda = Fa/(Fp+Fn+Fa+Fnn)
    bindnn = Fnn/(Fp+Fn+Fa+Fnn)
    
    n = crosss*(1-(1+(ec/temp))*math.exp(-(ec/temp)))
    nn = crosss*(((e*math.exp(-(e/temp))*bindnn*ec)-(e*math.exp(-(e/temp))*bindnn*0))/((e*math.exp(-(e/temp))*eby)-(e*math.exp(-(e/temp))*0)))
    al = crosss*(((e*math.exp(-(e/temp))*binda*ec)-(e*math.exp(-(e/temp))*binda*0))/((e*math.exp(-(e/temp))*eby)-(e*math.exp(-(e/temp))*0)))
    p = crosss*(((e*math.exp(-(e/temp))*bindp*ec)-(e*math.exp(-(e/temp))*bindp*0))/((e*math.exp(-(e/temp))*eby)-(e*math.exp(-(e/temp))*0)))
    sigg = ['(2)n','(2)nn','(2)al','(2)p',react]
    weights = [n/((R**2)*math.pi),nn/((R**2)*math.pi),al/((R**2)*math.pi),p/((R**2)*math.pi),crosss/((R**2)*math.pi)]
    win=choices(sigg, weights)
    return win, weights


#for protons

def sig_pn(R,e,A):
    h = Planck/(2*math.pi)
    Za = 1
    Zx = -90
    r = 1*(10**30)
    V = (Za*Zx*(2.7**2))/r
    sig = math.pi*R*(1 - (V/e))
    C = 0.02
    a = 12
    eby = 300
    w = C*math.exp(2*math.sqrt(a*(eby-e)))
    Q = eby - e
    Fp = ((2*1.2)/h**2)*(((e)*sig*w*eby)-((e)*sig*w*0))
    Fn = ((2*1)/h**2)*(((e+Q)*sig*w*eby)-((e+Q)*sig*w*0))
    Fnn = ((2*2)/h**2)*(((e+Q)*sig*w*eby)-((e+Q)*sig*w*0))
    Fa = ((2*4)/h**2)*(((e+Q)*sig*w*eby)-((e+Q)*sig*w*0))
    sigpn = sig*(Fn/(Fp+Fn+Fa+Fnn))
    sigpa = sig*(Fa/(Fp+Fn+Fa+Fnn))
    sigp2n = sig*(Fnn/(Fp+Fn+Fa+Fnn))
    return sigpn, sig, sigpa, sigp2n

from random import choices

Type = 'n'
A = 231
counts = 30
def collisions(env,Type,A,counts):
    h = Planck/(2*math.pi)
    testNum=1
    r_0 = 1.33
    M = m_n
    R = r_0*(A**(1/3))
    V0 = 100
    if Type == 'n':
        react = ['np','cap','n2n','scat','a','nn']
        n2n = 0
        a = 0
        scat = 0
        nn = 0
        cap = 0
        np = 0
        sec_reactions = 0
        while True:
            print('Test %d' % testNum)
            e=rm.randint(1000,2000)/100
            l = 1
            e0 = 10/(A**(2/3))
            nl = 0
            f = 0.003    #time in seconds
            k = ((2*M*e)**0.5)/h
            wav = k**(-1)
            yield env.timeout(1)
            sig__np, sig__nn = sig_np(R,wav,e,V0)
            sig_cap__av = sig_cap_av(R,l,e,V0)
            sig__n2n = sig_n2n(R,e,V0)
            sig__sc = math.pi*(wav**2)*(2*l +1)*(abs(1-nl)**2)
            sig__a = (2*math.pi)*(2*l +1)*(1-abs(nl))
            cross = [sig__np/(math.pi*(R**2)),sig_cap__av/(math.pi*(R**2)),sig__n2n/(math.pi*(R**2)),sig__sc/(math.pi*(R**2)),sig__a/(math.pi*(R**2)),sig__nn/(math.pi*(R**2))]
            win=choices(react, cross)
            if win==['n2n']:
                n2n+=1
                wiin = True
                winner,croos = sec_re(sig__n2n,A/2,A/2,e,R,'n2n')
            elif win==['a']:
                a+=1
                wiin = False
            elif win==['scat']:
                scat+=1
                wiin = True
                winner,croos = sec_re(sig__sc,A/2,A/2,e,R,'scat')
            elif win==['nn']:
                nn+=1
                wiin = True
                winner,croos = sec_re(sig__nn,A/2,A/2,e,R,'nn')
            elif win==['cap']:
                cap+=1
                wiin = False
            elif win==['np']:
                np+=1
                wiin = True
                winner,croos = sec_re(sig__sc,A/2,A/2,e,R,'np')
            print(e)
            print(cross)
            print(croos)
            testNum+=1
            print('n2n',n2n,'scat',scat,'a',a,'nn',nn,'cap',cap,'np',np)
            if wiin==True and win!=winner:
                print('The reaction is {},{}'.format(win,winner))
                sec_reactions+=1
            else:
                print('The reaction is {}'.format(win))
            print('there have been',sec_reactions,'secondary reactions\n')
    elif Type=='p':
        react = ['pn','pp','pa','p2n']
        pn = 0
        pp = 0
        pa = 0
        p2n = 0
        for i in range(counts):
            print('Test %d' % testNum)
            e=rm.randint(1000,2000)/10
            sig__pn,sig__pp,sig__pa,sig__p2n = sig_pn(R,e,A)
            cross = [sig__pn/(math.pi*(R**2)),sig__pp/(math.pi*(R**2)),sig__pa/(math.pi*(R**2)),sig__p2n/(math.pi*(R**2))]
            win=choices(react, cross)
            if win == ['pn']:
                pn+=1
            elif win == ['pp']:
                pp+=1
            elif win == ['pa']:
                pa+=1
            else:
                p2n+=1
            testNum+=1
            print(win)
            print(e)
            print(pn,pp,pa,p2n)
            print(cross,'\n')
env = simp.Environment()
env.process(collisions(env,Type,A,counts))
env.run(until=1001)
