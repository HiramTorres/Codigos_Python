from poo.vehiculo import Moto

moto = Moto(
    "Honda", 
    "Azul", 
    "CBR", 
    "2018", 
    "Verificado", 
    "10", 
    "Deportiva", 
    "125"
)
print(moto.encendido)
moto.encender_autou()
print(moto.encendido)
#help(Car) para ver que atributos tiene el objeto
moto.year="2021"
print(moto.year)

#Encapsulamiento, no se puede acceder a los atributos directamente para, para poder modificarlos
#if __name__ == "__main__": Para que no se ejecute el codigo cuando se importa el archivo
#Se ejecuta solo si es el principal 
