from sys import stdin

def main():
    cases = int(stdin.readline().strip())
    for c in range(cases):
        n = int(stdin.readline().strip())
        handShake = 0
        for i in range(1,n):
            handShake += n-i
            #print(handShake)
        print(handShake)

main()