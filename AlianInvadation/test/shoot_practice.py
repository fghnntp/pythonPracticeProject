import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite

class Bird(Sprite):
    """
    a bird show on the screen
    """
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('../Src/BIRD.png')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen_rect.left
        self.y = float(self.screen_rect.centery)
        self.u_move = False
        self.d_move = False

    def update(self):
        """
        update the location of the bird
        """
        if self.u_move and self.rect.y >= self.screen_rect.top:
            self.y -= 2
        if self.d_move and self.rect.bottom <= self.screen_rect.bottom:
            self.y += 2
        self.rect.y = self.y
    
    def center(self):
        self.rect.centery = self.screen_rect.centery
    
    def blitme(self):
        """
        show on the screen
        """
        self.screen.blit(self.image, self.rect)

class SlideRect(Sprite):
    """
    a slide rect set on the right slide of the screen
    """
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect(0, 0, 25, 100)
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery
        self.y = float(self.rect.y)
        self.direction = 1
        self.speed = 2

    def update(self):
        if self.rect.top <= self.screen_rect.top:
            self.direction = 1
        elif self.rect.bottom >= self.screen_rect.bottom:
            self.direction = -1
        self.y += self.direction * self.speed
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, (60, 60, 60), self.rect)

class Bullet(Sprite):
    """
    a bullet to shoot
    """
    def __init__(self, screen, bird):
        """
            inherit the Sprite
        """
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 50, 25)
        self.rect.centery = bird.rect.centery
        self.rect.right = bird.rect.right
        self.x = float(self.rect.x)
        self.speed_factor = 2

    def update(self):
        """
        upate data the bullet's y location
        """
        self.rect.x += self.speed_factor
        # print("self.rect.x = " + str(self.rect.x) + " self.rect.y= " + str(self.rect.y))
        self.x = float(self.rect.x)

    def draw_bullet(self):
        """
        draw the bullet on the screen
        """
        pygame.draw.rect(self.screen, (60, 60, 60), self.rect)

class Button():
    def __init__(self,screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # button size and attribute
        self.width, self.height = 200,50
        self.bullet_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # create button rect objetc, and placed it in the mid
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.pre_msg(msg)

    def pre_msg(self, msg):
        """
        apply mesg as pucter, then set center the button on it
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.bullet_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        draw a button with one color then draw text
        """
        self.screen.fill(self.bullet_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("bird")
screen_rect = screen.get_rect()
bird = Bird(screen)
rects = Group()
bullets = Group()
new_rect = SlideRect(screen) 
rects.add(new_rect)
failed_bullet = 0
game_active = True
button = Button(screen, "Play")
pygame.mouse.set_visible(False)
pre_speed = 2
speed = 2
speed_up_factor = 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.K_UP:
                bird.u_move = True
            if event.key == pygame.K_DOWN:
                bird.d_move = True
            if event.key == pygame.K_SPACE:
                if len(bullets) < 2:
                    new_bullet = Bullet(screen, bird)
                    bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                bird.u_move = False
            if event.key == pygame.K_DOWN:
                bird.d_move = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
            if button_clicked and not game_active:
                pygame.mouse.set_visible(False)
                game_active = True
                failed_bullet = 0
                rects.empty()
                bullets.empty()

    if game_active:
        if failed_bullet > 3:
            game_active = False
            speed = pre_speed
            pygame.mouse.set_visible(True)
        screen.fill((240, 248, 255))
        bird.update()
        rects.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.right >= screen_rect.right:
                failed_bullet += 1
                bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(bullets, rects, True, True)
        if len(rects) == 0:
            rects.empty()
            new_rect = SlideRect(screen) 
            speed *= speed_up_factor
            new_rect.speed = speed
            rects.add(new_rect)
        bird.blitme()
        for rect in rects:
            rect.draw()
        for bullet in bullets:
            bullet.draw_bullet()
    else:
        button.draw_button()
    # flip recent changes on the screen
    pygame.display.flip()