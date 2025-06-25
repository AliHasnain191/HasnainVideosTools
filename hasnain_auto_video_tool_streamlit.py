import shutil
import os

# Redefine the folder structure due to code execution environment reset
base_folder = "/mnt/data/Hasnain_Audio_To_Video_Tool"
input_audio_folder = os.path.join(base_folder, "input_audio")
assets_folder = os.path.join(base_folder, "assets", "motivation")
output_folder = os.path.join(base_folder, "output")

# Create necessary directories
os.makedirs(input_audio_folder, exist_ok=True)
os.makedirs(assets_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Python script content
tool_code = '''\
from moviepy.editor import *
import os

def get_media_clips(folder):
    clips = []
    for filename in sorted(os.listdir(folder)):
        path = os.path.join(folder, filename)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_clip = ImageClip(path).set_duration(5).fadein(1).fadeout(1)
            clips.append(img_clip)
        elif filename.lower().endswith(('.mp4', '.mov')):
            video_clip = VideoFileClip(path).subclip(0, 5).fadein(1).fadeout(1)
            clips.append(video_clip)
    return clips

def main():
    audio_file = 'input_audio/motivation.mp3'
    topic = os.path.splitext(os.path.basename(audio_file))[0]
    visuals_path = os.path.join('assets', topic)

    audio = AudioFileClip(audio_file)
    media_clips = get_media_clips(visuals_path)
    
    final = concatenate_videoclips(media_clips, method="compose").set_audio(audio)
    final = final.set_duration(audio.duration)
    final.write_videofile("output/output_video.mp4", fps=24)

if __name__ == "__main__":
    main()
'''

# Write the main script
with open(os.path.join(base_folder, "hasnain_auto_audio_video_tool.py"), "w") as f:
    f.write(tool_code)

# Create README
with open(os.path.join(base_folder, "README.txt"), "w") as f:
    f.write(
        "🎬 Hasnain Auto Audio to Video Tool\n\n"
        "Steps to use:\n"
        "1. Place your .mp3 or .wav file in 'input_audio/' folder.\n"
        "2. Name the file by category (e.g., love.mp3, sports.mp3).\n"
        "3. Place visuals in 'assets/<category>/' folder.\n"
        "4. Run the script: python hasnain_auto_audio_video_tool.py\n"
        "5. Video will be saved in 'output/' folder.\n"
    )

# Add placeholder files
with open(os.path.join(input_audio_folder, "motivation.mp3"), "wb") as f:
    f.write(b"")

with open(os.path.join(assets_folder, "1.jpg"), "wb") as f:
    f.write(b"")

with open(os.path.join(assets_folder, "2.jpg"), "wb") as f:
    f.write(b"")

# Create ZIP
zip_path = "/mnt/data/Hasnain_Audio_To_Video_Tool.zip"
shutil.make_archive(zip_path.replace(".zip", ""), 'zip', base_folder)

zip_path
