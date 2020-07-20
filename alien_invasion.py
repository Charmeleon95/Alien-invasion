import sys
import  pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()


    def run_game(self):

        while True: #3
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.bullets.update()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
              if event.key == pygame.K_LEFT:
                  self.ship.moving_left = True
              if event.key == pygame.K_q:
                  sys.exit()
              if event.key == pygame.K_SPACE:
                  self._fire_bullet()
            elif event.type==pygame.KEYUP:
               if event.key==pygame.K_RIGHT:
                    self.ship.moving_right = False
               if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _fire_bullet(self):
        new_bullet=Bullet(self)
        self.bullets.add(new_bullet)
    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            pygame.display.flip()
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()
