
# Python program to translate
# speech to text and text to speech
  
  
import speech_recognition as sr
import pyttsx3 
  
# Initialize the recognizer 
r = sr.Recognizer() 
  
# Function to convert text to
# speech
def SpeakText(command):
      
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(command) 
    engine.runAndWait()
      
      
# Loop infinitely for user to
# speak
  
while(1):    
      
    # Exception handling to handle
    # exceptions at the runtime
    try:
          
        # use the microphone as source for input.
        with sr.Microphone() as source2:
              
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
              
            #listens for the user's input 
            audio2 = r.listen(source2)
              
            # Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            if MyText=="activate":
  
                MyText="activating now"
                SpeakText(MyText)
                break
              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        print("unknown error occured")
# Face Recognition

# Importing the libraries
#import cv2
import speech_recognition as sr
import pyttsx3 
import cv2
r = sr.Recognizer()
if MyText=="activating now":

    # Loading the cascades
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    # Defining a function that will do the detections
    def detect(gray, frame):
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.5, 3)
            if len(eyes)==0:
                cv2.putText(frame,"DROWSY",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255, 255, 0),2)
                SpeakTest("Wake Up Wake Up")
            else:
                cv2.putText(frame,"AWAKE",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(100, 255, 0),2)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        return frame

    # Doing some Face Recognition with the webcam
    video_capture = cv2.VideoCapture(0)
    while(1):

            _, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            canvas = detect(gray, frame)
            cv2.imshow('Video', canvas)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    video_capture.release()
    cv2.destroyAllWindows()
