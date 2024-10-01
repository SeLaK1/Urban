
def is_prime(fun):
    def obrabotka(*args):
        rez = fun(*args)
        if True in list(True if rez % x == 0 else False for x in range(2, rez//2+1)):
            return 'Сложное'
        return 'Простое'
    return obrabotka
@is_prime
def sum_three(*args):
    return sum(args)

print(sum_three(18, 2, 3))