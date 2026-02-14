import streamlit as st
import glob
import random
import time

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

# ---------------------------------
# SESSION STATE INITIALIZATION
# ---------------------------------
if "show_photos" not in st.session_state:
    st.session_state.show_photos = False

st.set_page_config(
    page_title="For Khethi ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------------------------
# CUSTOM CSS
# ---------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
}
.main {
    background-color: rgba(255, 255, 255, 0.96);
    padding: 3rem;
    border-radius: 30px;
    text-align: center;
}
.title {
    font-size: 2.6rem;
    color: #ff4d6d;
    font-weight: bold;
}
.subtitle {
    font-size: 1.3rem;
    color: #555;
    margin-bottom: 25px;
}
.heart {
    font-size: 3.5rem;
    animation: pulse 1.5s infinite;
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.25); }
    100% { transform: scale(1); }
}
.message {
    font-size: 1.1rem;
    line-height: 1.7;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# APP CONTENT
# ---------------------------------
st.markdown('<div class="main">', unsafe_allow_html=True)

st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="title">Happy Valentine’s Day, Khethi</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">To the sweetest soul I know 💕</div>',
    unsafe_allow_html=True
)

# ---------------------------------
# PHOTO GALLERY
# ---------------------------------

st.markdown("### Our Memories 📸")

if st.button("Show Our Pictures ❤️"):
    st.session_state.show_photos = True

if st.session_state.show_photos:
    image_files = glob.glob("images/*")
    random.shuffle(image_files)

    cols = st.columns(3)
    for i, img in enumerate(image_files):
        cols[i % 3].image(img, use_container_width=True)
# ---------------------------------
# LOVE MESSAGE REVEAL
# ---------------------------------
if st.button("Open My Heart 💌"):
    with st.spinner("For you, Khethi..."):
        time.sleep(1.5)

    st.markdown("""
    <div class="message">
    💖 <strong>Khethi,</strong><br><br>
    You have the kindest heart and the softest way of making everything feel okay.
    Being with you feels like home, peace, and happiness all at once.<br><br>

    Thank you for your love, your warmth, and your beautiful soul.
    I’m really grateful for you, today and always.<br><br>

    <strong>I love you ❤️</strong><br><br>
    — Yours
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("### A little video, just for you 🎥❤️")

video_file = open("video/khethi.mp4", "rb")
video_bytes = video_file.read()



if st.button("Play My Favourite Memory 🎬"):
    st.video("video/khethi.mp4")
