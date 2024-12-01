import pygame

class Board:
    def __init__(self, rows, cols, cell_size, cor_fundo):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.cor_fundo = cor_fundo

    def draw(self, tela, cor_linha):
        # Desenha as linhas horizontais
        for row in range(self.rows + 1):  # +1 para garantir que a última linha seja desenhada
            y = row * self.cell_size
            pygame.draw.line(tela, cor_linha, (0, y), (self.cols * self.cell_size, y), 1)  # A espessura é '1' para linhas finas
        
        # Desenha as linhas verticais
        for col in range(self.cols + 1):  # +1 para garantir que a última coluna seja desenhada
            x = col * self.cell_size
            pygame.draw.line(tela, cor_linha, (x, 0), (x, self.rows * self.cell_size), 1)  # A espessura é '1' para linhas finas
