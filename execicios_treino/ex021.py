class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Pedido:
    def __init__(self):
        self.produto = []

    def adicionar_produto(self, produto):
        self.produto.append(produto)

    def calcular_valor(self):
        total = 0
        for produto in self.produto:
            total += produto.preco * produto.quantidade
        return total



cafe = Produto('Café Solúvel', 5.50, 1)
arroz = Produto('Arroz Integral', 4.90, 2)
feijao = Produto('Feijão Preto', 2.80, 2)
meu_pedido = Pedido()
meu_pedido.adicionar_produto(cafe)
meu_pedido.adicionar_produto(arroz)
meu_pedido.adicionar_produto(feijao)
print('O valor total é: ', meu_pedido.calcular_valor())	    # imprime 20.90
