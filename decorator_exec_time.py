from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        print(func(*args, **kwargs))
        end = datetime.now()
        time = end - start
        return time.total_seconds()
    return wrapper

@execution_time
def for_loop():
    for i in range(1000000):
        pass

@execution_time
def suma(a, b=3):
    return a+b

print(for_loop())
print(suma(20))