#
import pygame
import time
import sys
#
from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet
#


class AlienInvasion:
#
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_heinght = self.screen.get_rect().height
        # 1. 统一在这里设置屏幕尺寸
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
#
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.aliens = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        self._create_fleet()


#
    def run_game(self):
        """主游戏循环"""
        while True:
                # 2. 将事件监听和逻辑更新分开
                self._check_events()
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_screen()
                self.clock.tick(60)
#


    def  _check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)



    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key ==pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key  == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()



    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key ==pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

#
    def _fire_bullet(self):
        """"""
        #
        if len(self.bullets) < self.settings.bullets_allowed:
     
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

#
    def _create_fleet(self):
        """"""
        alien = Alien(self)
        self.aliens.add(alien)



    def _update_bullets(self):
        self.bullets.update()
#
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(self.bullets)



#
    def _update_screen(self):
         #  刷新屏幕并控制帧率
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw(self.screen)
            self.ship.blitme()
            self.aliens.draw(self.screen)

            pygame.display.flip()


#
if __name__ == "__main__":
    # 4. 创建实例并调用方法
    ai = AlienInvasion()
    ai.run_game()
    # 注意：由于 run_game 是个死循环，下面的代码通常不会执行，除非在 check_events 中修改循环条件
    pygame.quit()
    sys.exit()

