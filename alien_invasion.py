import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Classe geral para manipular o jogo"""

    def __init__(self):
        """Inicializa o jogo"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invasão Alien")
        self.ship = Ship(self)

    def run_game(self):
        """Inicializa o loop principal do jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Metodo acionado quando se aperta uma tecla ou mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Controla quando a seta é precionada
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # Controla quando a seta é solta
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Responde quando apertamos as teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:  # Atalho para fechar o game
            sys.exit()

    def _check_keyup_events(self, event):
        """Responde quando soltamos as teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Atualiza as imagens na tela e muda para a proxima tela"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()  # Sempre mostra a tela mais recente


if __name__ == '__main__':  # Cria uma instancia e da um start no game
    ai = AlienInvasion()
    ai.run_game()
