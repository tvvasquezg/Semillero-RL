import pygame
import random
import numpy as np
import matplotlib.pyplot as plt
 # set SDL to use the dummy NULL video driver, 
#   so it doesn't need a windowing system.




#np.random.seed(1)

WIDTH = 480
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Epsilon-greedy Agent")
clock = pygame.time.Clock()

fonts = pygame.font.get_fonts()

def draw_text(surf,text,font_name,size, x, y,color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)





K = 3

#7:02
class Visualizer:
    def __init__(self,epsilon,timesteps,qs,Qs):
        
        self.epsilon = epsilon
        self.timesteps = timesteps
        self.t = 0
        self.qs = qs
        self.Qs = Qs
        self.t = 0
        self.first_button = 0
        self.second_button = 0
        self.third_button = 0
        self.rewards = np.zeros(timesteps)
        self.total_rewards = 0
        self.load_data()
        
    def load_data(self):
        self.img = pygame.image.load('spritesheet.png').convert()
        self.robot = pygame.image.load('robot.png').convert_alpha()
        self.font_name = pygame.font.match_font('verdana')
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    def update(self,action,epsilon,t):
        all_sprites.update()
        self.t =t
        self.epsilon = epsilon
        
        color = WHITE
        self.piece = (0,0,64,64)
        self.piece2 = (128,0,64,64)
        self.piece3 = (256,0,64,64)

        if action == 0:
            number = random.choice([0,64])
            self.piece = (number,number,64,64)
            self.first_button +=1
        elif action == 1:
            number = random.choice([0,64])
            self.piece2 = (64-number,number,64,64)
            self.second_button +=1
        elif action == 2:
            number = random.choice([0,64])
            self.piece3 = (64-number,number,64,64)
            self.third_button +=1

    def draw(self):
        screen.fill(BLACK)

        all_sprites.draw(screen)
        screen.blit(self.img,(50,200),self.piece)
        screen.blit(self.img,((WIDTH//2)-32,200),self.piece2)
        screen.blit(self.img,(WIDTH-50-64,200),self.piece3)
        
        draw_text(screen, 'q[0] = '+str(self.qs[0]), self.font_name,25, 80,50,WHITE)
        draw_text(screen, 'q[1] = '+str(self.qs[1]), self.font_name,25, WIDTH//2,50,WHITE)
        draw_text(screen, 'q[2] = '+str(self.qs[2]), self.font_name,25, WIDTH-50-32,50,WHITE)

        draw_text(screen, 'Q[0] = '+str(np.round(self.Qs[0],2)), self.font_name,15, 80,100,WHITE)
        draw_text(screen, 'Q[1] = '+str(np.round(self.Qs[1],2)), self.font_name,15, WIDTH//2,100,WHITE)
        draw_text(screen, 'Q[2] = '+str(np.round(self.Qs[2],2)), self.font_name,15, WIDTH-50-32,100,WHITE)


        
        draw_text(screen, str(self.first_button), self.font_name,30, 80,150,WHITE)
        draw_text(screen, str(self.second_button), self.font_name,30, WIDTH//2,150,WHITE)
        draw_text(screen, str(self.third_button), self.font_name,30, WIDTH-50-32,150,WHITE)
        draw_text(screen, str(np.round(self.total_rewards,2)),self.font_name,30, WIDTH//2,10,WHITE)


        draw_text(screen, 'Epsilon: '+str(self.epsilon), self.font_name,20, 128,350,WHITE)
        draw_text(screen, 'timestep: '+str(self.t), self.font_name,20, 128,400,WHITE)
    
        pygame.display.flip()
#    def return_rewards(self)   
    def render(self,action,reward,epsilon,t):
        if self.t < self.timesteps:
            self.rewards[self.t] = reward
            self.total_rewards +=reward
            #Qs[action] += alpha*(reward - Qs[action])
            self.events()
            self.update(action,epsilon,t)
            self.draw()


        
        
        

def render(alpha,epsilon,timesteps):
    
    first_button = 0
    second_button = 0
    third_button = 0
    rewards = np.zeros(timesteps)
    total_rewards = 0
    img = pygame.image.load('spritesheet.png').convert()
    robot = pygame.image.load('robot.png').convert_alpha()

    for t in range(timesteps):
        # keep loop running at the right speed
        clock.tick(FPS)
        action = choose_action(epsilon)
        #epsilon *=0.999
        reward = get_reward(action)
        rewards[t] = reward
        total_rewards +=reward
        Qs[action] += alpha*(reward - Qs[action])
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            #if event.type == pygame.KEYDOWN:
             #   opc = (opc +1)%3
        #print(opc)
        # Update
        all_sprites.update()

        #img = pygame.transform.scale(img,(300,300))
        #rect = img.get_rect()
        # Draw / render
        screen.fill(BLACK)
        #rect.draw(screen)
        
        #screen.blit(img,(50,200),(number,number,64,64))
        #pygame.draw.rect(screen,(255,0,0),(100,200,300,300))
        all_sprites.draw(screen)
        font_name = pygame.font.match_font('verdana')
        color = WHITE
        piece = (0,0,64,64)
        piece2 = (128,0,64,64)
        piece3 = (256,0,64,64)
        # *after* drawing everything, flip the display
        if action == 0:
            number = random.choice([0,64])
            piece = (number,number,64,64)
            first_button +=1
            #screen.blit(img,(50,200),(number,number,64,64))
        elif action == 1:
            number = random.choice([0,64])
            piece2 = (64-number,number,64,64)
            second_button +=1
            #screen.blit(img,(WIDTH//2,200),(64+number,number,64,64))
                    #if  
                    #size -=1
        elif action == 2:
            number = random.choice([0,64])
            piece3 = (64-number,number,64,64)
            third_button +=1
        screen.blit(img,(50,200),piece)
        screen.blit(img,((WIDTH//2)-32,200),piece2)
        screen.blit(img,(WIDTH-50-64,200),piece3)
        
        draw_text(screen, 'q[0] = '+str(qs[0]), font_name,25, 80,50,color)
        draw_text(screen, 'q[1] = '+str(qs[1]), font_name,25, WIDTH//2,50,color)
        draw_text(screen, 'q[2] = '+str(qs[2]), font_name,25, WIDTH-50-32,50,color)

        draw_text(screen, 'Q[0] = '+str(np.round(Qs[0],2)), font_name,15, 80,100,color)
        draw_text(screen, 'Q[1] = '+str(np.round(Qs[1],2)), font_name,15, WIDTH//2,100,color)
        draw_text(screen, 'Q[2] = '+str(np.round(Qs[2],2)), font_name,15, WIDTH-50-32,100,color)


        
        draw_text(screen, str(first_button), font_name,30, 80,150,color)
        draw_text(screen, str(second_button), font_name,30, WIDTH//2,150,color)
        draw_text(screen, str(third_button), font_name,30, WIDTH-50-32,150,color)
        draw_text(screen, str(np.round(total_rewards,2)),font_name,30, WIDTH//2,10,color)
        #draw_text(screen, 'Click Here!', font_name,50, WIDTH//2,HEIGHT//2,color)
        #screen.blit(robot,(WIDTH//2,HEIGHT-32))
        pygame.display.flip()
    return rewards

def graph(l_rewards,labels):
    for i,rewards in enumerate(l_rewards):
        cumul_sum = np.cumsum(rewards)
        dens = np.arange(len(rewards))+1
        data = cumul_sum/dens
        plt.plot(data,label='Epsilon: '+str(labels[i])) 
    plt.legend()
    plt.show()

if __name__ == '__main__':
    def get_reward(action):
        return np.random.normal(qs[action],1)

    def choose_action(epsilon=0.1):
        p = np.random.rand()

        if p < epsilon:
            return np.random.choice(K)
        else:
            return np.argmax(Qs)
    alpha = 0.1
    epsilon = 0.1
    timesteps = 10_000
    qs = np.random.randint(-5,5,size=K)
    Qs = np.zeros(K)
    total_rewards = 0
    trs = render(alpha,epsilon,timesteps)
    #v = Visualizer(alpha,epsilon,timesteps)
    #v.render()
    print('total_rewards',trs)
    pygame.quit()
