import numpy as np
import matplotlib.pyplot as plt
#mars ua, au/day
xm = -3.359991802635406*10**(-1)
ym = -1.438947321197830
zm = -2.212181318593028*10**(-2)
vxm = 1.414913414952460*10**(-2)
vym = -1.971857089867377*10**(-3)
vzm = -3.886258758511196*10**(-4)
rm = (xm**2 + ym**2 + zm**2)**(1/2)
vm = (vxm**2 + vym**2 + vzm**2)**(1/2)
#mercury 
xe = 2.133679072387218*10**(-1)
ye = -3.727310311768299*10**(-1)
ze = -5.058864779204983*10**(-2)
vxe = 1.892057222101034*10**(-2)
vye = 1.513838055059527*10**(-2)
vze = -4.995475648824679*10**(-4)
re = (xe**2 + ye**2 + ze**2)**(1/2)
ve = (vxe**2 + vye**2 + vze**2)**(1/2)
#earth
xt = -6.857374296376276*10**(-1)
yt = -7.327617663911016*10**(-1)
zt = -6.678401969976758*10**(-5)
vxt = 1.232018285756917*10**(-2)
vyt = -1.176800108717166*10**(-2)
vzt = 6.153551277345986*10**(-7)
rt = (xt**2 + yt**2 + zt**2)**(1/2)
vt = (vxt**2 + vyt**2 + vzt**2)**(1/2)
#venus
alpha=np.linspace(0, 10, 100)
alphamin = alpha[0]
alphamax = alpha[-1]
sigma = alphamax - alphamin
G = 6.674 * 10**(-11)*4.46837*10**(-23)
ms = 1.989*10**(30)
betat = G*ms
x = []
y = []
def probabilidad(sigma, v, r, alpha, alphamin, alphamax, betat):	
	betamax = v**2 / (r**(alphamin-1)) 
	betamin = v**2 / (r**(alphamax-1))
	beta = v**2 / (r**(alpha-1))
	a = np.exp(-(betat-beta)**2/(sigma))
	return a, beta
y, x = probabilidad(sigma, ve, re, alpha, alphamin, alphamax, betat)
plt.plot(x, y)
plt.show()

