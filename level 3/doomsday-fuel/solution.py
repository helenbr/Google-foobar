from fractions import Fraction
import numpy as np
from fractions import gcd

def solution(m):
    if len(m) < 2:
        return [1,1]
    r = calculate_r_matrix(m)
    q = calculate_q_matrix(m)
    f = np.linalg.inv(np.subtract(np.identity(len(q)), q))
    fr = np.dot(f, r)
    result = calculate_array(fr[0])
    return result

def calculate_r_matrix(m):
    array = set()
    for i in range(len(m)):
        if sum(m[i]) == 0:
            array.add(i)
    r = []
    for i in range(len(m)):
        if i not in array:
            row_total = float(sum(m[i]))
            r_temp = []
            for j in range(len(m[i])):
                if j in array:
                    r_temp.append(m[i][j]/row_total)
            r.append(r_temp)
    return r

def calculate_q_matrix(m):
    array = set()
    for i in range(len(m)):
        if sum(m[i]) == 0:
            array.add(i)
    q = []
    for i in range(len(m)):
        if i not in array:
            row_total = float(sum(m[i]))
            q_temp = []
            for j in range(len(m[i])):
                if j not in array:
                    q_temp.append(m[i][j]/row_total)
            q.append(q_temp)
    return q

def calculate_array(l):
    array = []
    denoms = []
    for num in l:
        frac = Fraction(num).limit_denominator()
        array.append(frac.numerator)
        denoms.append(frac.denominator)
    lcd = 1
    for denom in denoms:
        lcd = lcd * denom // gcd(lcd, denom)
    for i in range(len(array)):
        array[i] = array[i] * int(lcd/denoms[i])
    array.append(lcd)
    return array