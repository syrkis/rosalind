"""
k individuals have two of G
m individuals have one G and one not G
n individuals have no G
"""

from sys import stdin
k, m, n = map(int, stdin.read().strip().split())
N = sum([k, m, n])


