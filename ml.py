import cv2
import requests
import numpy as np

# Function to create a named window and set its position
def create_window(window_name, x, y):
    cv2.namedWindow(window_name)
    cv2.moveWindow(window_name, x, y)

# Function to detect face shape
def detect_face_shape(frame):
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Loop over the detected faces
    for (x, y, w, h) in faces:
        # Draw a bounding box around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Add text label for the detected face
        cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame
#
# # Replace with the IP address and port from the IP Webcam app
# mobile_camera_url = "http://192.168.0.211:8080/video"
#
# # Create connections to the phone's camera feed and the webcam (usually 0 for the default webcam)
# cap_mobile = cv2.VideoCapture(mobile_camera_url)
# cap_webcam = cv2.VideoCapture(0)  # Use 0 for the default webcam, adjust as needed
#
# # Create windows for displaying the mobile camera and webcam video feeds
# create_window('Mobile Camera Feed', 700, 0)
# create_window('Webcam Feed', 700, 0)
#
# while True:
#     try:
#         # Read a frame from the phone's camera
#         ret_mobile, frame_mobile = cap_mobile.read()
#
#         # Read a frame from the webcam
#         ret_webcam, frame_webcam = cap_webcam.read()
#
#         # Detect face shape in the mobile camera frame
#         frame_mobile = detect_face_shape(frame_mobile)
#
#         # Detect face shape in the webcam frame
#         frame_webcam = detect_face_shape(frame_webcam)
#
#         # Display the mobile camera frame in one window
#         cv2.imshow('Mobile Camera Feed', frame_mobile)
#
#         # Display the webcam frame in another window
#         cv2.imshow('Webcam Feed', frame_webcam)
#
#         # Exit the loop when the 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     except Exception as e:
#         print(f"Error: {e}")
#         continue
#
# # Release the camera connections and close the windows
# cap_mobile.release()
# cap_webcam.release()
# cv2.destroyAllWindows()