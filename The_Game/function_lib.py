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
def qn_temp(my_title, my_x, my_qn, fnt_size, ansr, func, wrng_func):
    window = tkinter.Tk()
        
    window.title(my_title)
    window.geometry("800x350")
    
    lbl = Label(window,text=my_title,font=('Helvetica','20'), padx = 10, pady = 10)
    lbl.place(x=my_x, y = 10)
    
    qnl = Label(window,text=my_qn, border = 1, relief = "solid", font=('Helvetica',fnt_size), padx = 10, pady = 10)
    qnl.place(x=80, y = 80)
    
    my_ansr = StringVar()
    ansr_entry = Entry(window, textvariable=my_ansr)
    ansr_entry.place(x = 240, y = 220, width = 400, height = 30)
    
    lbl = Label(window,text="Answer: ",font=('Helvetica','14'), padx = 10, pady = 10)
    lbl.place(x=140, y = 213)
    
    def submitAction():
            myVar = messagebox.askquestion("Submit", "Do you wish to submit? ")
            if myVar == 'yes':
                the_ansr = my_ansr.get()
                if the_ansr == ansr:
                    messagebox.showinfo("Correct!!", "You answered correct!")
                    time.sleep(1)
                    window.destroy()
                    func()
                else:
                    wrng_func()
                
    new_btn = Button(window, text=" ",bg="Green", fg="White",font=('Helvetica','10'), command = submitAction)
    new_btn["text"] = "Submit"
    new_btn.place(x = 380, y = 270)
    window.mainloop()

#1. (b)
def qn_temp_no_opt(my_title, my_x, my_qn, fnt_size, ansr, func, wrng_func):
    window = tkinter.Tk()
        
    window.title(my_title)
    window.geometry("800x350")
    
    lbl = Label(window,text=my_title,font=('Helvetica','20'), padx = 10, pady = 10)
    lbl.place(x=my_x, y = 10)
    
    qnl = Label(window,text=my_qn, border = 1, relief = "solid", font=('Helvetica',fnt_size), padx = 10, pady = 10)
    qnl.place(x=80, y = 80)
    
    my_ansr = StringVar()
    ansr_entry = Entry(window, textvariable=my_ansr)
    ansr_entry.place(x = 240, y = 220, width = 400, height = 30)
    
    lbl = Label(window,text="Answer: ",font=('Helvetica','14'), padx = 10, pady = 10)
    lbl.place(x=140, y = 213)
    
    def submitAction():
            myVar = messagebox.askquestion("Submit", "Do you wish to submit? ")
            if myVar == 'yes':
                the_ansr = my_ansr.get()
                if the_ansr == ansr:
                    messagebox.showinfo("Correct!!", "You answered correct!")
                    time.sleep(1)
                    window.destroy()
                    func()
                else:
                    window.destroy()
                    wrng_func()
                
    new_btn = Button(window, text=" ",bg="Green", fg="White",font=('Helvetica','10'), command = submitAction)
    new_btn["text"] = "Submit"
    new_btn.place(x = 380, y = 270)
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
        button(opt1,420,220,110,50,white,bright_red,func1)
        button(opt2,420,320,140,50,white,bright_red,func2)
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
    
    display_text_animation("""CCS PRESENTS""", 250, 100, (0,255,0), 30)
    display_text_animation("""WORLD WAR III """, 250, 100, (0,0,255), 30)
    display_text_animation("""You're Donald Trump, President of the US. """, 250, 100, WHITE, 10)
    display_text_animation(""" Your country is at odds with Iran, China, and Russia """, 250, 100, WHITE, 10)
    display_text_animation(""" choose the path forward wisely. """, 250, 100, WHITE, 10)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    display_text_animation(""" Loading ... """, 250, 100, RED, 20)
    pygame.mixer.music.stop()
    qn_temp("Somewhere in Iran", 280, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "202849", count_opts, default_wrong)

# options screen
def count_opts():
    three_options("Choose Country to initiate war with"
            , 470, "Iran", iran, "China", china, "Russia", russia)
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
    qn_temp("Somewhere in Iran", 280, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "0", iran_chck_one, default_wrong)
    
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
    display_text_animation("""Answer the next question to continue...""", 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    qn_temp("Somewhere in Iran", 280, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "0", iran_fght_back, default_wrong)
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
    
    display_text_animation("""Iran fights back!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""In order to launch a devastating attack ...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer the next problem correctly """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp_no_opt("One Chance", 280, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "0", iran_win, iran_loose)
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
    qn_temp("Somewhere in Iran", 280, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "0", iran_fght_back, default_wrong)
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
    qn_temp_no_opt("One Chance", 280, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "0", iran_red_succ, iran_solo_inv)
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
    qn_temp_no_opt("One Chance", 280, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "0", iran_stealth, iran_solo_inv)
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
    
    qn_temp_no_opt("One Chance", 280, 
            """1,150,000 people stand in a circle. One of them is an undercover agent. There is a sword in 
            the hand of the 1st person, he kills the 2nd person and passes on the sword to the third, 
            who kills the fourth and gives the sword to the 5th, this goes on until one person is left. 
            At what position does the spy stand to survive?""", 10, "0", iran_win, iran_win)
    exit()
    
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
    
    display_text_animation("""US wins war, succesfully destroyed Iran..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Your score is 000""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Iran Mode FIN """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    sys.exit()

def iran_loose():
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
    
    display_text_animation("""US looses war.. Retreating troops""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Your score is 000""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Iran Mode FIN """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    sys.exit()
#--------------------------------------- welcome to china path -------------------------------------------------------------------#
#china option welcome screen
def china():
    messagebox.showerror("Error", "GAME UNDER CONSTRUCTION!!")
    exit()

#--------------------------------------- welcome to russia path -------------------------------------------------------------------#
#russia option welcome screen
def russia():
    messagebox.showerror("Error", "GAME UNDER CONSTRUCTION!!")
    exit()
    
