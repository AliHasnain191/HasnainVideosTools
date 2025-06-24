import streamlit as st
from moviepy.editor import VideoFileClip, concatenate_videoclips

st.set_page_config(page_title="Hasnain Video Tool", layout="centered")
st.title("🎬 Hasnain Auto Video Tool")
st.markdown("Merge multiple video clips into one!")

uploaded_files = st.file_uploader("Upload video clips", type=["mp4", "mov", "avi"], accept_multiple_files=True)

if uploaded_files:
    clips = []
    for uploaded_file in uploaded_files:
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())
        clips.append(VideoFileClip(uploaded_file.name))

    final_video = concatenate_videoclips(clips)
    final_video.write_videofile("merged_output.mp4")

    with open("merged_output.mp4", "rb") as file:
        st.download_button("⬇️ Download Merged Video", file, file_name="output.mp4", mime="video/mp4")