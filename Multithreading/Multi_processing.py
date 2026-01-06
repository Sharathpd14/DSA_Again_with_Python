import multiprocessing
import time


def square():
    for i in range(5):
        time.sleep(1.5)
        print(f"Square of {i} is {i * i}")
        

def cube():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube of {i} is {i * i * i}")


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)
    t = time.perf_counter()
    p1.start()
    p2.start()

    p1.join()   
    p2.join()

    fi_t = time.perf_counter() - t
    print(f"Time taken with multiprocessing: {fi_t:.12f} seconds")