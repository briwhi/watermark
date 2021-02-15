import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont


class WaterMarker:
    def __init__(self):
        self.window = tk.Tk()
        self.label = tk.Label(text="Watermarker")
        self.label.grid(row=0, column=1)

        # add image button
        self.add_button = tk.Button(text="Add Image", width=25, command=self.add_image)
        self.add_button.grid(row=2, column=0)

        # mark image button
        self.mark_button = tk.Button(text="Add Mark", width=25, command=self.add_mark)
        self.mark_button.grid(row=2, column=1)

        # save image button
        self.save_button = tk.Button(text="Save Image", width=25, command=self.save_image)
        self.save_button.grid(row=2, column=2)
        
        # image label
        self.image_label = tk.Label()
        self.image_label.grid(row=1, column=0, columnspan=3)


        self.window.mainloop()

    def add_image(self):
        file = filedialog.askopenfilename()
        image = Image.open(file)
        width, height = image.size
        image = image.resize((int(width/2), int(height/2)))
        image = ImageTk.PhotoImage(image)
        self.image_label.configure(image=image)
        self.image_label.image = image
        self.image = image
        


    def add_mark(self):
        draw = ImageDraw.Draw(self.image)
        text = "Watermark"
        font = ImageFont.truetype('arial.ttf', 36)
        textwidth, textheight = draw.textsize(text,font)
        margin=10
        x = width - textwidth - margin
        y = height - textwidth - margin - margin
        draw.text((x,y), text, font=font)
        self.image.show()

    def save_image(self):
        print("save image")








marker = WaterMarker()
