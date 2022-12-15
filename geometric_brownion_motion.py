import numpy as np
import matplotlib.pyplot as plt

def brown(S0,T=2,N=10000,mu=0.1,sigma=0.05):
    dt = T/N
    t = np.linspace(0,T,N)
    print(dt)
    print(t)
    W = np.random.standard_normal(size=N)
    W = np.cumsum(W)*np.sqrt(dt)
    X = (mu-0.5*sigma**2)*t+sigma*W
    S = S0 * np.exp(X)
    print(W)
    return t,S

def plot(t,s):
    plt.plot(t,s)
    plt.show()


t,s = brown(10)
plot(t,s)