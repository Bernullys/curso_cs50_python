class Class_name:
    def __init__(self, param1, param2):
        self._param1 = param1
        self.param2 = param2
    
    def __str__(self):
        return f"{self.param1} + {self.param2} = {self.param1 + self.param2}"
    
    @property
    def param1(self):
        return self._param1






def main():

    new_object = Class_name(2,4)
    print(new_object)

    #new_object.param1 = 10                 # Esto es lo que justamente se quiere evitar cuando hacemos ese atributo una propiedad. No poder asignarle un valor.
    print(new_object.param1)                #Solo lo podre imprimir por default. Aunque si se hace new_object_param1 igual lo puedo manipular, no se debe.



if __name__ == "__main__":
    main()