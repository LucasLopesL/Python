
class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c


lado1 = float(input('Digite o 1º lado do triângulo: '))
lado2 = float(input('Digite o 2º lado do triângulo: '))
lado3 = float(input('Digite o 3º lado do triângulo: '))

triangulo1 = Triangulo(lado1, lado2, lado3)
print(triangulo1.calcular_perimetro())
