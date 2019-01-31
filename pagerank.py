# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 14:58:21 2019

@author: samer
"""

import numpy as np

def pageRank(G, d = 0.85, tolerance = 0.00001):
    n = np.shape(G)[0]
    rank = np.ones(n)
    onesCol = np.ones((n, 1))
    D = np.transpose(G.dot(onesCol))[0]
    change = 1
    sum2 = np.sum(rank)
    while change > tolerance:
        sum1 = sum2
        for index in range(n):
            Iset = G[:, index]
            div = (rank/D)
            tsum = div.dot(Iset)
            rank.itemset(index, ((1-d) + (d*tsum)))
        sum2 = np.sum(rank)
        change = abs(sum2 - sum1)
        print("change = ", change)
    return rank

#main
if __name__=='__main__':
    G = np.array([[0,1,1,1,1,0,0,0,0,0],
                      [1,0,1,1,1,1,0,0,0,0],
                      [1,1,0,0,0,0,0,0,0,0],
                      [1,1,1,0,0,0,0,0,0,0],
                      [0,1,0,0,0,1,1,0,1,0],
                      [0,1,0,0,1,0,1,1,1,0],
                      [0,0,0,0,1,1,0,1,1,1],
                      [0,0,0,0,0,1,1,0,0,0],
                      [0,0,0,0,1,1,1,0,0,1],
                      [0,0,0,0,0,1,1,0,0,0]])
    print(pageRank(G))