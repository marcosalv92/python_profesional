import time

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter +=1
            yield n1
        elif counter == 1:
            counter +=1
            yield n2
        else:
            counter += 1
            result = n1 + n2
            n1, n2 = n2, result
            yield result

if __name__ == '__main__':
    fibonnacci = fibo_gen()
    for element in fibonnacci:
        print(element)
        time.sleep(1)