from customtkinter import *
from PIL import Image

class Authorize(CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry('600x450')
        self.resizable(True, False)
        
        font = CTkFont(size=15, weight='bold')
        font1 = CTkFont(size=30, weight='bold')
        font2 = CTkFont(size=25, weight='bold')
        
        img = Image.open(r'C:\Users\user\Documents\Documents\VSCode\python\img_login.jpg')
        image = CTkImage(dark_image=img, size=(300, 400))
        
        label1 = CTkLabel(self, image=image, width=350, height=450, text='', fg_color='grey')
        label1.pack(side=LEFT)
        
        frame = CTkFrame(self, width=250, height=450, fg_color='lightgrey', bg_color='lightgrey')
        frame.pack(side=RIGHT, fill="both", expand=True)
        frame.grid_rowconfigure(0, minsize=20) 
        
        label2 = CTkLabel(frame, width=250, height=50, text='4chan', fg_color='lightblue', font=font1)
        label2.pack(pady=25)
        
        entry = CTkEntry(frame, width=150, height=40, placeholder_text='username', placeholder_text_color="#a7a7a7", fg_color='lightblue', font=font)
        entry.pack(pady=70, padx=10)
        
        btn1 = CTkButton(frame, width=150, height=40, text='Settings', fg_color="#848484", font=font, corner_radius=5, border_width=3, 
                         border_color="#3B3B3B")
        btn1.pack()
        
        btn1 = CTkButton(frame, width=180, height=40, text='Login', fg_color="#D51616", font=font2, corner_radius=10, border_width=4, 
                         border_color="#000000")
        btn1.pack(pady=50, ipady=40)
        
        
        


window = Authorize()
window.mainloop()





























