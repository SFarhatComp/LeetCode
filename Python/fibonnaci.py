import time
from functools import lru_cache
import sys
sys.set_int_max_str_digits(15000)
    

@lru_cache(maxsize=3)
def fibonacci(n):
    if n <= 2:
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

if __name__ == "__main__":
    
    len_of_sequence  = 0
    MAX_SEARCHING = 1000
    n = 1
    start = time.time()
    while len_of_sequence != MAX_SEARCHING:
        len_of_sequence=len(str(fibonacci(n)))
        n+=1
        
    stop = time.time()
    print(n)
    print(stop-start)
    