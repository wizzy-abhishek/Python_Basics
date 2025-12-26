import multiprocessing
import time
def square():
    for i in range(10):
        time.sleep(1)
        print(f"square: {i*i}")

def cube():
    for i in range(10):
        time.sleep(1)
        print(f"cube: {i*i*i}")

if __name__ == '__main__': # Stops child process to re-import and avoids infinte loop
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target= cube)

    p1.start()
    p2.start()