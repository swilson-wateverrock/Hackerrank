from sys import stdin

def main():
    n,m = [int(x) for x in stdin.readline().strip().split()]

    res1 = (n+n%2)//2
    res2 = (m+m%2)//2
    print(res1*res2)

main()