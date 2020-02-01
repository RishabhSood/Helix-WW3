#this file contains all the functions
import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import messagebox
import time
import pygame
import sys

#defining used colors
BLACK = (  0,   0,   0)
WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)
#text animator

#score variable

score = 0
#-------------------------------screen templates --------------------------------#

#1. question template

# my_title refers to problem title
# my_x refers to title horizontal positioning
# my_qn refers to problem text (needs to be formated)
# fnt_size refers to font size for the qn text
# ansr refers to the expected input from the user
# func refers to the function to be executed incase the problem is solved correctly

def default_wrong():
    messagebox.showerror("Error", "Wrong Answer!!, try again")

#1. (a)
def qn_temp(my_title, my_x, my_qn, fnt_size, ansr, func, wrng_func, win_size = "800x350", tbx = 0, tby = 0, scr_a = 0):
    window = tkinter.Tk()
        
    window.title(my_title + " (unlimited tries question) ")
    window.geometry(win_size)
    
    lbl = Label(window,text=my_title,font=('Helvetica','20'), padx = 10, pady = 10)
    lbl.place(x=my_x, y = 10)
    
    global score
    lbl = Label(window,text="Score: " + str(score),font=('Helvetica','8'), padx = 10, pady = 10)
    lbl.place(x = 0, y = 0)
    
    qnl = Label(window,text=my_qn, border = 1, relief = "solid", font=('Helvetica',fnt_size), padx = 10, pady = 10)
    qnl.place(x=80, y = 80)
    
    my_ansr = StringVar()
    ansr_entry = Entry(window, textvariable=my_ansr)
    ansr_entry.place(x = 240+tbx, y = 220+tby, width = 400, height = 30)
    
    lbl = Label(window,text="Answer: ",font=('Helvetica','14'), padx = 10, pady = 10)
    lbl.place(x=140+tbx, y = 213+tby)
    
    
    def submitAction():
            myVar = messagebox.askquestion("Submit", "Do you wish to submit? ")
            if myVar == 'yes':
                the_ansr = my_ansr.get()
                if the_ansr == ansr:
                    global score
                    messagebox.showinfo("Correct!!", "You answered correct!")
                    time.sleep(1)
                    window.destroy()
                    score += scr_a
                    score_log = open("ww3_log.txt", "at")
                    score_log.write("\n@Checkpoint " + my_title + ", user score = " + str(score) + "\n")
                    score_log.close()
                    func()
                else:
                    wrng_func()
                
    def quitFunction():
        myVar = messagebox.askquestion("Quit Game", "Are you sure, you want to quit? ")
        if myVar == 'yes':
            score_log = open("ww3_log.txt", "at")
            score_log.write("\n+-----------------------------------------------------------------------------------------+\n")
            score_log.close()
            
            score_file = open("score.txt", "at")
            score_file.write("\nPath Score: " + str(score))
            score_file.write("\nGame quit midway @" + my_title +"\n\n")
            score_file.close()
            
            window.destroy()
            sys.exit()
        
    new_btn = Button(window, text=" ",bg="Green", fg="White",font=('Helvetica','10'), command = submitAction)
    new_btn["text"] = "Submit"
    new_btn.place(x = 380 + tbx-100, y = 270 + tby)
    
    new_btn = Button(window, text=" ",bg="Red", fg="White",font=('Helvetica','10'), command = quitFunction)
    new_btn["text"] = "Quit"
    new_btn.place(x = 380 + tbx+100, y = 270 + tby)
    
    window.mainloop()

