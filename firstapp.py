import streamlit as st
st.title('HAPPY BIRTHDAY')
st.write('THATS CRAZY ITS YOUR BIRTHDAY')
slider_value = st.slider('Select a value', min_value=0,max_value=100, value=50)
st.write(f'Slider value: {slider_value}')
st.balloons()

VIDEO_URL = "https://www.youtube.com/watch?v=9WDbVJmXwK8"
st.video(VIDEO_URL, start_time=2)