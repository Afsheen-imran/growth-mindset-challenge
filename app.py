import streamlit as st

# Custom CSS for styling and animations
def local_css(file_name):  # Use a variable name like `file_name`
    with open(file_name) as f:  # Open the CSS file
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load custom CSS
local_css("style.css")  # Pass the file name as a string

# App Title
st.title("🌱 Growth Mindset Challenge")

# Introduction Section
st.markdown("""
<div class="intro-card">
    <h2>Welcome to the Growth Mindset Challenge!</h2>
    <p>Complete daily tasks to develop a growth mindset and unlock your potential.</p>
</div>
""", unsafe_allow_html=True)

# Daily Challenge Section
st.markdown("""
<div class="challenge-card">
    <h2>Today's Challenge</h2>
    <p>Select one thing you learned today and one thing you struggled with.</p>
</div>
""", unsafe_allow_html=True)

# Dropdown Menu for Pre-Written Responses
options = [
    "Write down one thing you learned today and one thing you struggled with.",
    "I learned how to manage my time better, but I struggled with staying focused.",
    "I learned a new skill, but I struggled with understanding the basics.",
    "I learned to be more patient, but I struggled with handling stress.",
    "I learned to ask for help, but I struggled with feeling confident.",
    "I learned to set realistic goals, but I struggled with achieving them.",
    "I learned to embrace failure, but I struggled with self-doubt.",
    "I learned to prioritize tasks, but I struggled with procrastination.",
    "I learned to communicate better, but I struggled with listening.",
    "I learned to stay positive, but I struggled with negative thoughts."
]

selected_option = st.selectbox("Choose a response:", options)

# Submit Button
if st.button("Submit"):
    st.markdown(f"""
    <div class="success-message">
        <p>🎉 Thank you for completing today's challenge!</p>
        <p>Your response: <strong>{selected_option}</strong></p>
    </div>
    """, unsafe_allow_html=True)

# Progress Tracker
st.markdown("""
<div class="progress-card">
    <h2>Your Progress</h2>
    <p>Track how many challenges you've completed so far.</p>
</div>
""", unsafe_allow_html=True)

progress = st.slider("How many challenges have you completed?", 0, 30)
st.write(f"You've completed {progress} challenges so far. Keep going!")

# Footer
st.markdown("""
<div class="footer">
    <p>Made with ❤️ by [Afsheen Imran]</p>
</div>
""", unsafe_allow_html=True)