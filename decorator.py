
def funcion_decoradora(func):
    def wrapper(string):
        print('Este es el primer elemento')
        func(string)
        print('Este es el segundo elemento')
    return wrapper

@funcion_decoradora
def saluda(string):
    print(f'Hola {string}')

def despedida(string):
    print(f'Adios {string}')



saluda('Marcos')

despedida = funcion_decoradora(despedida)

despedida('Pedro')

