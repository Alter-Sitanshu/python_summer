from tkinter import *
from tkinter import filedialog,simpledialog,messagebox
from tkinter import ttk
import pytube as yt
import os
from pydub import AudioSegment
import pygame
from mutagen.mp3 import MP3
import time

FONT = ("Courier", 14, "bold")
CURRENT = False
SELECTED = ""
pos = 0
time_stamp = 0
time_id = None

class Player:
    def __init__(self) -> None:
        # ---- initialising pygame mixer -----
        pygame.mixer.init()


    # ----- All the Functionalities ------
    def search(self) -> None:
        try:
            song_box.insert(END, "Extracting....")
            song_url = simpledialog.askstring(title="url", prompt="")
            video = yt.YouTube(url=song_url)
            audio = video.streams.filter(only_audio=True, file_extension="mp4").first()
            init_path = audio.download("/home/sitanshu/Downloads/")

            mp3_file_path = os.path.splitext(init_path)[0] + ".mp3"
            print(mp3_file_path)
            # Converting the downloaded audio file to MP3
            audio1 = AudioSegment.from_file(init_path, format="mp4")
            audio1.export(mp3_file_path, format="mp3")

            #removing the original file (mp4)
            os.remove(init_path)
            print("Downloaded !!")
        
            # Adding to the playlist
            song = str(mp3_file_path).replace("/home/sitanshu/Downloads/", "")
            song = song.replace(".mp3", "")
            if song in loaded_songs:
                song_box.delete(END)
                messagebox.showwarning("Warning", "Song already loaded !")
            else:
                song_box.delete(END)
                song_box.insert(END, song)
        except:
            song_box.delete(END)


    def add_song(self) -> None:
        song = filedialog.askopenfilename(title="Choose a song", initialdir="/home/sitanshu/Downloads/", filetypes=(("mp3 files", "*.mp3"), ))
        song = str(song).replace("/home/sitanshu/Downloads/", "")
        song = song.replace(".mp3", "")
        if song != '()' and song not in loaded_songs:
            ok = messagebox.askyesno("Confirm", "Are you sure ?")
            if ok:
                song_box.insert(END, song)
        elif song != '()':
            messagebox.showwarning("Warning", "Song already loaded !")

    def delete(self) -> None:
        if song_box.curselection() == ():
            loaded_songs.pop(song_box.index(END)-1)
            song_box.delete(END)
        else:
            loaded_songs.pop(song_box.index(ACTIVE))
            song_box.delete(ACTIVE)

    def play(self) -> None:
        global SELECTED, CURRENT
        global pos
        global time_stamp, time_id
        if song_box.curselection() == ():
            pass
        else:
            song = song_box.get(ACTIVE)
            song_length = MP3(f"/home/sitanshu/Downloads/{song}.mp3").info.length

            if SELECTED != song:
                SELECTED = song
                time_slider.config(value=0)
                song = f"/home/sitanshu/Downloads/{song}.mp3"
                pygame.mixer.music.load(song)
                pygame.mixer.music.play(loops=0)
                pos = 0       # -----RESET THE POS-----
                time_stamp = 0
                if time_id:
                    status_bar.after_cancel(time_id)
                self.get_time_stamp(False, time_stamp, song_length)
                CURRENT = False
            elif SELECTED == song:
                song = f"/home/sitanshu/Downloads/{song}.mp3"
                if CURRENT:
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play(loops=0, start=pos/1000)
                    self.get_time_stamp(True, time_stamp, song_length)
                    CURRENT = False
                else:
                    pass

    def pause(self) -> None:
        global CURRENT
        global pos
        pos += pygame.mixer.music.get_pos()
        pygame.mixer.music.pause()
        CURRENT = True
        if time_id:
            status_bar.after_cancel(time_id)

    def forward(self) -> None:
        global CURRENT
        length = song_box.size()
        if song_box.curselection():
            index = song_box.curselection()[0]
            forw = 1 + index
        else:
            forw = 0
        if forw == length:
            messagebox.showerror("Error", "No more songs !")
        else:
            song_box.selection_clear(ACTIVE)
            song_box.selection_set(forw)
            song_box.activate(forw)
            CURRENT = False
            self.play()


    def backward(self) -> None:
        global CURRENT
        if song_box.curselection():
            index = song_box.curselection()[0]
            if index:
                back = index - 1
            else:
                back = None
        else:
            back = None
        if back == None:
            messagebox.showerror("Error", "No more songs !")
        else:
            song_box.selection_clear(ACTIVE)
            song_box.selection_set(back)
            song_box.activate(back)
            CURRENT = False
            self.play()

    def get_time_stamp(self, pause: bool, time_: int, song_length: float) -> None:
        global time_stamp, time_id
        if pause:
            time_stamp = time_ + int((pygame.mixer.music.get_pos()+335)/1000)
        else:
            time_stamp = int(pygame.mixer.music.get_pos()/1000)
        time_id = status_bar.after(1002, self.get_time_stamp, pause, time_, song_length)
        value = (time_stamp/song_length)*100
        time_slider.config(value=value)
        status_bar.config(text=f"{time.strftime('%M:%S',time.gmtime(time_stamp))} / {time.strftime('%M:%S', time.gmtime(song_length))}  ")


    def slide(self, x) -> None:
        global time_stamp, pos
        if song_box.curselection() != ():
            song = song_box.get(ACTIVE)
            song_length = MP3(f"/home/sitanshu/Downloads/{song}.mp3").info.length
            time_pos_slider = (int(float(time_slider.get()))/100)*song_length
            pygame.mixer.music.pause()
            if time_id:
                status_bar.after_cancel(time_id)
            pos = time_pos_slider*1000
            pygame.mixer.music.play(loops=0, start=time_pos_slider)
            time_stamp = 0
            self.get_time_stamp(True, time_= time_pos_slider, song_length=song_length)
        else:
            pass
    