#1. (b)
def qn_temp_no_opt(my_title, my_x, my_qn, fnt_size, ansr, func, wrng_func,win_size = "800x350", tbx = 0, tby = 0, scr_a = 0):
    window = tkinter.Tk()
        
    window.title(my_title + " (direct consequence question) ")
    window.geometry(win_size)
    
    lbl = Label(window,text=my_title,font=('Helvetica','20'), padx = 10, pady = 10)
    lbl.place(x=my_x, y = 10)
    
    global score
    lbl = Label(window,text="Score: " + str(score),font=('Helvetica','8'), padx = 10, pady = 10)
    lbl.place(x = 0, y = 0)
    
    qnl = Label(window,text=my_qn, border = 1, relief = "solid", font=('Helvetica',fnt_size), padx = 10, pady = 10)
    qnl.place(x=80, y = 80)
    
    my_ansr = StringVar()
    ansr_entry = Entry(window, textvariable=my_ansr)
    ansr_entry.place(x = 240 + tbx, y = 220 + tby, width = 400, height = 30)
    
    lbl = Label(window,text="Answer: ",font=('Helvetica','14'), padx = 10, pady = 10)
    lbl.place(x=140 + tbx, y = 213 + tby)
    
    def submitAction():
        myVar = messagebox.askquestion("Submit", "Do you wish to submit? ")
        if myVar == 'yes':
            the_ansr = my_ansr.get()
            if the_ansr == ansr:
                global score
                messagebox.showinfo("Correct!!", "You answered correct!")
                time.sleep(1)
                window.destroy()
                score += scr_a
                score_log = open("ww3_log.txt", "at")
                score_log.write("\n@Checkpoint " + my_title + ", user score = " + str(score) + "\n")
                score_log.close()
                func()
            else:   
                window.destroy()
                score_log = open("ww3_log.txt", "at")
                score_log.write("\n@Checkpoint " + my_title + ", user score = " + str(score) + "\n")
                score_log.close()
                wrng_func()
                
    def quitFunction():
        myVar = messagebox.askquestion("Quit Game", "Are you sure, you want to quit? ")
        if myVar == 'yes':
            score_log = open("ww3_log.txt", "at")
            score_log.write("\n+-----------------------------------------------------------------------------------------+\n")
            score_log.close()
            
            score_file = open("score.txt", "at")
            score_file.write("\nPath Score: " + str(score))
            score_file.write("\nGame quit midway @" + my_title +"\n\n")
            score_file.close()
            
            window.destroy()
            sys.exit()
        
    new_btn = Button(window, text=" ",bg="Green", fg="White",font=('Helvetica','10'), command = submitAction)
    new_btn["text"] = "Submit"
    new_btn.place(x = 380 + tbx-100, y = 270 + tby)
    
    new_btn = Button(window, text=" ",bg="Red", fg="White",font=('Helvetica','10'), command = quitFunction)
    new_btn["text"] = "Quit"
    new_btn.place(x = 380 + tbx+100, y = 270 + tby)
    
    window.mainloop()
    
#2.
    
# str is the questions proposed
# x is the horizontal positioning of the qn
# opt1/opt2/opt3 refer to options texts
# func1/func2/func3 refer to executable function names

def two_options(str, x, opt1, func1, opt2, func2):
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
        button(opt1,420,220,160,50,white,bright_red,func1)
        button(opt2,420,320,160,50,white,bright_red,func2)
        pygame.display.flip()
        clock.tick(clock_tick_rate)
    exit()

#3.
    
# str is the questions proposed
# x is the horizontal positioning of the qn
# opt1/opt2/opt3 refer to options texts
# func1/func2/func3 refer to executable function names

def three_options(str, x, opt1, func1, opt2, func2, opt3, func3):
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
        button(opt2,340,320,110,50,white,bright_red,func2)
        button(opt3,500,320,110,50,white,bright_red,func3)
        pygame.display.flip()
        clock.tick(clock_tick_rate)
    exit()
    
#------------------------------------------------------------------------------#
    
# decorator animation
def display_text_animation(string, pos1, pos2, mycolor, mysize, my_surf):
        text = ''
        for i in range(len(string)):
            my_surf.fill(BLACK)
            text += string[i]
            font=pygame.font.Font('D:/myfonts/thefont.ttf',mysize)
            text_surface = font.render(text, True, mycolor)
            text_rect = text_surface.get_rect()
            text_rect.center = (pos1, pos2)
            my_surf.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.event.get()
            pygame.time.wait(100)
        time.sleep(2)
        
# Game intro and loading

def load():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    
    def display_text_animation(string, pos1, pos2, mycolor, mysize):
        text = ''
        for i in range(len(string)):
            DISPLAYSURF.fill(BLACK)
            text += string[i]
            font=pygame.font.Font('D:/myfonts/thefont.ttf',mysize)
            text_surface = font.render(text, True, mycolor)
            text_rect = text_surface.get_rect()
            text_rect.center = (pos1, pos2)
            DISPLAYSURF.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.event.get()
            pygame.time.wait(100)
        time.sleep(2)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""CCS PRESENTs""", 250, 100, (0,255,0), 30)
    display_text_animation("""WORLD WAR III """, 250, 100, (0,0,255), 30)
    display_text_animation("""You're Donald Trump, President of the US. """, 250, 100, WHITE, 10)
    display_text_animation(""" Your country is at odds with Iran, China, and Russia """, 250, 100, WHITE, 10)
    display_text_animation(""" choose the path forward wisely. """, 250, 100, WHITE, 10)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    pygame.mixer.music.stop()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n------------------------------------------------------------------------------------------\n")
    score_log.write("Welcome to Path Iran\n")
    score_log.write("------------------------------------------------------------------------------------------\n\n")
    score_log.close()
    qn_temp("Somewhere in Iran (050 pts)", 230, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "202849", count_opts, default_wrong,"800x350", 0, 0, 50)

