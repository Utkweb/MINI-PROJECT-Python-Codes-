from tkinter import *
from tkinter import messagebox
import random

def determine_winner(player_choice):
    choices = ['Rock','Paper','Scissors']
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result ="It's a Tie "
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
    (player_choice == 'Scissors' and computer_choice == 'Paper') or \
    (player_choice == 'Paper' and computer_choice == 'Rock') :
        result = "You win !!"
    else:
        result = "Computer Wins!!!"
    
    result_label.config(text=f"Your choice : {player_choice} || Computer Choice : {computer_choice} \n {result}")

        

root = Tk()
root.title("Rock Paper Scissors")
root.geometry('450x350')

# rock_image = PhotoImage('rock.png')
# scissors_image = PhotoImage('scissors.jpg')
# paper_image = PhotoImage('paper.png')

heading = Label(root,text="Rock Paper Scissors",font=('Arial',20,"bold"))
heading.pack(pady=10)


button_frame = Frame(root)
button_frame.pack(pady = 20)

rock_button = Button(button_frame,text="Rock",font=("Arial",14),width=10,command = lambda : determine_winner('Rock'))
rock_button.grid(row=0,column=0,padx=10)

paper_button = Button(button_frame,text="Paper",font=("Arial",14),width=10,command = lambda : determine_winner('Paper'))
paper_button.grid(row=0,column=1,padx=10)

scissors_button = Button(button_frame,text="Scissors",font=("Arial",14),width=10,command = lambda : determine_winner('Scissors'))
scissors_button.grid(row=0,column=2,padx=10)

result_label = Label(root,text="",font=("Arial",14),fg='blue')
result_label.pack(pady=10)

exit_button = Button(root,text="Exit",font=("Arial",14),width=10,command=root.quit)
exit_button.pack(pady=10)

root.mainloop()