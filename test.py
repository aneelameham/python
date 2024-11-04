sieve = [True]*101

for i in range(2, 100):
    if sieve[i]:
        print(i)
        for j in range(i*i, 100, i):
            print(f" These is {j} value")
            sieve[j] = False