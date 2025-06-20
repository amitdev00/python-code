#  Print all the numbers from 1 to 10 which are divisible by 3

# for numbers in range(1, 10):
#     if numbers % 3 == 0:
#         print(numbers)


# print all the prime numbers from 1 to 10

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
