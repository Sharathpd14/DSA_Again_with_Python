import multiprocessing
import time
import sys
import math

sys.set_int_max_str_digits(100000)  # Disable the limit on the number of digits in an integer

def compute_factorial(n):
    print("Computing factorial of", n)
    result = math.factorial(n)
    print(F"factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    NUMBERS = [1000, 2100, 1600, 800, 5000]
    
    start_time = time.perf_counter()
    
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, NUMBERS)
        
        
    end_time = time.perf_counter()
    
    print(f"Results: {results}")
    print(f"Time taken with multiprocessing: {end_time - start_time:.12f} seconds")
    