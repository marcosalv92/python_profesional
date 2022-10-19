import time

class Fibonaci:
    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.num = 0
        self.result = 0
        return self
    
    def __next__(self):
        if not self.max or self.n1 + self.n2 <= self.max:
            if self.num == 0:
                self.num += 1
                return self.n1
            elif self.num == 1:
                self.num +=1
                return self.n2
            else:
                self.num += 1
                self.result = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.result
                return self.result
        else:
            raise StopIteration
        
if __name__ == '__main__':
    num_even = Fibonaci(20)

    for i in num_even:
        print(i)
        time.sleep(1)
