class Televisao:
    def __init__(self):
        self.canal = None
        self.volume = 0
    def aumentar_volume(self, volume):
        volume = int(input('Digite em quanto deseja aumentar o volume: '))
        self.volume += volume
    def diminuir_volume(self, volume):
        volume = int(input('Digite em quanto deseja diminuir o volume: '))
        self.volume -= volume
    def alterar_canal(self, canal):
        canal = int(input('Digite o canal que deseja ir: '))
        self.canal = canal

canal = str(input('Diga o canal da televisão: '))
volume = int(input('Digite o volume da televisão: '))

tv1 = Televisao

tv1.aumentar_volume(tv1, 2)
tv1.diminuir_volume(tv1, 3)
tv1.alterar_canal(tv1, 1)

print(tv1.canal)

print(f'A tv está no volume {tv1.volume} e no canal {tv1.canal}')

