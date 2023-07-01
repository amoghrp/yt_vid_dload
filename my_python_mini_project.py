# SIMPLE YOUTUBE VIDEO DOWNLOADER PROJECT USING PYTHON



from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil

# Functions
def select_path():
    # allows users to select the path from the explorer 
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title('Downloading Please Wait....')
    # Download video heart of program
    mp4_video =YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # code to move that video to required directory
    shutil.move(mp4_video,user_path)
    screen.title('Success !!!')


    

screen = Tk()
title = screen.title('YouTube Video Download')
canvas = Canvas(screen,width = 500, height = 500) # here I can edit 
canvas.pack()


#image logo
logo_img = PhotoImage(file='yt.png')
#resize
logo_img = logo_img.subsample(2,2) # I can remove this line if I want big size image 

canvas.create_image(250,80,image=logo_img)   # here I can edit


#link field
link_field = Entry(screen,width=50)
link_label = Label(screen, text="Enter video Link !!",font=('Verdana',15)) # here font

# here we can select path for the file
path_label = Label(screen,text = "select location for file",font = ("Segoe Print",15))
select_btn = Button(screen,text = "Select",command = select_path) # here method call 
# here add to window
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_btn)




# add widgets to window
canvas.create_window(250,170,window=link_label)
canvas.create_window(250,220,window=link_field)



#download buttons section
download_btn = Button(screen,text="DOWNLOAD",command=download_file)
# adding to canvas process
canvas.create_window(250,390,window =download_btn)



screen.mainloop()
