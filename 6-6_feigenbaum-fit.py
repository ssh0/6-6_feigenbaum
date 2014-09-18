#! usr/bin/env python
# coding:utf-8
""" 計算機実習
問題6.6 ファイゲンバウム定数の評価
-a 最小2乗法で r_infinity を求める。
作成者：藤本將太郎
"""

import scipy.optimize as optimize
from numpy import *

delta = 4.669201609102991
# b=[0.750000, 0.862372, 0.886023, 0.891102,
#    0.892190, 0.892423, 0.892473, 0.892484]
# k = range(1, len(b)+1)
b = [0.886023, 0.891102, 0.892190, 0.892423]
k = range(3, 7)
parameter0 = [1.0, 1.0]  # c, r_m　初期値

def fit_func(parameter0, k, b):
    c = parameter0[0]
    r_infinity = parameter0[1]
    residual = b - (r_infinity - c * delta ** (-k))
    return residual

result = optimize.leastsq(fit_func, parameter0, args=(array(k), array(b)))

print 'c=', result[0][0]
print 'r_infinity=', result[0][1]
