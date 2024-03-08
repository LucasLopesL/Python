class Livro:
    def __init__(self, titulo, autor, quantidade_paginas):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas


livro1 = Livro("Harry Potter e a Pedra Filosofal", "J. K. Rowling", 264)
print(livro1.titulo)
