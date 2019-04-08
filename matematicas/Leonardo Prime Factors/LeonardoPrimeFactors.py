from sys import stdin

primes = []
isPrime = [1]*100
def seive():
    isPrime[0] = isPrime[1] = 0
    for i in range(100):
        if( isPrime[i] ):
            for j in range(i*i,100,i):
                isPrime[j] = 0
            primes.append(i)




def main():
    #print(len(primes))
    seive()
    #print(primes)
    q = int(stdin.readline().strip())
    for c in range(q):
        n = int(stdin.readline().strip())
        res = 0
        maxi = 0
        for i in range(len(primes)):
            if(primes[i] > n):
                break
            multi = 1
            for j in range(i,-1,-1): 
                multi *= primes[i-j]
        
            if(multi >= maxi and multi <= n):
                #print(primes[i])
                res = i+1
            
        print(res)
            




main()