# options screen
def count_opts():
    two_options("Choose Country to initiate war with"
            , 470, "Iran", iran, "Russia", russia)
    exit()

#--------------------------------------- welcome to iran path -------------------------------------------------------------------#
#iran option welcome screen

def iran():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Iran has attacked US military """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Your bases in Iraq have retaliated.""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer the next question to continue...""", 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    qn_temp("Held Hostage... (300 pts)", 350, 
            """Some of your soldiers have been held hostage by Iran Military. To set them free, you need access to their database. 
            The database is distributed amongst 21 servers. It is known that each server has the same password. However, you've already 
            attempted access to 20/21 servers and been blocked. This is your last chance! Following information has been gathered from 
            the previous attacks:


        	Password     CC
        	228569150065 1
        	907564288621 0
        	496954400043 0
        	713459943615 0
        	211421327491 1
        	258317293172 0
        	919252724339 1
        	197103476352 0
        	151173430038 0
        	063794395936 0
        	504759866532 1
        	502906565456 0
        	790539816536 0
        	595873942664 1
        	346602334981 0
        	988808475766 1
        	559203789779 0
        	498580144863 1
        	441454897857 1
        	622818801178 0
        
        	Here, CC is number of correct digits at correct place in the password.
        	Enter password to the server below:""", 10, "884045122207", iran_chck_one, default_wrong, "1000x690", 70, 370, 300)
    
def iran_chck_one():
    two_options("Israel has requested to join war", 
            470, "Allow", iran_allw, "Fight Solo", iran_fght_solo)
    exit()
    
def iran_allw():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
  
    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Israel has bombed Iraq, suffered losses """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""No American blood shed...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You gain 500pts!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    global score
    score+=500
    iran_fght_back()
    exit()

def iran_fght_back():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""UN demands explanation!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Choose one of the explanations that follow""", 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    iran_un_exp()
    exit()
    
def iran_un_exp():
    two_options("UN has asked for an explanantion.. Select one...", 
            470, "Moderate", iran_exp_good, "Insane", iran_exp_insane)
    exit()

def iran_exp_good():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Requesting meetup ...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Countries need convincing... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer the next question to succeed...""", 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp_no_opt("Trusty Old Farts (400 pts)", 250, 
            """To cut costs, UN wished to power their network with their own special encryption. Each server would 
               Your explanation was rejected, it's now time to send in your time-tested lawyers

               You have nine lawyers with, whose arguments can have an effectiveness of 1, 2, 3, or 4.
               Iran has only six lawyers but their arguments can have effectiveness from 1, 2, 3, 4, 5, 6 due to 
               your aggression.
            
               Find out the probability of your lawyers succeeding to help them plan better, if the efficacy of 
               both sides' arguments are equal, it's a draw.
               
               Submit your answer upto 7 decimal places, as 0.BCDEFGH

            """, 10, "0.5731441",iran_cyb_atck, russia, "800x420", 10, 100, 400)
    
    exit()

def iran_exp_insane():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Prepare for hell...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""All units at standby... """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp_no_opt("Secure their Network (800 pts)", 250, 
            """To cut costs, UN wished to power their network with their own special encryption. Each server would 
            further encrypt and send information to the server numbered next, with the top server sending data back 
            down to the bottom server. That way, they could have the information entered on any node and have data 
            flow freely throughout the network.
            
            Unfortunately, the designers misinterpreted the schematics when they built the network. It was leaked 
            that each server sends data to another server at random, instead. This may compromise their freedom to 
            have the data entering the network anywhere, since certain nodes may never recieve the info and hence 
            increase data loss risks.
            
            For example, consider the following connections in a 3 server based network with servers numbered 1,2 
            and 3 in order:
                
            1 connects to 3
            3 connects to 2
            and 2 connects to 3
            
            If the information was fed in the first node, then every server would receive data. But if it were fed 
            in the second or third servers instead, then there would be no data entering first server. Note that 
            while a given server can receive data from many other servers at once, it can only send data to one 
            other server.
            
            To resolve the data loss risks, UN decided to have a minimal number of servers rewired. To rewire a 
            server is to change the server it sends data to. In the sample above, all possible losses can be avoided 
            by rewiring the second server to send data to the first server instead of the third server.
            
            Let F(n) be the sum of the minimum number of server rewirings needed over all possible data-flow 
            arrangements in a network of n servers. For example, F(3) mod 135707531 = 6.
            
            Find F(8) mod 135707531.

            """, 10, "16276736",iran_cyb_atck, iran_exp_good, "820x750", 20, 410, 800)
    exit()
    
