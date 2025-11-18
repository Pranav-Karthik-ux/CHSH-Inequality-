import numpy as np
import matplotlib.pyplot as plt
from qutip import (Qobj, basis, expect, qeye, sigmaz, tensor)
a=basis(2,0)
b=basis(2,1)
psi_plus= (1/np.sqrt(2))*(tensor(a,a)+tensor(b,b)) #bell state
def rotation(theta):
    t=np.cos(theta)*qeye(2)+np.sin(theta)*(b*a.dag()-a*b.dag())
    return t
def CHSH_quantity(t):
    theta=[t/2,-t/2]
    theta_1=[0,t]
    sigma=tensor(sigmaz(),sigmaz())
    s=0
    for i in range(2):
        for j in range(2):
            r=tensor(rotation(theta[i]),rotation(theta_1[j]))
            psi_rot=r*psi_plus
            ab=expect(sigma,psi_rot)
            if i==1 and j==1:
                s=s-ab
            else:
                s+=ab
    return s
t=np.linspace(0,2*np.pi,50)
y=np.zeros(len(t))
for i in range(len(t)):
    y[i]=CHSH_quantity(t[i])
plt.plot(t,y,'-ok')

y1= 2*np.ones(len(t))
y2=5*np.ones(len(t))
y11= -2*np.ones(len(t))
y21=-5*np.ones(len(t))
plt.fill_between(t,y1,y2, where=(y1 < y2), color='blue', alpha=0.3, label='CHSH inequality breaking')
plt.fill_between(t, y21, y11, where=(y21 < y11), color='blue', alpha=0.3)
plt.legend()
plt.xlabel('Various angles of rotation in radians')
plt.ylabel('CHSH quantity')
plt.show()
