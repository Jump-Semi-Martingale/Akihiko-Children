# -*- coding: utf-8 -*-

# test for github

import numpy as np

class test:
    def __init__(self, opt_type):
        self.opttype = opt_type
        
    def BS(self,S, K, r, v, T):
        d1 = (np.log(S/K) + (r+ (v*v*0.5))*T) / (v*np.sqrt(T))
        d2 = d1 - v*np.sqrt(T)

        if self.opttype == "Call":
            C = S * np.random.randn.cdf(d1) - K*np.random.randn.cdf(d2)*np.exp(-r*T)
            return C
        elif self.opttype =="Put":
            P = S * np.random.randn.cdf(d1) - K*np.random.randn.cdf(d2)*np.exp(-r*T)
            return P
            

if __name__ == "__main__":
    t = test("Call")
    print t.BS(100, 100, 0.01, 0.4, 1)
