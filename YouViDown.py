import pytube.exceptions
from pytube import YouTube
from tkinter import *
from tkinter import font
from tkinter import filedialog

window = Tk()
window.title("YouViDown")
window_set = Canvas(window, bg='#282b30', height=450, width=450, highlightthickness=0)
window.resizable(False, False)
window_set.pack()

title_font = font.Font(underline=1, family="verdana", size="20")
title = Label(window, text="YouViDown",font=title_font, bg='#282b30', fg='#FFFFFF').place(relx="0.33", rely="0.05")

link_title_font = font.Font(family="verdana", size="15")
link_title = Label(window, text="Video Link",font=link_title_font, bg='#282b30', fg='#FFFFFF').place(relx="0.37", rely="0.18")

link_text = Entry(window, width=50)
link_text.place(relx=0.15, rely=0.27)

t_title_font = font.Font(family="verdana", size="15", underline=1)
t_title = Label(window, font = t_title_font, bg='#282b30', fg='#FFFFFF')
t_title.place(relx=0.37, rely=0.58)

video_title = Label(window, bg='#282b30', fg='#FFFFFF',wraplength = 200)
video_title.place(relx=0.28, rely=0.65)

wrong_L = Label(window, bg='#282b30', fg='#FF0000', font="7")
wrong_L.place(relx=0.36, rely=0.60)

support_L = Label(window, bg='#282b30', fg='#FF0000', font="7")
support_L.place(relx=0.20, rely=0.60)

none_L = Label(window, bg='#282b30', fg='#FF0000', font="7")
none_L.place(relx=0.36, rely=0.60)

folder_dir=""
link=""

def check():
    global link
    link = link_text.get()


    print(link)

    try:
        yt = YouTube(link)
        print(f"Video Title: {yt.title}")
        wrong_L.lower()
        support_L.lower()
        none_L.lower()

        video_title.lift()
        t_title.lift()

        video_title["text"] = yt.title
        t_title["text"] = "Video Title"
    except:
        if (link == ""):
            video_title.lower()
            t_title.lower()
            wrong_L.lower()
            support_L.lower()
            none_L.lift()
            none_L["text"] = "URL not specified!"
            print("URL not specified!")

        else:
            video_title.lower()
            t_title.lower()
            support_L.lower()
            none_L.lower()
            wrong_L.lift()

            wrong_L["text"] = "Wrong URL Link!"
            print("Wrong URL Link!")


video_resolution = [
    "360p",
    "720p"
]
resolution = StringVar(window)
resolution.set(video_resolution[0])

opt = OptionMenu(window, resolution, *video_resolution)
opt.config(width=4,font=('Helvetica', 9))
opt.place(relx=0.416, rely=0.50)


def browse():
    global folder_dir
    folder_dir = filedialog.askdirectory()
    print(folder_dir)


def download():
    global link
    global folder_dir


    yt = YouTube(link)
    mp4s = yt.streams.filter(file_extension="mp4", progressive=True)


    res = resolution.get()
    #print(res)
    try:

        if (res == "360p"):
            choice = int("0")
            mp4s[choice].download(folder_dir)
            support_L.lower()

        if (res == "720p"):
            choice = int("1")
            mp4s[choice].download(folder_dir)
            support_L.lower()


    except IndexError:
        #print("The video does not support this quality!")
        t_title.lower()
        video_title.lower()
        wrong_L.lower()

        support_L.lift()
        support_L["text"] = "The video does not support this quality!"


check_button = Button(window, text="Check", command=check).place(relx=0.45, rely=0.35)
browse_button = Button(window, text="Browse", font="5", command=browse).place(relx=0.30, rely=0.9)
download_button = Button(window, text="Download", font="5",command=download).place(relx=0.50, rely=0.9)


window.mainloop()
