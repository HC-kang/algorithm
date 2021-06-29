def solution(s):
    dic = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm',
           'nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
    while True:
        before = len(s)
        for i in dic:
            s = s.replace(i, '')
        after = len(s)
        if before == after:
            return 0
        elif s=='':
            return 1


s1 = 'baabaa' # 1
s2 = 'cdcd' # 0






import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 0.1

s = np.random.normal(mu, sigma, 1000)
s

plt.figure(figsize = (15, 7))
plt.plot(s)

count, bins, ignored = plt.hist(s, 30, normed
=True)

plt.plot(bins, 1/(sigma * np.sqrt(2*np.pi))*np.exp(-(bins-mu)**2/2*(sigma)))