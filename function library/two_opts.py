# str is the questions proposed
# x is the horizontal positioning of the qn
# opt1/opt2/opt3 refer to options texts
# func1/func2/func3 refer to executable function names

def two_options(str, x, opt1, func1, opt2, func2):
    quit()
    pygame.init()
    
    window_width=960
    window_height=540
    
    clock_tick_rate=20
    white = (255,255,255)
    
    bright_red = (255,0,0)
    # Open a window
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size)
    
    # Set title to the window
    pygame.display.set_caption("World War 3")
    
    dead=False
    
    clock = pygame.time.Clock()
    background_image = pygame.image.load("warback.jpg").convert()
    
    def text_objects(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    
    def button(msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(screen, ac,(x,y,w,h))
    
            if click[0] == 1 and action != None:
                action()         
        else:
            pygame.draw.rect(screen, ic,(x,y,w,h))
    
        smallText = pygame.font.Font('D:/myfonts/cs_regular.ttf',20)
        textSurf, textRect = text_objects(msg, smallText, (0,0,0))
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)
    
    while(dead==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
    
        screen.blit(background_image, [0, 0])
        largeText = pygame.font.Font('D:/myfonts/cs_regular.ttf',40)
        TextSurf, TextRect = text_objects(str, largeText, white)
        TextRect.center = ((x),(120))
        screen.blit(TextSurf, TextRect)
        button(opt1,420,220,110,50,white,bright_red,func1)
        button(opt2,420,320,110,50,white,bright_red,func2)
        pygame.display.flip()
        clock.tick(clock_tick_rate)