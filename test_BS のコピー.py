# -*- coding: utf-8 -*-

# test for github
#よくわかんない

from scipy.stats import norm
import numpy as np

class test:
    def __init__(self, S, K, r, v, T, opt_type):
        self.S = S
        self.K = K
        self.r = r
        self.v = v
        self.T = T
        self.opttype = opt_type

    def BS(self):
        S = self.S
        K = self.K
        r = self.r
        v = self.v
        T = self.T
        opttype = self.opttype

        d1 = (np.log(S/K) + (r + (v*v*0.5))*T) / (v * np.sqrt(T))
        d2 = d1 - v * np.sqrt(T)

        if opttype == "Call":
            C = S * norm.cdf(d1) - K * norm.cdf(d2) * np.exp(-r * T)
            return C
        elif opttype =="Put":
            P = K * norm.cdf(-d2) * np.exp(-r * T) - S * norm.cdf(-d1)
            return P

if __name__ == "__main__":
    t = test(100, 100, 0.01, 0.4, 1, "Put")
    print t.BS()
