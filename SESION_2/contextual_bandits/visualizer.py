import pygame as pg
import numpy as np

pg.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
BROWN = (100,100,0)
FPS = 120
WIDTH = 600
HEIGHT = 600
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('contextual bandits')

clock = pg.time.Clock()

running = True
ops = 0
img_states = [pg.image.load(f'state{i+1}.png').convert_alpha() for i in range(2)]
img_actions = [pg.image.load(f'action{i+1}.png').convert_alpha() for i in range(5)]


fonts = pg.font.get_fonts()

def draw_text(surf,text,font_name,size, x, y,color):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)



def visualize(states,actions,n_timesteps,color,title,poss,negss):
    states = np.array(states,dtype=np.int16)
    actions = np.array(actions,dtype=np.int16)
    n_frames = 60
    ps = 0
    ns = 0
    for t in  range(n_timesteps):
        
        cur_state = states[t]
        cur_action = actions[t]
        p = poss[t]
        n = negss[t]
        for f in range(n_frames):
            
            #print('states[t]',states[t])
            #print('actions[t]',actions[t])
            print(clock.tick(FPS))
            #state = pg.image.load('C:\\Users\\mateo\\Downloads\\ironman.png').convert_alpha()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()


            state = img_states[cur_state]
            state = pg.transform.scale(state,(128,128))

            action = img_actions[cur_action]
            action = pg.transform.scale(action,(256,256))
            
            agent = pg.image.load('agent.png').convert_alpha()
            agent = pg.transform.scale(agent,(128,128))
            
            screen.fill(color)
            
            screen.blit(state,(WIDTH//2 - 64,HEIGHT//2 + 128))
            screen.blit(agent,(WIDTH//2 - 64,HEIGHT//2 ))
            screen.blit(action,(WIDTH//2 - 128,HEIGHT//2 - 256))
            
            if f < n_frames//6:
                screen.fill(color)
            elif n_frames//6 <= f < 3*n_frames//6:
                pg.draw.rect(screen,color,(0,0,WIDTH,300))
            font_name = pg.font.match_font('verdana')
            draw_text(screen,title,font_name,30, WIDTH//2, 5,WHITE)
            
            draw_text(screen,str(ps),font_name,30, WIDTH//2+200, 5,BLUE)
            draw_text(screen,str(ns),font_name,30, WIDTH//2-200, 5,BROWN)
            pg.display.flip()

            if f == 0 and t == 0:
                pg.time.wait(1000)
        ps +=p
        ns +=n

if __name__ == '__main__':
    states = np.random.randint(0,2,size=10)
    actions = np.random.randint(0,5,size=10)
    visualize(states,actions,10,WHITE)



