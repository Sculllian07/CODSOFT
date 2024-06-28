import cv2
import os

# Get the directory where this script is located
script_dir = os.path.dirname(__file__)

# Path to the Haar cascade file for face detection
harcascade = os.path.join(script_dir, "model/haarcascade_frontalface_default.xml")

def detect_faces_video():
    # Initialize the video capture from default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    
    # Set the width and height of the video capture
    cap.set(3, 640)  # Width
    cap.set(4, 480)  # Height
    
    # Create a cascade classifier for detecting faces
    facecascade = cv2.CascadeClassifier(harcascade)
    
    # Check if the cascade classifier loaded successfully
    if facecascade.empty():
        print("Error: Could not load cascade classifier.")
        cap.release()
        cv2.destroyAllWindows()
        return
    
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # If frame is not read correctly, break the loop
        if not ret:
            break
        
        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the grayscale frame
        faces = facecascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
        
        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('Face Detection', frame)
        
        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to start face detection from the webcam feed
detect_faces_video()

