
import streamlit as st
import cv2
import numpy as np

# Our sketch generating function
def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)
    
    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

def main_loop():
    st.title("Live Sketch App")
    st.subheader("This app allows you to get your live sketch!")
    st.text("We use OpenCV and Streamlit for this demo")
    st.title("Webcam Live Feed")
   
    FRAME_WINDOW = st.image([])
    run = st.button('Run')
    stop = st.button('Stop')
    camera = cv2.VideoCapture(0)
    
         
    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            
        FRAME_WINDOW.image([frame, sketch(frame)])   

    if stop:
        st.write('Stopped')
  



if __name__ == '__main__':
    main_loop()