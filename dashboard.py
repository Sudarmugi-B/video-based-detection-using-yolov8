import streamlit as st

def main():
    st.title("Welcome to Explore Our Detection System!!!😊")

    # Create a hyperlink that points to the localhost URL
    st.markdown("<a href='http://localhost:8503' style='font-size: 20px;'>Click to Go in System 😉</a>", unsafe_allow_html=True)
    st.markdown("<a href='http://192.168.1.6:8503' style='font-size: 20px;'>Click to Go in Mobile 😉</a>", unsafe_allow_html=True)
       

if __name__ == "__main__":
    main()


