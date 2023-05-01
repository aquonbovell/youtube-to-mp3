# Python code to convert video to audio
def convert(link):
	# importing packages
	from pytube import YouTube
	import os
	import moviepy.editor as mp

	# url input
	yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)

	yt.streams.get_highest_resolution().download()

	# Insert Video File Path
	name = yt.title.replace('.', '') 
	name = name.replace('"', '') 
	name = name.replace(',', '') 
	name = name.replace("'", '') 
	clip = mp.VideoFileClip((name +".mp4"))
	# Insert Audio File Path
	clip.audio.write_audiofile(name+".mp3")
	clip.close()
	try:
		os.remove((name)+".mp4")
	except OSError:
		pass
	# result of success
	print("successfully converted!!")