import tkinter 
import customtkinter 
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        youtubeObject = YouTube(ytLink)
        video = youtubeObject.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        video.download()
    except:
        print("The link is invalid")
    print("Download completed !")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk();
app.geometry("720x480")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(app, text='Insert a YouTube link')
title.pack(padx = 10, pady = 10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx = 10, pady = 10)

app.mainloop()