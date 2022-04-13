def process_list(n_list,prime_list):
    first_num = n_list[0]
    prime_list.append(first_num)
    for k,num in enumerate(n_list):
        if num % first_num == 0:
            n_list.pop(k)
    return prime_list, n_list


def find_prime(n):
    prime_list = []
    num_list = list(range(2, n+1))
    while True:
        prime_list, num_list = process_list(num_list,prime_list)
        if len(num_list) == 0:
            break
    return n, prime_list

n, prime_list = find_prime(100)
print("%s以内的所有质数为：%s"%(n, prime_list))
