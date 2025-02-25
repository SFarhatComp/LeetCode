from functools import lru_cache
# 1 Find the eleven truncatable primes
@lru_cache
def is_prime_number(n:int) -> bool:
    if n == 1:
        return False
    
    square_root_of_n = int(n**(1/2)+1)
    for i in range(2,square_root_of_n):
        if n % i == 0:
            return False
    return True

if __name__=="__main__":
    result = []
    number_to_check = 11
    while len(result)!=11:
        
        true_from_left = False
        true_from_right = False
        # Truncate from the left
        for i in range(len(str(number_to_check))):
            number_left =  number_to_check//(10**i)
            if not is_prime_number(number_left):
                break
        else:
            true_from_left = True
        
        # Truncate from the left
        for i in range(1, len(str(number_to_check))):
            number_left =  number_to_check%(10**i)
            if not is_prime_number(number_left):
                break
        else:
            true_from_right = True
        
        if true_from_left and true_from_right:
            result.append(number_to_check)
        number_to_check+=1
        
    print(sum(result))