import pygame
from board import Board
from piece import Piece

pygame.init()
tamanho = (1280, 720)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza_claro = (130, 130, 130)  # Cor cinza claro

# Configuração do tabuleiro
cell_size = 30
rows = 720 // cell_size  # número de linhas
cols = 1280 // cell_size  # número de colunas

# Cria o tabuleiro
tabuleiro = Board(rows, cols, cell_size, branco)

# Criando algumas peças
piece1 = Piece('white', 'pawn', 1, 1, cell_size)
piece2 = Piece('black', 'king', 4, 4, cell_size)

pieces = [piece1, piece2]

# Carregar a imagem de fundo
fundo_imagem = pygame.image.load('assets/cenarios/fundoTeste.jpg')  # Substitua 'fundo.jpg' pelo nome do seu arquivo de imagem
fundo_imagem = pygame.transform.scale(fundo_imagem, (tamanho[0], tamanho[1]))  # Ajusta a imagem para o tamanho da tela

dragging_piece = None  # Para armazenar a peça que está sendo arrastada
offset_x, offset_y = 0, 0  # Para armazenar a diferença de posição ao clicar na peça

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        # Detecta clique do mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for piece in pieces:
                # Checa se o clique está dentro da peça
                if (piece.col * piece.size < mouse_x < (piece.col + 1) * piece.size and
                    piece.row * piece.size < mouse_y < (piece.row + 1) * piece.size):
                    dragging_piece = piece
                    # Calcula a diferença entre a posição do mouse e o canto superior esquerdo da peça
                    offset_x = mouse_x - (piece.col * piece.size)
                    offset_y = mouse_y - (piece.row * piece.size)

        # Detecta o movimento do mouse
        if evento.type == pygame.MOUSEMOTION:
            if dragging_piece:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Ajusta a posição da peça com base na posição do mouse e o offset
                dragging_piece.row = (mouse_y - offset_y) // cell_size
                dragging_piece.col = (mouse_x - offset_x) // cell_size

        # Para quando o mouse é solto
        if evento.type == pygame.MOUSEBUTTONUP:
            # Ajusta a posição da peça para o centro da célula mais próxima
            if dragging_piece:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                dragging_piece.row = (mouse_y - offset_y) // cell_size
                dragging_piece.col = (mouse_x - offset_x) // cell_size
                dragging_piece.row = max(0, min(dragging_piece.row, rows - 1))  # Limita as coordenadas
                dragging_piece.col = max(0, min(dragging_piece.col, cols - 1))  # Limita as coordenadas
            dragging_piece = None

    tela.blit(fundo_imagem, (0, 0))  # Desenha a imagem de fundo na tela
    tabuleiro.draw(tela, cinza_claro)  # Passa a cor cinza claro para desenhar as linhas da grade

    # Desenha as peças
    for piece in pieces:
        piece.draw(tela)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
