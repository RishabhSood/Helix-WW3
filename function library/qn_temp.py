# my_title refers to problem title
# my_x refers to title horizontal positioning
# my_qn refers to problem text (needs to be formated)
# fnt_size refers to font size for the qn text
# ansr refers to the expected input from the user
# func refers to the function to be executed incase the problem is solved correctly

def qn_temp(my_title, my_x, my_qn, fnt_size, ansr, func):
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
                    messagebox.showerror("Error", "Wrong Answer!!, try again")
                    time.sleep(3)
                    window.destroy()
                    
            else:
                window.destroy()
                
    new_btn = Button(window, text=" ",bg="Green", fg="White",font=('Helvetica','10'), command = submitAction)
    new_btn["text"] = "Submit"
    new_btn.place(x = 380, y = 270)
    window.mainloop()