def iran_cyb_atck():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""UN accepts your explanation""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Iran retaliates!! """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Cyber attack launched!! """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Fight off by answering the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp("Iran Cyber Attack (100 pts)", 250, 
            """Iran has launched an attack on your digital foundations, find the passcode to prevent a complete 
            strategic defeat. 125874, and its double, 251748, have the same digits, similarly, the passcode is 
            the smallest positive integer x such that 2x, 3x, 4x, 5x and 6x contain the same digits.
            """, 10, "142857", iran_cyb_opt, default_wrong, "800x320", 10, -20, 100)

    exit()
    
def iran_cyb_opt():
    two_options("Choose a mode of throwback", 
            470, "Wire To Wire", iran_cyb_on, "Cold Blooded", iran_cyb_off)
    exit()
    
def iran_cyb_on():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Engaging intelligence services...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Succeed by answering the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp("Wire with Wire (100 pts)", 250, 
            """You summon that peculiar mixture of young and old, pale as if they haven't seen the sun in decades, 
            our Intelligence Service!
        	The peculiarities of this otherworldly assault require the usage of strange Mathematicks to overflow 
            arcane buffers beyond your understanding.
            
        	There are exactly 10 ways of choosing three from five, i.e., 5C3 = 10.
            
        	In general, nCr = n! / (r! x (n-r)!)
            
        	How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?
            """, 10, "4075", iran_att, default_wrong, "800x420", 10, 100, 100)

    exit()

def iran_att():
    two_options("Choose a mode of attack", 
            470, "Cyber Warfare", iran_cyb_war, "Hunter Hunted", iran_hunt)
    exit()
    
def iran_cyb_war():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Launching cyber attack...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Succeed by answering the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp_no_opt("War of the wizards (400 pts)", 250, 
            """You try to bring the iranian network down, paving the way for a complete strategic victory.
            	Their binary nature of their network intertwines it's fate with the number 2, you must get to 
                understand the root of 2 to destroy it.
            	The square root of 2 can be expressed as an infinite continued fraction. 
                sqrt(2) =  1 + (1 / (2 + 1 / (2 + 1 / (2 + 1.....
                
            	Expanding this for the first three iterations:
            	1 + 1/2 = 3/2 = 1.5
            	1 + 1/(2 + 1/2) = 7/5 = 1.4
            	1 + 1/(2 + 1/(2 + 1/2) = 17/12 = 1.4166...
                
            	The eighth expansions is 1393/985, which is the first exxpansion where the number of digits in the 
                numerator is mroe than that in the denominator.
                
            	In the first one-thousand expansions, how many fractions contain a numerator with more digits 
                than the denominator?
            """, 10, "153", iran_win_opt, iran_hunt, "800x540", 10, 200, 400)
    
    exit()

def iran_win_opt():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""The Iranian princess pleads for mercy for her kingdom ...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Peaceful end or make Harsh demands? """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    two_options("Choose an end", 
            470, "Peace", sad_old, "Harsh demands", hegem)
    exit()
    
def iran_hunt():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Preparing troops...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Loading ammunition... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer next problem to continue """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp("Forward, glorious death! (200 pts)", 220, 
            """You believe in our troops and give them the chance to savour the ashen taste of victory.
            	In the midst of battle, divine inspiration strike you and you realise that the secret to overflowing 
                the enemy encirclements is held in Budget-Lychrel numbers.
                
            	If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
            	Not all numbers produce palindromes so quickly. For example,
            
            	349 + 943 = 1292,
            	1292 + 2921 = 4213
            	4213 + 3124 = 7337
            
            	That is, 349 took three iterations to arrive at a palindrome.
            	It has long been thought by sages that some numbers never arrive at a palindrome, 50 is a big number, 
                numbers that do not fall in line(become a palindrome) in 50
                
            	iterations are to be deemed Budget-Lychrel numbers and are the secret to victory.
                
            	How many Lychrel Numbers are there below ten-thousand?
            """, 10, "249",iran_hunt_cont, default_wrong, "800x540", 10, 200, 200)
    
    exit()

