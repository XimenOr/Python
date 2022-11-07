class Calculadora:

    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))

    def sumar(self):
        suma=self.valor1+self.valor2
        print("El total de la suma es",suma)

    def restar(self):
        resta=self.valor1-self.valor2
        print("El total de la resta es",resta)

    def multiplicar(self):
        multiplicar=self.valor1*self.valor2
        print("El resultado de la multiplicacion es",multiplicar)

    def dividir(self):
        dividir=self.valor1/self.valor2
        print("El resultado de la division es",dividir)


operacion1=Calculadora()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.dividir()
