import streamlit as st
st.title('HAPPY BIRTHDAY')
st.write('THATS CRAZY ITS YOUR BIRTHDAY (I dont care if it is or not. IT IS NOW YOUR BIRTHDAY WOOHOOOOOOOO mess around with the slider for a surprise')
slider_value = st.slider('Select a value', min_value=0,max_value=100, value=50)
if (slider_value > 51):
    VIDEO_URL = "https://www.youtube.com/watch?v=NT3zp2vYMvo"
else:
    VIDEO_URL = "https://www.youtube.com/watch?v=2GK1B1RshN4"

st.balloons()
st.video(VIDEO_URL, start_time=2)