def iran_hunt_cont():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Prevent your impeachment and decapitation...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" for extreme foolishness in leading your country.. """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer next problem to continue """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp_no_opt("Prison (500 pts)", 360, 
            """You fight to prevent your impeachment and decapitation for extraordinary disservice to God and Country
            	To break the Democrats's arguments you must navigate the halls of circular thinking and break free of all reason.
            	Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
            
            	37 36 35 34 33 32 31
            	38 17 16 15 14 13 30
            	39 18  5  4  3 12 29
            	40 19  6  1  2 11 28
            	41 20  7  8  9 10 27
            	42 21 22 23 24 25 26
            	43 44 45 46 47 48 49
            
            	It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting 
                is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
            
            	If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
                If this process is continued, what is the side length of the square spiral for which the ratio of primes along 
                both diagonals first falls below 10%?
            
            """, 10, "26241", iran_win, russia, "900x540", 60, 220, 500)
    
    exit()
    
def iran_cyb_off():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Too hell with reason, too hell with the internet,""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" ..guerilla warfare, no red blooded american ..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""will bow to nerds at computers across the world from them...  """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" Answer next problem to continue... """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp("Too hell with Reason! (300 pts)", 220, 
            """You refuse to engage Iran on the cyber front, sling your greatsword on your back, and walk out 
            of the white house, prepared for guerilla warfare.

        	Iranian Strongholds are arrayed in the form of Pascal's Triangle, with 51 rows, with the vulnerable 
            holdings being those whose number in the triangle is square-free, i.e., not divisible by the square 
            of any prime.
            
        	Find the sum of the distinct square free numbers in these 51 rows.
                    
            """, 10, "34029210557338", iran_coff_cont, default_wrong, "800x400", 20, 60, 300)


    exit()

def iran_coff_cont():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Through sheer americana you have overwhelmed the enemy!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" Answer next problem to continue... """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp("Victor's Choice (150 pts)", 280, 
            """The final push, you attempt to capture the royal palace.

            	The path to the throne room is blocked by a door, you must get the passcode in time or the king may flee.
                
            	The passcode is the 3 X 10^6th term of a series defined by: 
            		a0 = 1;
            		for n ≥ 1, an is the sum of the digits of all preceding terms.
                    
            	The 10^6th term is 31054319
                
            	The sequence starts with 1, 1, 2, 4, 8, 16, 23, 28, 38, 49, ...     
            """, 10, "102915032", iran_coff_ch, default_wrong, "840x440", 20, 100, 150)
        
    exit()

