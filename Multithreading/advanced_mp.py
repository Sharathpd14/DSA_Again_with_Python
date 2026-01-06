from concurrent.futures import ProcessPoolExecutor  
import time

def square(n):
    time.sleep(1.5)
    return f"Square of {n} is {n * n}"



if __name__ == "__main__":
   
    numbers = [0, 1, 2, 3, 4]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)
        
        
    for result in results:
        print(result)