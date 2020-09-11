import pygame 
import tkinter as tkr
player = tkr.Tk()
player.title("Music Player")
player.geometry("205x340")


file = "darkside.mp3"

def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def ExitPlayer():
    pygame.mixer.music.stop()

def Pause():
    pygame.mixer.music.pause()

def Resume():
    pygame.mixer.music.unpause()



Button1 = tkr.Button(player, width = 5 , height = 3 , text="PLAY", command = Play)
Button1.pack(fill = "x")

Button2 = tkr.Button(player, width = 5 , height = 3 , text="STOP", command = ExitPlayer)
Button2.pack(fill = "x")
Button3 = tkr.Button(player, width = 5 , height = 3 , text="PAUSE", command = Pause)
Button3.pack(fill = "x")
Button4 = tkr.Button(player, width = 5 , height = 3 , text="RESUME", command = Resume)
Button4.pack(fill = "x")




label1 = tkr.LabelFrame(player , text ="Song name")
label1.pack(fill = "both" , expand = "yes")
contents1 = tkr.Label(label1,text = file)
contents1.pack()


player.mainloop()