def iran_coff_ch():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation(""" Declare your love for the heritage of Iran and your sadness""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" at the destruction it has faced, as you twist a knife into the """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" king's chest and American Bombers raze the capital to the ground""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" or Sue for peace, making Iran dependant on America ...""", 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    two_options("Choose an end", 
            470, "Murder", mad_dog, "Bondage", hegem)
    exit()

def iran_fght_solo():
    two_options("Choose one of the two proposed attacks", 
            470, "Invasion", iran_solo_inv, "Opp. Red Wed", iran_solo_redwed)
    exit()


def iran_solo_inv():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Preparing to invade... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    qn_temp("Plane Hijack (300 pts)", 280, 
            """You have decided to enter Iran in stealth mode. Crack password to their base. Following 
            information about the current code has been leaked by an insider. See if you can crack it:
	        
            The password is last 5 digits of the sum of all integers n, 10<n<10^17, having property as depicted:

	        Consider the number 142857. 
            We can right-rotate this number by moving the last digit 7 to the front of it, giving us 714285.
	        It can be verified that 
            714285 = 5 * 142857. 
            This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.""", 10, "75309", iran_fght_back, default_wrong
            ,"800x370", 0, 60, 300)
    exit()
    
#iran_fght_back already defined

def iran_solo_redwed():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Planning the Red Wedding... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Preparing chemicals and ammunition... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer next problem to succesfully execute... """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    qn_temp_no_opt("Convince The Supplier (200 pts)", 250, 
            """The supplier doesn't trust anyone without a code!! You are new and have been entrusted 
            with the task of arranging ammunition. Enter the code below. Follow the gudelined below to get the code:

            Consider the triangle below:
             1
            |2| |3|
             4  |5|  6
            |7 | 8   9   10
            |11| 12 |13| 14 15
            ...
        
            A set of three primes is called a prime triplet if one of the three primes has the other two as neighbours 
            in the triangle. 
            (Neighbors refers to top, below, left, right and diagonal ones, MAX 8).
            (|n| is a prime triplet member)
            We define S(n) as the sum of the primes in row n which are elements of any prime triplet.
            For example, S(5) = 24 and S(2) = 5.
        
            Key = S(10000)""", 10, "950007619", iran_red_succ, iran_solo_inv, "820x540", 40, 200, 200)
    exit()

def iran_red_succ():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Succesfully executed operation... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer next problem to fight off their deffences... """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    qn_temp_no_opt("Formation (150 pts)", 270, 
            """Fighting off their deffences will need a certain formation for the army. This formation 
            has been scribbled on a document present inside a safe. Access the document and fight off 
            their deffences!!. Enter the safe code below.

            Safe Code: 
                Sum of all n, 0 <= n <= 100, such that f(n) is a perfect square modulo 10^9 + 7.
                
            Here, 
            f(n) is the sum of the squares of the digits (in base 10) of n, 
            
            ex:
            f(442) = 4^2 + 4^2 + 2^2 = 36""", 10, "826", iran_stealth, iran_solo_inv, "760x440", -10, 100, 150)
    exit()

def iran_stealth():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("WW3music.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    display_text_animation("""Destroyed Deffences...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Attack Succesful!! """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Maintain your cover, answer the next problem.. """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp_no_opt("Hide the files! (050 pts)", 250, 
            """Out of the 1000 files of evidence, one proves your involvement. However, the labor
            available at hand is unskilled and incapable of reading. The evidence file has a special 
            property, it leave an impression on the hands of whoever touched it, which turns blue within
            10 to 20 hours of contact. The impression is however, otherwise undetectable. What is the 
            minimum amount of labor you will require to find the file within 24hrs ?
            """, 10, "10", iran_win, iran_win, "760x340", -10, 20, 50)
    exit()
    
# Winning functions
def iran_win():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("uswins.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    scor = "Your score is " + str(score)
    score_file = open("score.txt", "at")
    score_file.write("\nIran Path Score: " + str(score))
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------iran path fin-------------------------------------------\n")
    score_log.close()
    display_text_animation("""US wins war, succesfully destroyed Iran..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Iran Mode FIN """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    sys.exit()

def mad_dog():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("uswins.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    scor = "Your score is " + str(score)
    score_file = open("score.txt", "at")
    score_file.write("\nIran Path Score: " + str(score))
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------iran path fin-------------------------------------------\n")
    score_log.close()
    display_text_animation("""Mad Dog Victory""",250,100,WHITE,10,DISPLAYSURF)
    display_text_animation("""US wins war, succesfully destroyed Iran..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Iran Mode FIN """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    sys.exit()

def hegem():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("uswins.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    scor = "Your score is " + str(score)
    score_file = open("score.txt", "at")
    score_file.write("\nIran Path Score: " + str(score))
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------iran path fin-------------------------------------------\n")
    score_log.close()
    display_text_animation("""Hegemonic Tyrant Victory""",250,100,WHITE,10,DISPLAYSURF)
    display_text_animation("""US wins war, succesfully destroyed Iran..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Iran Mode FIN """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    sys.exit()

def sad_old():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("uswins.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
        
    def main():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    scor = "Your score is " + str(score)
    score_file = open("score.txt", "at")
    score_file.write("\nIran Path Score: " + str(score))
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------iran path fin-------------------------------------------\n")
    score_log.close()
    display_text_animation("""Sad Old Man Victory""",250,100,WHITE,10,DISPLAYSURF)
    display_text_animation("""US wins war, succesfully destroyed Iran..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Iran Mode FIN """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    sys.exit()

#--------------------------------------- welcome to russia path -------------------------------------------------------------------#
#russia option welcome screen
def russia():
    messagebox.showerror("Error", "GAME UNDER CONSTRUCTION!!")
    exit()
    
#new fucntions go here temporarily
    

    
