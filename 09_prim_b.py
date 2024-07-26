DEBUG_INFO = False

def prime_num(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                if DEBUG_INFO:
                    print(num,"is not a prime number")
                if DEBUG_INFO:
                    print(i,"times",num//i,"is",num)
                break
        else:
            if DEBUG_INFO:
                print(num,"is a prime number")
            return True
    else:
        if DEBUG_INFO:
            print(num,"is not a prime number")
        return False


max_num = 500
prime_nums = {}

for z in range(0, max_num + 1):
    
    if prime_num(z):
        print("                Ich bin eine Primzahl: ", z)
        prime_nums[z] = prime_num(z)

print(prime_nums)
