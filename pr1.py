import streamlit as st
import random
import time

# 1. Page Configuration & Aesthetic
st.set_page_config(page_title="DecodeLabs Logic Engine", page_icon="🌱", layout="centered")

st.title("🌱 DecodeLabs Warm-Logic Engine")
st.write("A rule-based chatbot engineered with a human touch. Let's have a chat!")
st.write("---")

# 2. Initialize Session State for Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Render past chat logs directly onto the UI layout
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 3. Input Acquisition
user_query = st.chat_input("Say something...")

if user_query:
    # Render user's message instantly on screen
    with st.chat_message("user"):
        st.write(user_query)
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    # 4. Sanitization & Normalization Funnel
    clean_input = user_query.lower().strip()

    # 5. Process (Humanized Logic Engine)
    
    # Priority Rule 1: Termination / Goodbyes
    if clean_input in ['exit', 'quit', 'bye', 'goodbye']:
        goodbyes = [
            "Take care! Hope we talk again soon. 😊",
            "Goodbye! Have a wonderful rest of your day.",
            "Catch you later! It was nice chatting with you."
        ]
        bot_response = random.choice(goodbyes)
        
    # Priority Rule 2: Warm Greetings
    elif clean_input in ['hello', 'hi', 'hey', 'asalamualaikum']:
        greetings = [
            "Hey there! It's great to connect with you. How's your day going?",
            "Hello! Hope you're doing well. What's on your mind today?",
            "Hi! Always a pleasure. How can I help you out today?"
        ]
        bot_response = random.choice(greetings)
        
    # Priority Rule 3: Identity Queries (Who are you?)
    elif "your name" in clean_input or "who are you" in clean_input:
        bot_response = "I'm a rule-based AI built for DecodeLabs Project 1! I might run on hard-coded logic, but I always try my best to be helpful. ✨"
        
    # Priority Rule 4: Well-being Queries (How are you?)
    elif "how are you" in clean_input:
        well_being = [
            "I'm doing great, thank you for asking! Hope you are having a fantastic day too.",
            "Everything is running smoothly on my end! How are things treating you?",
            "Can't complain! Just sitting here ready to help you out. How about yourself?"
        ]
        bot_response = random.choice(well_being)
        
    # Priority Rule 5: Default Fallback (Zero-Hallucination Guardrail)
    else:
        fallbacks = [
            "Hmm, I'm not quite sure how to answer that just yet. My developer is still expanding my rules!",
            "I wish I could answer that, but my logic engine doesn't have a rule for it yet. Mind trying something else?",
            "That sounds interesting, but it's a bit beyond my current vocabulary! Try asking me how I am or saying hello."
        ]
        bot_response = random.choice(fallbacks)

    # Simulate a "human typing" pause for realism
    with st.spinner("Typing..."):
        time.sleep(0.6)  # Delays response by 600 milliseconds

    # Render bot response on screen
    with st.chat_message("assistant"):
        st.write(bot_response)
        
    # Save bot response to history log
    st.session_state.chat_history.append({"role": "assistant", "content": bot_response})