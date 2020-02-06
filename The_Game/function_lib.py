#this file contains all the functions
import tkinter
from tkinter import Button
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import messagebox
import time
import pygame
from datetime import datetime
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
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            score_file.write(current_time)
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
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            score_file.write(current_time)
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
    
        smallText = pygame.font.Font('cs_regular.ttf',20)
        textSurf, textRect = text_objects(msg, smallText, (0,0,0))
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)
    
    while(dead==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
    
        screen.blit(background_image, [0, 0])
        largeText = pygame.font.Font('cs_regular.ttf',40)
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
    
        smallText = pygame.font.Font('cs_regular.ttf',20)
        textSurf, textRect = text_objects(msg, smallText, (0,0,0))
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        screen.blit(textSurf, textRect)
    
    while(dead==False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
    
        screen.blit(background_image, [0, 0])
        largeText = pygame.font.Font('cs_regular.ttf',40)
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
            font=pygame.font.Font('thefont.ttf',mysize)
            text_surface = font.render(text, True, mycolor)
            text_rect = text_surface.get_rect()
            text_rect.center = (pos1, pos2)
            my_surf.blit(text_surface, text_rect)
            pygame.display.update()
            pygame.event.get()
            pygame.time.wait(100)
        time.sleep(2)
        

def userinfo():
  window = tkinter.Tk()

  window.title("Enter User Details")
  window.geometry("800x370")
  
  lbl = Label(window,text="Login",font=('Helvetica','20'), padx = 10, pady = 10)
  lbl.place(x=370, y = 60)
    
  my_team = StringVar()
  team_entry = Entry(window, textvariable=my_team)
  team_entry.place(x = 280, y = 220-80, width = 360, height = 30)

  lbl = Label(window,text="Team Name: ",font=('Helvetica','14'), padx = 10, pady = 10)
  lbl.place(x=140, y = 213-80)
  
  my_plyo = StringVar()
  plyo_entry = Entry(window, textvariable=my_plyo)
  plyo_entry.place(x = 280, y = 220-40, width = 360, height = 30)

  lbl = Label(window,text="Player 1: ",font=('Helvetica','14'), padx = 10, pady = 10)
  lbl.place(x=140, y = 213-40)
  
  my_plyt = StringVar()
  plyt_entry = Entry(window, textvariable=my_plyt)
  plyt_entry.place(x = 280, y = 220, width = 360, height = 30)

  lbl = Label(window,text="Player 2: ",font=('Helvetica','14'), padx = 10, pady = 10)
  lbl.place(x=140, y = 213)

  def submitAction():
    one = my_team.get()
    two = my_plyo.get()
    three = my_plyt.get()
    if one == "":
        messagebox.showinfo("Error!", "Please Enter Team Name!!")

    else:
        usr_data = open("usr_details.txt", "at")
        usr_data.write("Team Name:" + one + "\n")
        usr_data.write("PLayer 1 Name:" + two + "\n")
        usr_data.write("PLayer 2 Name:" + three + "\n")
        usr_data.close()
        window.destroy()
        load()
        
        
  new_btn = Button(window, text=" ",bg="Green", fg="White",font=('Helvetica','10'), command = submitAction)
  new_btn["text"] = "LOGIN"
  new_btn.place(x = 390 , y = 280 )
  
  window.mainloop()
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
            font=pygame.font.Font('thefont.ttf',mysize)
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
                    
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n------------------------------------------------------------------------------------------\n")
    score_log.write("Welcome to Path Iran\n")
    score_log.write("------------------------------------------------------------------------------------------\n\n")
    score_log.close()
    
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
            
            """, 10, "26241", sad_old, dumb, "900x540", 60, 220, 500)
    
    exit()
    
def dumb():
    exit
    
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
    
    display_text_animation("""To hell with reason, to hell with the internet,""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" ..guerilla warfare, no red blooded american ..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""will bow to nerds at computers across the world from them...  """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" Answer next problem to continue... """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    
    qn_temp("To hell with Reason! (300 pts)", 220, 
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
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------iran path fin-------------------------------------------\n")
    score_log.close()
    display_text_animation("""US wins war, succesfully destroyed Iran..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER """, 250, 100, WHITE, 10, DISPLAYSURF)
    
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
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------iran path fin-------------------------------------------\n")
    score_log.close()
    display_text_animation("""Mad Dog Victory""",250,100,WHITE,10,DISPLAYSURF)
    display_text_animation("""US wins war, succesfully destroyed Iran..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER """, 250, 100, WHITE, 10, DISPLAYSURF)
    
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
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------iran path fin-------------------------------------------\n")
    score_log.close()
    display_text_animation("""Hegemonic Tyrant Victory""",250,100,WHITE,10,DISPLAYSURF)
    display_text_animation("""US wins war, succesfully destroyed Iran..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    sys.exit()

def omaewa():
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
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------iran path fin-------------------------------------------\n")
    score_log.close()
    display_text_animation("""Teleports behind you, Omae Wa Mou Shindeiru""",250,100,WHITE,10,DISPLAYSURF)
    display_text_animation("""You are decapitated""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER """, 250, 100, WHITE, 10, DISPLAYSURF)
    
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
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------iran path fin-------------------------------------------\n")
    score_log.close()
    display_text_animation("""Sad Old Man Victory""",250,100,WHITE,10,DISPLAYSURF)
    display_text_animation("""US wins war, succesfully destroyed Iran..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER """, 250, 100, WHITE, 10, DISPLAYSURF)
    
    pygame.mixer.music.stop()
    sys.exit()

#--------------------------------------- welcome to russia path -------------------------------------------------------------------#
#russia option welcome screen
def russia():
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
                    
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n------------------------------------------------------------------------------------------\n")
    score_log.write("Welcome to Path Russia")
    score_log.write("------------------------------------------------------------------------------------------\n\n")
    score_log.close()
    
    display_text_animation("""Russia starts arms buildup... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""... along its European borders""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Leaders in your country have gathered """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Make a decision on what to do ... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""...with the arms buildup """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()

    two_options("Make a decision:"
            , 470, "No Panic", russia_calm, "War", russia_war_prev)
    exit()

def russia_calm():
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
    
    display_text_animation("""Defend your decision by answering the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp("Is all fine, no need to panic!! (150 pts)", 200, 
            """You try to convince the room that everything is under control.
            	To prepare yourself for logical arguments you decide to practice with some quick maths:
            	A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost 
                unimaginably large: 
                    
                    one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
                    
            	Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?    
            """, 10, "972", russia_calm_cont, default_wrong, "840x400", 20, 60, 150)

    
def russia_calm_cont():
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
    
    display_text_animation("""Some of the more noconfrontational personalities agree """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""but an old mainframe in the back""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""makes allegations of incompetence, ...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""... or worse, COLLUSION.  """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Defend yourself by answering the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp("Dratted Computers (150 pts)", 270, 
            """To convince this computer with more brains than the rest of the gathering combined you must 
            fool it with loops in logic that it cannot grasp.
        	The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
        
        	1! + 4! + 5! = 1 + 24 + 120 = 145
        
        	Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
            it turns out that there are only three such loops that exist:
        
        	169 → 363601 → 1454 → 169
        	871 → 45361 → 871
        	872 → 45362 → 872
        
        	It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
        
        	69 → 363600 → 1454 → 169 → 363601 (→ 1454)
        	78 → 45360 → 871 → 45361 (→ 871)
        	540 → 145 (→ 145)
        
        	Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a 
            starting number below one million is sixty terms.
        
        	How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?  
            """, 10, "402", russia_wink, russia_anyhow, "840x600", 20, 280, 150)
    
    exit()

def russia_wink():
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

    display_text_animation("""Russia attacks in the night!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Unable to locate damage...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You decide to hell with AI overlords""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Time to Attack!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    russia_war()
    exit()
    
def russia_anyhow():
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
    

    display_text_animation("""You stumble through your explanation but... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Mainframe tries to press his advantage...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Other shout over him, calling him a worrywart..""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You are asked to simply get this sorted with...""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    russia_wink()
    exit()
    
def russia_war_prev():
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
    
    display_text_animation("""You try to convince the gathering of the importance of war ...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Continue by answering the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    

    qn_temp(" We must declare war... Yesterday! (100 pts)", 140, 
                """You try to convince the gathering that the best course of action is to start this battle more 
                awaited than Cleganebowl.
            	War is war no matter how you phrase it, but selectively forming your arguments might help with some 
                of the more pacifist types here.
            	
            	There are exactly ten ways of selecting three from five, 12345:
            	123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
                
            	In we, use combinatorics the notation, 5C3=10
            
            	In general, (nCr)=n! * r! / (n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1
            	It is not until n=23, that a value exceeds one-million: 
                    (2310)=1144066
            	
            	How many, not necessarily distinct, values of (nr)
            	for 1≤n≤100, are greater than one-million?
                """, 10, "4075",russia_war, default_wrong, "840x500", 20, 180, 100)
    exit()
    
def russia_war():
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
    
    display_text_animation("""You choose to meet russia head on... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Choose where to attack...""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    two_options("Choose Attack Mode"
            , 470, "Cyber War", russia_cyber, "Winter War", russia_winter)
    
    exit()

def russia_cyber():
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
    
    display_text_animation("""You decide to attack Russian Digital infrastructure ...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Obtain Electrical blackouts, failure of military equipment and""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""National Security secrets in order to cripple them...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Continue by answering the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp(" Numbers War (140 pts)", 200, 
            """The Russian digital network works on the basis of powers of 2, to attack it, you must use
            higher powers, as bigger is better.
	
        	The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 
            134217728=89, is a ninth power.
            
        	How many n-digit positive integers exist which are also an nth power?
            """, 10, "49",russia_war_on, default_wrong, "700x380", -60, 40, 140)
    

def russia_winter():
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
    
    display_text_animation("""You have decide that the fire in your hearts can brave the...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""... russian cold and ask for Nato Support for the same.""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Convince Nato of your war being just... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp_no_opt(" Our Glorious Allies! (500 pts)", 220, 
            """ You try to Convince Nato of your war being Just!
            	You plan to go about this using a roundabout analogy about how what you're doing truly is the 
                most sensible thing to do.
            	
            	Five pirates have obtained 100 gold coins and have to divide up the loot. The pirates are all 
                extremely intelligent, treacherous and selfish (especially the captain).
            
            	The captain always proposes a distribution of the loot. All pirates vote on the proposal, and if 
                half the crew or more go "Aye", the loot is divided as proposed, as no pirate would be willing to 
                take on the captain without superior force on their side.
            
            	If the captain fails to obtain support of at least half his crew (which includes himself), he 
                faces a mutiny, and all pirates will turn against him and make him walk the plank. The pirates 
                start over again with the next senior pirate as captain.
            
            	What is the maximum number of coins the captain can keep without risking his life?
            """, 10, "98",trump_rogue, allies_reject, "800x500", 20, 180, 500)
    
    exit()
    
def allies_reject():
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
    
    display_text_animation("""Your offer gets rejected...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Show them that you have the truth as your ally!! """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    russia_war_on()
    exit()
    
def russia_war_on():
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
    
    display_text_animation("""War is on!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Continue by solving the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp(" War is on! (120 pts)", 230, 
            """ You must deal with logistics issues, you have supplies for a million troops for protracted war 
            but you need to support 2 million.
	
        	Let a0, a1, a2, ... be an integer sequence defined by:
        
        		a0 = 1;
        		for n ≥ 1, an is the sum of the digits of all preceding terms.
        
        	The sequence starts with 1, 1, 2, 4, 8, 16, 23, 28, 38, 49, ...
        	You are given a10^6 = 31054319.
        
        	Find a(2 x 10^6)
            """, 10, "65514710", russia_the_spy, default_wrong, "700x450", -40, 120, 120)
    
    exit()

def russia_the_spy():
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

    display_text_animation("""Bam!!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""@$%×#$%#@%%%#@#$!!! """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Your memory of your training as a ... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Russian spy returns to you ...""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    two_options("Go back to russia and sell your Country?"
            , 470, "Yes", spy_returns, "No", trump_rogue)
    
    exit()

def trump_rogue():
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

    display_text_animation("""You choose to return to Moscow your own way...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Blazing Guns and exploding bombs!! """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Continue by answering the following problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp(" Pussy Riot (110 pts)", 280, 
            """Prime your weapons for the final charge on the Kremlin.
	
        	The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne 
            prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, 
            of the form 2p−1, have been found which contain more digits.
        
        	However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 
                28433×27830457+1.
        
        	Find the last ten digits of this prime number.
            """, 10, "8739992577",russia_destroyed, default_wrong, "800x430", 20, 100, 110)
    exit()

def russia_destroyed():
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
    
    display_text_animation("""Moscow's actual war readiness left much to be desired...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You have destroyed Russia!!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    two_options("Choose a path forward:"
            , 470, "Unify", russia_unify, "Birth of Nations", birth_of_nations)
    exit()

def russia_unify():
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

    display_text_animation("""You decide to conjoin the Bear of the North and the Eagle of Oil""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""under your guidance.. as the senate is about to protest...""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    china_war()
    exit()

def birth_of_nations():
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

    display_text_animation("""You declare plans for the division of Russia into sovereign nations...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""to be overseen by a new body under the UN...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""your broadcast is halted to report that...""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    china_war()
    exit()
    
def spy_returns():
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
    
    display_text_animation("""You ride your plane to Moscow, as you ditch your country""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Continue by solving the next problem...""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp(" Set it and forget it (110 pts)", 230, 
            """You do not even turn to look as the White House, the symbol of the Presidency, 
            the United States government, and the American people, explodes in flames as you board your 
            ex-Presidential Jet to Moscow.
	
        	Now, you must dodge the jets that'll soon bar your way, you must become one with the wind, and with 
            the planes that once would've protected you, mirroring them but passing through.
        	A palindromic number reads the same both ways. The largest palindrome made from the product of 
            two 2-digit numbers is 9009 = 91 × 99.
        
        	Find the largest palindrome made from the product of two 3-digit numbers.
            """, 10, "906609", spy_cont, default_wrong, "800x430", 20, 100, 110)
    
    exit()

def spy_cont():
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
    
    display_text_animation("""Now that you have chosen to return, you try to sell...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""your handwritten plans to destroy The United States... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""which no other sane human can decode... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Succeed by solving the next problem...""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp_no_opt(" Most Powerful man for Sale (150 pts)", 200, 
            """You try to sell your importance to the Kremlin, chaining yourself to the Russian Cause, 
        	with handwritten notes detailing chains of supply and what not that'll spell america's doom.
        
        	A number chain is created by continuously adding the square of the digits in a number to form a 
            new number until it has been seen before.
        
        	For example,
        
        	44 → 32 → 13 → 10 → 1 → 1
        	85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
        
        	Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing 
            is that EVERY starting number will eventually arrive at 1 or 89.
        
        	How many starting numbers below one million will arrive at 89?
            """, 10, "856929", trump_returns, spy_death, "820x480", 20, 160, 150)
    exit()

def spy_death():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("chinatheme.mp3")
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
    score_file.write("\nRussia Path Score: " + str(score))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------russia path fin-------------------------------------------\n")
    score_log.close()
    
    display_text_animation("""Your plans were rejected by the Russian govt.""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""you are sent to live in siberia for the rest of your life... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""you die nameless!!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    sys.exit()

def trump_returns():
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
    
    display_text_animation("""With your military and tactical genius...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""you are entrusted with destroying US in the easiest way... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""America collapses within a day... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Your popularity is at it's peak!!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    two_options("Press your claim over Russia?"
            , 470, "Yes", trump_senate, "No", trump_expendable)
    
    exit()

def trump_senate():
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
    
    display_text_animation("""You declare yourself emperor of Russia!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""the troops will follow you, as you prepare to head back to moscow""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""The kremlin sens assasins after you, as your work is done... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""the news reaches you, the Kremlin is done for...""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    china_war()
    exit()

def trump_expendable():
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
    
    display_text_animation("""Your work is done...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""The kremlin has sent assasins to finish you off... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Defend yourself by answering the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp_no_opt(" Expendable (120 pts)", 280, 
            """ Your work finished, the kremlin sends assassins after you, defend yourself.

        	It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, 
            but in a different order.
        
        	Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
            """, 10, "142857",trump_rises, trump_death, "820x360", 20, 20, 120)
    exit()

def trump_death():
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
    
    scor = "Your score is " + str(score)
    score_file = open("score.txt", "at")
    score_file.write("\nRussia Path Score: " + str(score))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------russia path fin-------------------------------------------\n")
    score_log.close()
    
    display_text_animation("""You were murdered by the assassins...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""The earth lost it's last hope... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    sys.exit()
    exit()
    
def trump_rises():
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
    
    display_text_animation("""You destroy all the assassins with Krav Maga Netanhayu taught you""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""The Kremlin blows up...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You are the last hope of Russia now...""", 250, 100, WHITE, 10, DISPLAYSURF)

    china_war()
    exit()
    
def china_war():
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
    
    display_text_animation("""A video has surfaced...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Chinese President Xi Jinping has declared war!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Your constant interference in other countries has caused this...""", 250, 100, WHITE, 10, DISPLAYSURF)

    two_options("Choose the path forward..."
            , 470, "Undercover Agent", trump_solo, "Fire with Fire", china_attack)
    
    pygame.mixer.music.stop()
    exit()

def china_attack():
    qn_temp(" The ***** Wars (600 pts)", 290, 
            """ You will fight fire with fire, armies with armies, you will not balk, and at the end of this, 
            YOU   WILL   BE   THE   VICTOR!
            
        	You've ascertained that the route to victory over the chinese is through duality, of the wes and the east, 
            of russian and american, of cold and oil, and thus, the number 2.
        	The square root of 2 can be expressed as an infinite continued fraction. 
            sqrt(2) =  1 + (1 / (2 + 1 / (2 + 1 / (2 + 1.....
            
        	Expanding this for the first three iterations:
        	1 + 1/2 = 3/2 = 1.5
        	1 + 1/(2 + 1/2) = 7/5 = 1.4
        	1 + 1/(2 + 1/(2 + 1/2) = 17/12 = 1.4166...
            
        	The eighth expansions is 1393/985, which is the first exxpansion where the number of digits in the numerator 
            is more than that in the denominator.
            
        	In the first one-thousand expansions, how many fractions contain a numerator with 
            more digits than the denominator?

            
            """, 10, "153",chin_att_fw, default_wrong, "860x580", 40, 240, 600)
    exit()
    
def chin_att_fw():
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

    display_text_animation("""You receive intel of your armies being destroyed...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""by fiendish armies which feel no pain...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""there is now only one option, will you make the choice??""", 250, 100, WHITE, 10, DISPLAYSURF)

    
    two_options("Choose the path forward..."
            , 470, "Investigate", trump_investigate, "Nuclear Attack", china_nuclear)
    
    pygame.mixer.music.stop()
    exit()

def china_nuclear():
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

    display_text_animation("""The reptilians have invaded this far...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""you must use the last option...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" give up your life, blow up russia and all of asia!!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer the next problem to succeed""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp_no_opt("The Nuclear Option (350 pts)", 210, 
            """ The reptilians have invaded this far, you must use the last option, give up your life, blow up 
            russia and all of asia, for the future of the Earth!
        	To do this, the only prerequisite is knowledge, knowledge of this building and of nukes.
        	
        	By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains 
            eighteen rectangles.
            
        	Although there exists no rectangular grid that contains exactly two million rectangles, 
            find the area of the grid with the nearest solution.

            """, 10, "2772",nuclear_succeed, nuclear_fail, "740x420", -20, 90, 350)

    exit()

def nuclear_succeed():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("chinatheme.mp3")
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
    score_file.write("\nRussia Path Score: " + str(score))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------russia path fin-------------------------------------------\n")
    score_log.close()

    display_text_animation("""Praises of your sacrifise are forever sung!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You die but rescue humanity""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You Win!""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    sys.exit()
    
def nuclear_fail():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("chinatheme.mp3")
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
    score_file.write("\nRussia Path Score: " + str(score))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------russia path fin-------------------------------------------\n")
    score_log.close()

    display_text_animation("""Your efforts go in vain...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You have failed...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    sys.exit()
    
def trump_investigate():
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

    display_text_animation("""You send your spies to find the cause of your losses""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer the next problem to continue""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp(" Investigate (400 pts)", 320, 
            """ You send your elite spies to find out the cause for your losses.
            ever, even they were spooked by what they saw, use your powers as prime to return them to a functional state.
            Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive 
            numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
            are all less than nine and relatively prime to nine, φ(9)=6.
             
            number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

            Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

	        Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and 
            the ratio n/φ(n) produces a minimum.

            
            """, 10, "55374",shock_truth, default_wrong, "860x480", 40, 140, 400)
    
    exit()

def shock_truth():
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

    display_text_animation("""You receive reports of rituals to strange gods and sermon...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""which brainwash the masses into brainless husks ready for war""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""there is only one option""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    china_nuclear()
    exit()
    
def trump_solo():
    
    qn_temp(" Solo, A Trump Story (160 pts)", 230, 
            """ No one else can be trusted, you must accomplish this on your own, infiltrate China.
        	Chinese Checkposts are arrayed in the form of Pascal's Triangle, with 51 rows, with the passable 
            ones being those whose number in the triangle is square-free, 
            i.e., not divisible by the square of any prime.
            
        	Find the sum of the distinct square free numbers in these 51 rows.
            """, 10, "34029210557338",solo_opts, default_wrong, "800x360", 20, 20, 160)
    
    exit()

def solo_opts():
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
    
    display_text_animation("""Walking through rural china, you pass...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""empty towns and armies of dazed peasants led by snakelike men""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Rumors of the Forbidden City resound in the air... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    two_options("Fight a Combat/visit the Forbidden City"
            , 470, "Combat", trump_combat, "Visit", the_forbidden_city)
    exit()
    
def trump_combat():
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

    display_text_animation("""Answer the question that follows, to win the combat...""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp_no_opt(" Trump Power!! (240 pts)", 280, 
            """ You Engage a battalion in combat, Fight!!!
        	Divine authority guides your arm and you realise that the secret to smoting the enemy is held in 
            Budget-Lychrel numbers.
            
        	If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
        	Not all numbers produce palindromes so quickly. For example,
        
        	349 + 943 = 1292,
        	1292 + 2921 = 4213
        	4213 + 3124 = 7337
        
        	That is, 349 took three iterations to arrive at a palindrome.
        	It has long been thought by sages that some numbers never arrive at a palindrome, since 50 is a big number,
            numbers that do not fall in line(become a palindrome) in 50
        	iterations are to be deemed Budget-Lychrel numbers and are the secret to victory.
            
            
        	How many Budget-Lychrel Numbers are there below ten-thousand?
            """, 10, "249",one_man_army, combat_death, "860x550", 40, 210, 240)
    
    exit()

def combat_death():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("chinatheme.mp3")
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
    score_file.write("\nRussia Path Score: " + str(score))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------russia path fin-------------------------------------------\n")
    score_log.close()

    display_text_animation("""Hordes tear into your flesh...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You die....""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    sys.exit()

def one_man_army():
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

    display_text_animation("""With your almost divine martial prowess...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(""" you manage to defeat them and find out that...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""the inhuman chinese leadership has brainwashed the masses""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""this is a repltilian ploy for world domination!!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    the_forbidden_city()
    exit()
    
def the_forbidden_city():
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

    display_text_animation("""You infiltrate the forbidden city and see...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""dead people and reptilian soldiers everywhere... """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Fight your way into the inner Sanctum """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Answer the next problem... """, 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp(" The Forbidden City (300 pts)", 280, 
            """ You infiltrate the forbidden city and see dead people and reptilian soldiers everywhere, 
            fight your way into the inner sanctum.
        	To reach the inner sanctum through this carnage, you must remember the way of bounce(3D) and achieve 
            maximum bounce!
        	Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; 
            for example, 134468.
        	
        	Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; 
            for example, 66420.
        
        	We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; 
            for example, 155349.
        
        	Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below 
            one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first 
            reaches 50% is 538.
        
        	Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion 
            of bouncy numbers is equal to 90%.
        
        	Find the least number for which the proportion of bouncy numbers is exactly 99%.
            """, 10, "1587000",el_fin, default_wrong, "860x590", 40, 270, 300)

    exit()
    
def el_fin():
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

    display_text_animation("""You enter the inner sanctum, a horrific sight awaits!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Xi Jinping sheds his humanoid skin, and then his ursine skin!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""A half lizard abomination stands before you!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""ahhh Donald.. i knew you would come!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""answer the next question to fight him!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    
    qn_temp_no_opt(" Duel of the fates (800 pts)", 260, 
            """ Cut off the Head and the Snake Collapses, kill Xi to save the world!
        	Defeat the other prime, and be the Hero, prime exponential!
        	The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power 
            is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
        
        	28 = 22 + 23 + 24
        	33 = 32 + 23 + 24
        	49 = 52 + 23 + 24
        	47 = 22 + 33 + 24
        
        	How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, 
            and prime fourth power?
            
            """, 10, "1097343",highlander, earth_destroyed, "820x480", 25, 140, 800)
    exit()
    
def highlander():    
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("chinatheme.mp3")
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
    score_file.write("\nRussia Path Score: " + str(score))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------russia path fin-------------------------------------------\n")
    score_log.close()

    display_text_animation("""In a battle for the ages, you decapitate his head...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""You've won, earth is saved, rejoice, Hero!""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""YOU WIN!!""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    sys.exit()

def earth_destroyed():
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 200
    
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.mixer.music.load("chinatheme.mp3")
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
    score_file.write("\nRussia Path Score: " + str(score))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    score_file.write(current_time)
    score_file.close()
    score_log = open("ww3_log.txt", "at")
    score_log.write("\n+---------------------------------russia path fin-------------------------------------------\n")
    score_log.close()

    display_text_animation("""As you cut off Xi's head with your greatsword...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""two more heads pop up and spew fire at you!!! """, 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""your outer skin burns off as Xi decapitates you...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""the reptilian revolution succeeds...""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""Earth devolves into a wasteland.""", 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation(scor , 250, 100, WHITE, 10, DISPLAYSURF)
    display_text_animation("""GAME OVER""", 250, 100, WHITE, 10, DISPLAYSURF)
    pygame.mixer.music.stop()
    sys.exit()
    

