 from datetime import datetime
 from pygame import mixer

Starting the mixer
mixer.init()
#
Loading the song
mixer.music.load("song.mp3")
#
Setting the volume
mixer.music.set_volume(0.7)
#
open log file
f = open("Log.txt", "wt")
f.write("%s" % datetime.now())
while True:
     c = datetime.now()
     H = c.hour
     M = c.minute
     # this condition use for water
     if H == H + 1:
         # Start playing the song
         mixer.music.play()
         # write start time in file
         f.write("Water start time %s" % datetime.now())
         # line break in file
         f.write("\n")
         w = input("If you Drank the ONE glass of water  then type D/d : ")
         if w == 'D' or 'd':
             # write end time in file
             f.write("Water end time %s" % datetime.now())

             # line break in file
             f.write("\n")
             mixer.music.stop()
             print("DONE")
             break

     # This condition use for eye
     elif M == M + 1:
         # Start playing the song
         mixer.music.play()
         # write start time in file
         f.write("Eye close start time %s" % datetime.now())
         # line break in file
         f.write("\n")
         w = input("If you closed the eye  for THREE MINUTE then type E/e : ")
         if w == 'E' or 'e':
             # write end time in file
             f.write("Eye closed end time %s" % datetime.now())
             # line break in file
             f.write("\n")
             mixer.music.stop()
             print("DONE")
             break
