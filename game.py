import pygame
import math
from Board import Board


# Set up the game state
pygame.init()
clock = pygame.time.Clock()
state = 'init'  # One of 'init', 'play' 'increment'
MAX_FPS = 60

# Set up the drawing window
display_size = (720, 720)
screen = pygame.display.set_mode(display_size)
pygame.display.set_caption("Conway's Game of Life")

# Initialize the board
cell_size = 30
board_area = (660, 720)
board_size = (int(board_area[0] / cell_size), int(board_area[1] / cell_size))
board = Board(board_size, init='empty')

# Initialize cells
cells = []
for i in range(board_size[0]):
    column = []
    for j in range(board_size[1]):
        column.append(pygame.Rect((j * cell_size, i * cell_size),
                                  (cell_size * 0.9, cell_size * 0.9)))
    cells.append(column)

# Initialize the buttons
play_button = pygame.Rect((10, 670), (60, 40))
pause_button = pygame.Rect((80, 670), (60, 40))
stop_button = pygame.Rect((150, 670), (60, 40))
step_button = pygame.Rect((220, 670), (60, 40))

# Initialize the slider
fps_slider_max_size = 240
fps_slider = pygame.Rect((470, 670), (10, 40))
fps_boundary = pygame.Rect((470, 670), (fps_slider_max_size, 40))

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # During 'init' mode, you can click on rectangles to make them alive or dead
            if event.button == 1 and event.pos[1] < board_area[0] and event.pos[0] < board_area[1] and state == 'init':
                cell_location = (math.floor(event.pos[1] / cell_size)
                                 if board_size[0] > event.pos[1] / cell_size
                                 else board_size[0],
                                 math.floor(event.pos[0] / cell_size)
                                 if board_size[1] > event.pos[0] / cell_size
                                 else board_size[1])

                board.set_cell(cell_location, reverse=True)

            # Pressing increment button
            elif event.button == 1 and state != 'play' and step_button.collidepoint(event.pos):
                state = 'increment'
                board.calculate_next_state()

            # Pressing play button
            elif event.button == 1 and play_button.collidepoint(event.pos):
                state = 'play'

            # Pressing reset button
            elif event.button == 1 and stop_button.collidepoint(event.pos):
                state = 'init'
                board.reset()

            # Pressing pause button
            elif event.button == 1 and state == 'play' and pause_button.collidepoint(event.pos):
                state = 'increment'

            # Adjusting slider size
            if fps_boundary.collidepoint(event.pos):
                fps_slider.width = event.pos[0] - fps_slider.x

    # If in play mode, calculate next step
    if state == 'play':
        clock.tick(MAX_FPS * fps_slider.width / fps_slider_max_size)
        board.calculate_next_state()
    else:
        clock.tick(60)

    # Fill the background with gray
    screen.fill((51, 51, 51))

    # Draw the board
    for i, row in enumerate(cells):
        for j, rect in enumerate(row):
            pygame.draw.rect(screen,
                             ([255, 255, 255] if board.state[i][j] == 0 else [0, 0, 0]),
                             rect,
                             border_radius=int(cell_size * 0.1))

    # Draw the 4 buttons
    pygame.draw.rect(screen, [0, 255, 0], play_button)
    pygame.draw.rect(screen, [255, 255, 0], pause_button)
    pygame.draw.rect(screen, [255, 0, 0], stop_button)
    pygame.draw.rect(screen, [0, 140, 255], step_button)

    # Draw the fps slider
    pygame.draw.rect(screen, [0, 0, 0], fps_boundary)
    pygame.draw.rect(screen, [math.floor(255 * fps_slider.width / fps_slider_max_size),
                              255 - math.floor(255 * fps_slider.width / fps_slider_max_size), 0], fps_slider)

    # This updates the display
    pygame.display.flip()

pygame.quit()
