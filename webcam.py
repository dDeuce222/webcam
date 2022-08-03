import cv2
  

# define a video capture object


while(True):
# Capture the video frame
# by frame
    

    cap = cv2.VideoCapture(0)
    if(cap.isOpened()):
        while(True):
            ret, frame = cap.read()
            if ret:
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cap.release()
        cv2.destroyAllWindows()
    else:
        print('disconnected')
    
    
    
# After the loop release the cap object

