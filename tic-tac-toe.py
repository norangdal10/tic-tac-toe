from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"
      CheckWinner(player)
      
      if player == "X" :
            player = "O"
            button["bg"] = "yellow" 
      else :
            player = "X"
            button["bg"] = "lightgreen"

def Win(player):
      global Msg
      Msg = Message(window, text = " " + player + " win!")
      Msg.grid(row = 4, column = 1)
      
      
def CheckWinner(player):
      for j in range(3):
            if list[j]["text"] == list[j+3]["text"] == list[j+6]["text"] == player :
                  Win(player)
            if list[j*3]["text"] == list[j*3+1]["text"] == list[j*3+2]["text"] == player :
                  Win(player)
      if list[0]["text"] == list[4]["text"] == list[8]["text"] == player :
            Win(player)
      if list[2]["text"] == list[4]["text"] == list[6]["text"] == player :
            Win(player)


window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)


window.mainloop()


