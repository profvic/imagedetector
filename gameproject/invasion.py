import sys

import pygame

class Invasion:
    #overall class assets
    def __init(self):
        
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Invasion")
    
    def run_game(self):
        #starting themain loop of the game
        
        while True:
            #for the event action of mouse or keyboard clicks
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    sys.exit()
                    

            pygame.display.flip()
            
            
if __name__ == '__main__':
    ai = Invasion()
    ai.run_game()