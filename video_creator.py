import config
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip

def create_video(input_clip, script, voiceover):
    clip = VideoFileClip(input_clip).subclip(0, config.VIDEO_DURATION)
    txt = TextClip(script, fontsize=24, method='caption', size=clip.size)
    txt = txt.set_duration(config.VIDEO_DURATION).set_pos("center")
    audio = AudioFileClip(voiceover)
    video = CompositeVideoClip([clip, txt]).set_audio(audio)
    out_path = f"{config.OUTPUT_DIR}/generated.mp4"
    video.write_videofile(out_path, fps=24)
    return out_path

if __name__ == '__main__':
    video_path = create_video("stock.mp4", "Beispieltext", "voice.mp3")
    print(f"Video gespeichert: {video_path}")
