from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Seatify")

def seat_clicked(row, column):
    seat_number = f"{row}-{column}"
    messagebox.showinfo("Seat Selected", f"Seat {seat_number} selected")
    x=seat_states[row,column]
    x.config(state=DISABLED,image=img2)
     
img = PhotoImage(file="vseat.png")
img=img.subsample(10)
img2=PhotoImage(file="oseat.png")
img2=img2.subsample(2)
# Create the button
seat_states={}
k=1
l=1
for i in range(0,20,2):
    l=1
    for j in range(0,20,2):
        s = Button(root, text=f"S{k}-{l}",padx=30,pady=30,image=img, command=lambda a=k, b=l: seat_clicked(a, b))
        temp=Label(root,text=" ")
        temp.grid(row=i+1,column=i+1)
        
        s.grid(row=i,column=j)
        seat_states[k,l]=s
        l+=1
    k+=1    



# Start the GUI event loop
root.mainloop()
