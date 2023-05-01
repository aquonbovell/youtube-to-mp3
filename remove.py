import os
import moviepy.editor as mp
# Insert Video File Path
clip = mp.VideoFileClip("Luh Kel - F Love (Official Music Video)" +".mp4")
# Insert Audio File Path
clip.audio.write_audiofile("Luh Kel - F Love (Official Music Video)"+".mp3")
clip.close()
try:
  os.remove(("Luh Kel - F Love (Official Music Video)")+".mp4")
except OSError:
  pass
# result of success
print("successfully removed!!")
