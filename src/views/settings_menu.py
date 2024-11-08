from views import *
from models.draw import ButtonStarting

def settings_menu(game):
    back_button = ButtonStarting(game.screen, "Back", 18*SQUARE_WIDTH, 11*SQUARE_HEIGHT)
        
    running = True
    while running:
        game.screen.fill(BLACK)
        # draw_text(screen, "Settings", 60, 250, 100)
        back_button.draw(game.screen, pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                running = back_button.check_click(event, running)

        
        pygame.display.flip()