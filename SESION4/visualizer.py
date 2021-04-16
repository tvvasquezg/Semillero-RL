import pygame as pg
import numpy as np






def visualize(env,agent,agent_poss,value_function=True):
    pg.init()

    WHITE = (255,255,255)
    BLACK = (0,0,0)
    GRAY = (100,100,100)
    GREEN = (0,255,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    factor = max(env.rows,env.cols)
    TILESIZE = 256//(factor//2)
    WIDTH = TILESIZE*env.cols#4
    HEIGHT = TILESIZE*env.rows#3
    FPS = 60

    screen = pg.display.set_mode((WIDTH,HEIGHT))

    clock = pg.time.Clock()

    #walls = [(1,1)]
    running = True
    t = 0

    def draw_text(surf,text,font_name,size, x, y,color):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surf.blit(text_surface, text_rect)
    def draw_value_function(screen,font_name,agent):
        for x in range(env.cols):#range(0,WIDTH,TILESIZE):
            for y in range(env.rows):#range(0,HEIGHT,TILESIZE):            
                draw_text(screen,str(np.round(np.max(agent.Qs[y,x]),3)),font_name,10, x*TILESIZE + TILESIZE//2, y*TILESIZE + TILESIZE//2,BLACK)
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(screen,GRAY,(x,0),(x,HEIGHT))
            
    def draw_grid():
        for y in range(0,HEIGHT,TILESIZE):
            #print(y)
            pg.draw.line(screen,GRAY,(0,y),(WIDTH,y))
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(screen,GRAY,(x,0),(x,HEIGHT))
    

    def draw_walls(walls=[(1,1)]):
        for wall in walls:
            pg.draw.rect(screen,BLACK,
            (wall[1]*TILESIZE,wall[0]*TILESIZE,
             TILESIZE,TILESIZE))

    def draw_terminal_states(terminal_states={(0,3):1,(1,3):-1}):
        for ts in terminal_states:
            if terminal_states[ts]>0:
                pg.draw.rect(screen,GREEN,
                (ts[1]*TILESIZE,ts[0]*TILESIZE,
                 TILESIZE,TILESIZE))
            else:
                pg.draw.rect(screen,RED,
                (ts[1]*TILESIZE,ts[0]*TILESIZE,
                 TILESIZE,TILESIZE))

    def draw_agent(agent_pos=(2,0)):
        pg.draw.rect(screen,YELLOW,
                     (agent_pos[1]*TILESIZE,agent_pos[0]*TILESIZE,TILESIZE,TILESIZE))
    
    font_name = pg.font.match_font('verdana')
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        screen.fill(WHITE)
        draw_grid()
        draw_walls(env.walls)
        draw_terminal_states(env.terminal_states)
        if value_function:
            draw_value_function(screen,font_name,agent)
        #agent_pos = (np.random.randint(0,3),np.random.randint(0,4))
        #print('agent_poss[t]',agent_poss[t])
        draw_agent(agent_poss[t])
        pg.display.flip()
        pg.time.wait(50)
        t +=1
        if t == len(agent_poss):
            #print('fin')
            running = False
    
pg.quit()

    
