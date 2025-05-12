import streamlit as st
import random

st.set_page_config(page_title="For Raha 💌", page_icon="🐾", layout="centered")

# Initial CSS & Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap');

html, body, [class*="css"] {
    font-family: 'Patrick Hand', cursive;
    background-color: #fff0f6;
    overflow: hidden;
}

.title {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    color: #ff69b4;
    margin-top: 20px;
    animation: sparkle 2s infinite alternate;
}

.subtitle {
    font-size: 20px;
    text-align: center;
    color: #6c757d;
    margin-bottom: 30px;
}

.box {
    background-color: #fff;
    border-radius: 20px;
    padding: 30px;
    margin-top: 20px;
    box-shadow: 0 8px 25px rgba(255, 192, 203, 0.4);
    animation: float 3s ease-in-out infinite;
}

.message {
    font-size: 22px;
    color: #333;
    font-style: italic;
    text-align: center;
    margin-top: 20px;
}

.footer {
    font-size: 14px;
    color: #999;
    text-align: center;
    margin-top: 50px;
}

button:hover {
    color: #ff69b4 !important;
}

@keyframes sparkle {
    from {text-shadow: 0 0 5px #ffc0cb;}
    to {text-shadow: 0 0 20px #ff69b4;}
}

@keyframes float {
    0% { transform: translatey(0px); }
    50% { transform: translatey(-10px); }
    100% { transform: translatey(0px); }
}

.butterfly {
    animation: butterfly 4s ease-in-out infinite;
}

@keyframes butterfly {
    0% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-10px) scale(1.2); }
    100% { transform: translateY(0) scale(1); }
}

.plant {
    display: inline-block;
    font-size: 36px;
    color: #32cd32;
    animation: grow 3s ease-in-out infinite;
}

@keyframes grow {
    0% { transform: scale(0); }
    100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">For Raha 🌷</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Here’s something small with care💖</div>', unsafe_allow_html=True)

# Session state
if 'loaded' not in st.session_state:
    st.session_state.loaded = False
    st.session_state.image = ""
    st.session_state.msg1 = ""
    st.session_state.msg2 = ""
    st.session_state.fact = ""
    st.session_state.plant_growth = ""

# Image pool
cat_images = [
    "https://images.unsplash.com/photo-1555685812-4b943f1cb0eb",  # cozy
    "https://images.unsplash.com/photo-1601758123927-1961c8991b69",  # playful
    "https://images.unsplash.com/photo-1518791841217-8f162f1e1131",  # sleepy
    "https://images.unsplash.com/photo-1574158622682-e40e69881006",  # curious
    "https://images.unsplash.com/photo-1592194996308-7b43878e84a6"   # gentle
]

# Sweet messages
sweet_messages = [
    "You have a way of making ordinary moments feel like little treasures. 💎",
    "Like a cat curled in sunlight, your presence is warmth I didn’t know I needed. ☀️",
    "The world feels softer when you’re around — like everything exhales. 🌿",
    "You’re the kind of person who turns small talk into something worth remembering.",
    "If kindness had a favorite student, it’d be you. 🌸"
]

# Compliments/jokes
fun_jokes = [
    "Scientists confirm: Your laugh is 97% contagious. Handle with care. 😄",
    "If you were a cat, you’d be the type who steals hearts instead of food. 🐾",
    "Warning: Prolonged exposure to your smile may cause excessive happiness.",
    "I’d say you’re one in a million, but honestly? The math doesn’t check out — you’re rarer. ✨"
]

# Cat facts
cat_facts = [
    "Did you know cats purr not only when they’re happy, but also when they’re healing? 🐱",
    "Cats sleep up to 70% of their lives — professional nappers. 😴",
    "Each cat’s nose print is unique — like a fingerprint! 👃",
    "When a cat slowly blinks at you, it’s a sign of trust and love. 💕"
]

# Click or reload
def generate():
    st.session_state.loaded = True
    st.session_state.image = random.choice(cat_images)
    st.session_state.msg1 = random.choice(sweet_messages)
    st.session_state.msg2 = random.choice(fun_jokes)
    st.session_state.fact = random.choice(cat_facts)
    st.session_state.plant_growth = "🌱"

# Main interaction
if st.button("💘 Tap for a Mood-Lifter"):
    generate()

# Show content if loaded
if st.session_state.loaded:
    st.markdown(f"""
    <div class="box">
        <img src="{st.session_state.image}" style="width:100%; border-radius:15px;">
        <div class="message">{st.session_state.msg1}</div>
        <div class="message" style="color:#d6336c;">{st.session_state.msg2}</div>
        <div class="message" style="font-size:18px; color:#888; margin-top:20px;">{st.session_state.fact}</div>
    </div>
    """, unsafe_allow_html=True)

    # Butterfly animation (appears above the content)
    st.markdown('<div class="butterfly">🦋</div>', unsafe_allow_html=True)

    # Growing plant emoji (magical growth effect)
    st.markdown(f'<div class="plant">{st.session_state.plant_growth}</div>', unsafe_allow_html=True)

    st.markdown("""<div style="text-align:center; font-size:18px; color:#444; margin-top:40px;"> — With warmth, Joy 🐾💌 </div>""", unsafe_allow_html=True)

    # Song
    st.markdown("---")
    st.markdown("### 🎶 A song for when you need a hug in melody:")
    st.video("https://www.youtube.com/watch?v=LSUR0075KLI")


# Footer
st.markdown('<div class="footer">Made with love for Raha — because Joy cares 🌙</div>', unsafe_allow_html=True)
