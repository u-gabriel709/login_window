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
        
        img = Image.open(r'img_login.jpg')
        image = CTkImage(dark_image=img, size=(300, 400))
        
        label1 = CTkLabel(self, image=image, width=350, height=450, text='', fg_color='grey')
        label1.pack(side=LEFT)
        
        frame = CTkFrame(self, width=250, height=450, fg_color='lightgrey', bg_color='lightgrey')
        frame.pack(side=RIGHT, fill="both", expand=True)


        def Btn_Login_onclick():
            frame.pack_forget() 
            label1.pack_forget()

            frame1 = CTkFrame(self, width=200, height=450, fg_color="#202020", corner_radius=0)
            frame1.pack(side=LEFT)
            frame2 = CTkFrame(self, width=400, height=450, fg_color="#7d7d7d", corner_radius=0)
            frame2.pack(side=RIGHT)

            msg = CTkEntry(frame2, width=350, height=40, fg_color="#6b6b6b", font=font, 
                           border_color='#000',
                           placeholder_text='Enter your message', placeholder_text_color='#fff')
            msg.pack(side=BOTTOM, pady=50, padx=50)

            btn = CTkButton(frame2, width=30, height=30, text='»', font=font1, fg_color='green')
            btn.pack(side=RIGHT, padx=5, pady=90)

        def Btn_Settings_onclick():
            settings_txt = CTkLabel(frame, font=font, text_color="#500808", 
                                    text='you can\'t click before login')
            settings_txt.place(x=30, y=300)
        

        label2 = CTkLabel(frame, width=250, height=50, text='4chan', fg_color='lightblue', font=font1)
        label2.pack(pady=25)
        
        entry = CTkEntry(frame, width=150, height=40, placeholder_text='Create username', 
                         placeholder_text_color="#a7a7a7", fg_color='lightblue', font=font)
        entry.pack(pady=5, padx=10)

        entry = CTkEntry(frame, width=150, height=40, placeholder_text='Create password', 
                         placeholder_text_color="#a7a7a7", fg_color='lightblue', font=font)
        entry.pack(pady=5, padx=10)
        
        btn1 = CTkButton(frame, width=150, height=40, text='Settings', fg_color="#848484", font=font, 
                        corner_radius=5, border_width=3, border_color="#3B3B3B", command=Btn_Settings_onclick)
        btn1.pack(pady=50)
        
        btn1 = CTkButton(frame, width=180, height=40, text='Login', fg_color="#D51616", font=font2, 
                        corner_radius=10, border_width=4, border_color="#000000", command=Btn_Login_onclick)
        btn1.pack(pady=10)


window = Authorize()
window.mainloop()


