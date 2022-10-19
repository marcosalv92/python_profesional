import time

class EvenNumber:
    def __init__(self, max=None) -> None:
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    num_even = EvenNumber(20)

    for i in num_even:
        print(i)
        time.sleep(1)
