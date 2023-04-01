# Import Statements
import streamlit as st
from PIL import Image

# Creating Title
st.title("Upload or take a picture in greyscale!")

# UI Widget to upload an image instead
uploaded_image = st.file_uploader("Upload Image")                                                                               

# UI Widget that allows user to start the camera
with st.expander("Start the Camera"):
    # Creating Camera Widget
    camera_picture = st.camera_input("Say cheese!")

# Expander can also be used as such: 
# expander = st.expander("Start the Camera: ")
# camera_picture = expander.camera_input("Say cheese!")

# If object (in our case a file object), then do the following... (if camera_picture is None, if 
# conditional would not be executed)
if camera_picture:

    # Image.open requires either a path (str) or a file object to be passed 
    # st.camera_input returns (if a picture is taken) a file object, so we can pass camera_picture as
    # the argument and thereby create a PIL Image object (returned from Image.open())
    image = Image.open(camera_picture)

    # image returns a PIL Image object, which has a method, convert(), that returns a converted
    # PIL Image object, which in our case, is grey-scale ("L")
    grey_image = image.convert("L")

    # Display the image on the streamlit web app
    st.image(grey_image)

# If user instead decides upload an image
if uploaded_image:
    # Open up the image with PIL Image.open()
    image = Image.open(uploaded_image)

    # Convert the image to grey scale
    grey_image = image.convert("L")

    # Display the image to the streamlit web app
    st.image(grey_image)




