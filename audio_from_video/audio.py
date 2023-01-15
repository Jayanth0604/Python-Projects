import moviepy.editor

video = moviepy.editor.VideoFileClip("status.mp4.mp4")

audio = video.audio

audio.write_audiofile("audio.mp3")