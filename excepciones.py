import re

class correo:
    def __init__(self):
        self.correoelectronico = str(input("El correo electronico es: "))
    def comprobar(s):
        if re.search(". * @. * \ .. *", s) == None:
            return False
        else:
            return True
    
while True:
    correo_usuario = input("Introduzca su correo electronico: ")
    cemail = correo(correo_usuario)
    if correo.valido() == False:
        print("No ha introducido un correo valido")
    else:
        if correo.existe() == False:
            print("Cuenta bloqueada")
            exit()
        print("Bienvenido")
        exit()