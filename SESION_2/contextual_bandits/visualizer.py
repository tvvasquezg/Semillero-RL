import pygame as pg

WHITE = (255,255,255)
BLACK = (0,0,0)

FPS = 1
WIDTH = 600
HEIGHT = 600
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('contextual bandits')

clock = pg.time.Clock()

running = True
ops = 0

def visualize(states,actions,n_timesteps,color):
    for t in  range(n_timesteps):
        print('states[t]',states[t])
        print('actions[t]',actions[t])
        clock.tick(FPS)
        #state = pg.image.load('C:\\Users\\mateo\\Downloads\\ironman.png').convert_alpha()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()



        if states[t] == 0:
            state = pg.image.load('state1.png').convert_alpha()
            state = pg.transform.scale(state,(128,128))
        elif states[t] == 1:
            state = pg.image.load('state2.png').convert_alpha()
            state = pg.transform.scale(state,(128,128))

        if actions[t] == 0:
            action = pg.image.load('action1.png').convert_alpha()
            action = pg.transform.scale(action,(256,256))
        elif actions[t] == 1:
            action = pg.image.load('action2.png').convert_alpha()
            action = pg.transform.scale(action,(256,256))
        elif actions[t] == 2:
            action = pg.image.load('action3.png').convert_alpha()
            action = pg.transform.scale(action,(256,256))        
        elif actions[t] == 3:
            action = pg.image.load('action4.png').convert_alpha()
            action = pg.transform.scale(action,(256,256))        
        elif actions[t] == 4:
            action = pg.image.load('action5.png').convert_alpha()
            action = pg.transform.scale(action,(256,256))        
        elif actions[t] == 5:
            action = pg.image.load('action6.png').convert_alpha()
            action = pg.transform.scale(action,(256,256))  


        agent = pg.image.load('agent.png').convert_alpha()
        agent = pg.transform.scale(agent,(128,128))
        screen.fill(color)
        screen.blit(state,(WIDTH//2 - 64,HEIGHT//2 + 128))
        screen.blit(agent,(WIDTH//2 - 64,HEIGHT//2 ))
        screen.blit(action,(WIDTH//2 - 128,HEIGHT//2 - 256))
        pg.display.flip()
