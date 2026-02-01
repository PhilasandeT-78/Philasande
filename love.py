import streamlit as st
from time import sleep
from streamlit.runtime.scriptrunner import get_script_run_ctx
import sys

# Page config
st.set_page_config(
    page_title="For My Love ❤️",
    page_icon="💖",
    layout="centered"
)

if get_script_run_ctx() is None:
    print("Please run this app with: streamlit run .\\Week_01\\love.py")
    sys.exit(0)

# Custom CSS Styling
st.markdown("""
<style>

body {
background-color: #fff0f5;
}

.love-box {
background: linear-gradient(135deg, #ff9a9e, #fad0c4);
padding: 30px;
border-radius: 20px;
text-align: center;
box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
}

.big-text {
font-size: 28px;
font-weight: bold;
color: #ffffff;
}

.message {
font-size: 20px;
color: white;
line-height: 1.6;
}

.heart {
font-size: 40px;
animation: pulse 1.5s infinite;
}

@keyframes pulse {
0% { transform: scale(1); }
50% { transform: scale(1.2); }
100% { transform: scale(1); }
}

</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("<h1 style='text-align:center;color:#ff4b6e;'>💖 My Love Letter App 💖</h1>", unsafe_allow_html=True)

st.markdown("<div style='text-align:center;' class='heart'>❤️</div>", unsafe_allow_html=True)

st.write("")

# Message Card
st.markdown("""
<div class="love-box">
<div class="big-text">To The Most Amazing Girlfriend 💕</div>
<br>
<div class="message">
Every day with you feels like a blessing.  
Your smile lights up my world.  
Your love gives me strength.  
Your presence makes everything better.  

<br><br>
I just want you to remember how deeply loved, appreciated, and special you are to me.  
Forever yours ❤️
</div>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# Bouquet Surprise Button
if st.button("💐 Click For A Flower Surprise 💐"):

    with st.spinner("Preparing your bouquet..."):
        sleep(1.5)

    st.success("Surprise!!! 💖💐")

    # Celebration animation
    st.balloons()

    # Bouquet Image (online image)
    st.image(
        "https://th.bing.com/th/id/OIP.udpwkvZQqKWnt80s7reLHQHaHa?w=156&h=150&c=6&o=7&dpr=1.3&pid=1.7&rm=3",
        caption="A bouquet for you my love 🌹",
        use_container_width=True
    )

    st.toast("I love you more than words can say ❤️", icon="💖")

