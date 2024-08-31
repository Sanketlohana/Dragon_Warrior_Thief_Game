import streamlit as st # type: ignore
import random
import base64

# Dictionary of rules for who defeats whom
rules = {
    "initial":"static",
    "Dragon": "Warrior",  # Dragon Overpowers Warrior
    "Warrior": "Thief",   # Warrior Defeats Thief
    "Thief": "Dragon"     # Thief Steals from Dragon
}
user_choice = 'initial'
def game():
    # Determine the outcome
    if user_choice == "initial":
        st.markdown("##### Choose an option")
    elif user_choice == computer_choice:
        # st.markdown("#### Result :")
        st.markdown("## It's a Draw!")
        
    elif rules[user_choice] == computer_choice:
        # st.markdown("#### Result :")
        st.markdown("## You Win!")
    else:
        # st.markdown("#### Result :")
        st.markdown("## You Lose!")

# Function to set the background image using a local file
def set_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded_img = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_img});
            background-size: contain;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image using the local file path
set_bg_image('bgimage.png')

choices = ["Thief", "Warrior","Dragon"]
computer_choice = random.choice(choices)
col1, col2, col3 = st.columns([2,2,2])

with col1:
    st.markdown("<br>",unsafe_allow_html=True)    
    if st.button("Choose Dragon"):
        result1 = 1
        user_choice = "Dragon"
    st.markdown("<br><br><br><br><br>",unsafe_allow_html=True)    
    if st.button("Choose Warrior"):
        result2 = 1 
        user_choice = "Warrior"
    st.markdown("<br><br><br><br><br>",unsafe_allow_html=True)    
    if st.button("Choose Thief"):
        result3 = 1
        user_choice = "Thief"

with col2:
    st.markdown("<br>",unsafe_allow_html=True)    
    st.subheader("Your choice")
    st.markdown("<br>",unsafe_allow_html=True)
    if 'result1' in locals():
        st.image("image1.png",width = 190,caption = "Dragon")
    elif 'result2' in locals():
        st.image("image2.png",width = 190,caption = "Warrior")
    elif 'result3' in locals():
        st.image("image3.png",width = 190,caption = "Thief")
    game()
    

with col3:
    st.markdown("<br>",unsafe_allow_html=True)    
    st.subheader("Computer choice")
    if user_choice!= "initial":
        if computer_choice == "Dragon":
            st.image("image1.png",width = 187,caption = "Dragon")
        elif computer_choice == "Warrior":
            st.image("image2.png",width = 187,caption = "Warrior")
        elif computer_choice == "Thief":
            st.image("image3.png",width = 189,caption = "Thief")

# with col4:
#     st.markdown("<br><br><br><br><br><br><br><br><br><br>",unsafe_allow_html=True)
    
#     game()



        
    