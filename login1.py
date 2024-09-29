import streamlit as st
import sqlite3
from streamlit import util
from dashboard import main as dashboard_main

# Connect to SQLite database
conn = sqlite3.connect('user_credentials.db')
cursor = conn.cursor()

def signup_user(username, password):
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

def authenticate(username, password):
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    if result and result[0] == password:
        return True
    return False

class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def main():
    st.title("NeuraScan 🕵🏽‍♀️")

    st.markdown("<h3>Welcome to Our Application!!!😊 </h3>", unsafe_allow_html=True)
    st.write("Login (or) Signup to Continue")

    session_state = SessionState(logged_in=False)  # Initialize session state variable

    if not session_state.logged_in:
        mode = st.radio("Choose a mode", ["Login", "Signup"])
        if mode == "Login":
            login(session_state)
        else:
            signup()

    if session_state.logged_in:
        logout_button = st.button("Logout")
        if logout_button:
            session_state.logged_in = False
        dashboard_main()  # Display the dashboard content

def login(session_state):
    st.header("Login")
    # Display custom image for login
    st.image('login_img1.jpg')

    with st.form(key='login_form'):
        username = st.text_input("Username")
        password = st.text_input("Password", type='password')

        login_button = st.form_submit_button("Login")

        if login_button:
            if authenticate(username, password):
                st.success('Login successful!',icon="✅")
                st.balloons()
                session_state.logged_in = True  # Set the session state to indicate logged-in state
            else:
                st.warning('Invalid credentials', icon="⚠️")

def signup():
    st.header("Signup")
     # Display custom image for signup
    st.image('sign_in.jpg')
    with st.form(key='signup_form'):
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type='password')

        signup_button = st.form_submit_button("Signup")

        if signup_button:
            if signup_user(new_username, new_password):
                st.success('Signup successful! You can now login.',icon="✅")
            else:
                st.warning("Username already exists. Please choose a different one.")

if __name__ == "__main__":
    main()

# Close the database connection when the Streamlit app is closed
conn.close()
