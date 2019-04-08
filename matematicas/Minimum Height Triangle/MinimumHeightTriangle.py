from sys import stdin
import math

def main():
    b,a = [int(x) for x in stdin.readline().strip().split()]
    h = (a*2)/b
    h = math.ceil(h)
    print(h)

main()