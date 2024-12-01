import pygame

class Piece:
    def __init__(self, color, type, row, col, size):
        self.color = color  # Cor da peça (ex: 'white' ou 'black')
        self.type = type  # Tipo da peça (ex: 'king', 'queen', 'pawn', etc.)
        self.row = row  # Linha da peça no tabuleiro
        self.col = col  # Coluna da peça no tabuleiro
        self.size = size  # Tamanho da célula (para dimensionar a peça)

    def draw(self, screen):
        """Desenha a peça no tabuleiro"""
        center_x = self.col * self.size + self.size // 2
        center_y = self.row * self.size + self.size // 2
        radius = self.size // 3  # Ajusta o tamanho da peça para caber na célula

        # Cor da peça
        piece_color = (255, 255, 255) if self.color == 'white' else (255, 0, 0)

        # Desenha a peça como um círculo (ou poderia ser uma imagem)
        pygame.draw.circle(screen, piece_color, (center_x, center_y), radius)