player = Player()
# -------- GUI ---------
screen = Tk()
screen.minsize(width=500, height=450)
screen.config(padx=0, pady=0)
screen.title("Mp3 Player")

# ----- MENU -------
menu = Menu(screen, relief=SOLID, bd=2)
screen.config(menu=menu)

add_song_menu = Menu(menu)
menu.add_cascade(label="Add", menu=add_song_menu)
add_song_menu.add_command(label="Add Song", command=player.add_song)
add_song_menu.add_separator()
add_song_menu.add_command(label="From Youtube", command=player.search)
menu.add_command(label="Delete", command=player.delete)

# ------- LIST BOX FOR SONGS -------
song_frame = Frame(screen)

loaded_songs = [f.replace(".mp3", "") for f in os.listdir("/home/sitanshu/Downloads/") if os.path.isfile(os.path.join("/home/sitanshu/Downloads/", f)) and f.__contains__(".mp3")]
song_box = Listbox(song_frame, bg="black", fg="green", width=60, height=20, selectbackground="grey", font=("Ariel", 12, ""), selectmode="single")
for songs in loaded_songs:
    song_box.insert(END, songs)
song_box.pack(ipadx=5, ipady=5)
song_frame.grid(row=0, column=0, pady=15, padx=50)

# ------SONG SLIDER ----------
time_slider = ttk.Scale(screen, from_=0, to=100, length=440, orient=HORIZONTAL, cursor="hand2")
time_slider.grid(row=1, column=0 ,pady=10)
time_slider.bind("<ButtonRelease-1>", player.slide)

# ------ CONTROLS -------
control_frame = Frame(screen)

play_img = PhotoImage(file="images/play.png").subsample(6,6)
play_button = Button(master=control_frame, image=play_img, borderwidth=0, cursor="hand2", activebackground=screen.cget("bg"), command=player.play)
pause_img = PhotoImage(file="images/pause.png").subsample(5,5)
pause_button = Button(master=control_frame, image=pause_img, borderwidth=0, cursor="hand2", activebackground=screen.cget("bg"), command=player.pause)
forw_img = PhotoImage(file="images/forw.png").subsample(4,4)
forw_button = Button(master=control_frame, image=forw_img, borderwidth=0, cursor="hand2", activebackground=screen.cget("bg"), command=player.forward)
back_img = PhotoImage(file="images/back.png").subsample(4,4)
back_button = Button(master=control_frame, image=back_img, borderwidth=0, cursor="hand2", activebackground=screen.cget("bg"), command=player.backward)

play_button.grid(column=1, row=0, padx=10)
pause_button.grid(column=2, row=0, padx=10)
forw_button.grid(column=3, row=0, padx=10)
back_button.grid(column=0, row=0, padx=10)
control_frame.grid(row=2, column=0, pady=20)

# ------- STATUS BAR ----------
status_bar = Label(screen, text="", bd=1, anchor=E, relief=GROOVE, font=("Ariel", 13, "bold"))
status_bar.grid(row=3, column=0, ipady=8, sticky="ew")

screen.mainloop()