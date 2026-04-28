"""
Problem: [Baekjoon 2739] multiplication table
Concept: Loop (for statement, format)
Description: Given an integer N (1<=N<=9), print multiplication table for N.
"""

N = int(input())
for i in range(1,10):
  print("{} * {} = {}".format(N,i,N*i))
