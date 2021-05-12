from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
root=Tk()

root.geometry("500x610")

root.title("YouTube Video Downloader")

root.maxsize(500,610)

def Browse():
    try:
        download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH")
        download_Path.set(download_Directory)
    except:
        pass

def Download():
    try:
        Youtube_link = video_Link.get()
        download_Folder = download_Path.get()
        getVideo = YouTube(Youtube_link)
        videoStream = getVideo.streams.first()
        videoStream.download(download_Folder)
        messagebox.showinfo("SUCCESSFUL",
                            "DOWNLOADED AND SAVED IN\n"
                            + download_Folder)
    except:
        pass

video_Link = StringVar()
download_Path = StringVar()


photo=PhotoImage(file="dummy/youtube.png")
label_1=Label(image=photo)
label_1.pack(pady=40)

frame1=Frame(root,bg="black",relief=SUNKEN,borderwidth=5)
label1=Label(frame1,text="Video Link:",font=("lucida 12 italic bold"),bg="black",fg="white").pack(side=LEFT,ipadx=5,padx=5,ipady=10,pady=10)
screen1 = Entry(frame1, textvar=video_Link, font=("lucida 12 italic"), bg='red', borderwidth=6, relief=SUNKEN)
screen1.pack(ipady=10, padx=10, pady=10,ipadx=40)
frame1.pack(pady=20,fill=X,padx=10)


frame2=Frame(root,bg="black",relief=SUNKEN,borderwidth=5)
label2=Label(frame2,text="Destination:",font=("lucida 12 italic bold"),bg="black",fg="white").pack(side=LEFT,anchor="nw",ipadx=5,padx=5,ipady=10,pady=15)
screen2 = Entry(frame2, textvar=download_Path, font=("lucida 12 italic"), bg='white', borderwidth=6, relief=SUNKEN)
screen2.pack(ipady=10, padx=10, pady=10,ipadx=40)
# labeb1=Button(frame2,text="Browse",font=("lucida 5 italic bold"),bg="white",fg="black").pack(side=RIGHT)
b1=Button(frame2,text="Browse",font=("lucida 10 italic bold"),bg="white",fg="black",relief=SUNKEN,borderwidth=10,command=Browse).pack(side=RIGHT)
frame2.pack(pady=5,fill=X,padx=10)

b2=Button(root,text="Download as mp4",font=("lucida 15 italic bold"),bg="red",fg="white",relief=SUNKEN,borderwidth=10,command=Download).pack(side=TOP,pady=20,ipady=10)

root.config(background="black")

root.mainloop()