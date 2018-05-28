# facerec.py
import cv2
size=1
webcam = cv2.VideoCapture(0) #Use camera 0

# We load the xml file
classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:

    # Loop until the camera is working
    rval = False
    while(not rval):
        # Put the image from the webcam into 'frame'
        (rval, frame) = webcam.read()
        if(not rval):
            print("Failed to open webcam. Trying again...")

    frame=cv2.flip(frame,1,0) #Flip to act as a mirror

    # Resize the image to speed up detection
    mini = cv2.resize(frame, (int(frame.shape[1] / size), int(frame.shape[0] / size)))

    # We let OpenCV do it's thing
    faces = classifier.detectMultiScale(mini)

    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f] #Scale the shapesize backup
        cv2.rectangle(frame, (x, y), (x + w, y + h),(0,255,0),thickness=2)

    # Show the image and lookout for the Escape key
    cv2.imshow('OpenCV', frame)
    key = cv2.waitKey(10)
    if key == 27: #The Esc key
        break
