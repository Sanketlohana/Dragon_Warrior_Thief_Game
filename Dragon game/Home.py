import streamlit as st # type: ignore

# Center the title using st.markdown with markdown syntax
st.markdown("<h1 style='text-align: center;'>Dragon Warrior Thief Game</h1>", unsafe_allow_html=True)

# Add some space after the title
st.text("")
st.text("")

# Create three columns with custom widths for spacing
col1, col2, col3 = st.columns([1.5, 1.6,1.7])

# Display an image in each column
with col1:
    st.image("image1.png", use_column_width=True)

with col2:
    st.image("image2.png", use_column_width=True)
    
with col3:
    st.image("image3.png", use_column_width=True)


