import threading

def num():
    for i in range(100):
        print(i)

def alphabet():
    for i in 'abcdefghijklmnopqrstuvwxyz':
        print(i)

t1 = threading.Thread(target=num)
t2 = threading.Thread(target=alphabet)
t1.start()
t2.start()

t1.join()
print(t1.is_alive())
print(t2.is_alive())