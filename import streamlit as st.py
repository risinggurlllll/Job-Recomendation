import streamlit as st
import cv2
import numpy as np

# Function to analyze live video stream
def analyze_live_video():
    cap = cv2.VideoCapture(0)  # Use webcam, assuming it's the default camera (index 0)

    if not cap.isOpened():
        st.error("Error: Unable to open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Unable to receive frame from webcam.")
            break

        # Convert frame to grayscale for analysis
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Calculate brightness
        avg_brightness = np.mean(gray_frame)

        # Calculate blur
        avg_blur = cv2.Laplacian(gray_frame, cv2.CV_64F).var()

        # Display video stream and analysis results
        st.image(frame, channels="BGR", caption="Live Video Stream")
        st.write("Average Brightness:", avg_brightness)
        st.write("Average Blur:", avg_blur)

        # Check for stop button click
        if st.button("Stop"):
            break

    # Release the webcam
    cap.release()

# Streamlit UI
def main():
    st.title("Live Video Analysis")

    st.write("Click the button below to start analyzing the live video stream from your webcam:")
    if st.button("Start Analysis"):
        analyze_live_video()

if __name__ == "__main__":
    main()