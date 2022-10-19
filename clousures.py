
def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, 'Error: El argumento debe ser un string'
        return string * n
    return repeater

repeat_5 = make_repeater_of(5)
print(repeat_5('Hola'))