"""
Problem: [Baekjoon 10950] A+B - 3
Concept: Loop (for statement, list)
Description: Given the number of test cases, take two integers A and B for each, and print A+B.
"""

a = int(input())
b = [list(map(int,input().split())) for i in range(a)]

for i in b:
  print(i[0] + i[1])
