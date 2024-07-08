numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(len(numbers)):
    flag = True
    if abs(numbers[i]) > 2:
        if numbers[i] % 2 != 0:
            for j in range(3, int(numbers[i]/2), ):
                if flag == True:
                    if i % j == 0:
                        flag = False
        else:
            flag = False
        if flag == True:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])

print(primes)
print(not_primes)











