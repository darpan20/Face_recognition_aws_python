
def surv_detect():
    import boto3
    import sys
    import cv2
    import os
    import time
    from Recognition_Collections import real_time_detect
    from Face_Recognition_App import main
    from winsound import PlaySound,SND_ASYNC
    s3 = boto3.client('s3')
    stream = cv2.VideoCapture(0)
    global x
    folderName = "user2"                                        # creating the person or user folder
    folderPath = os.path.join(os.path.dirname(os.path.realpath('__file__')), folderName)
    folderName1 = "Suspected"                                      # creating the person or user folder
    folderPath1 = os.path.join(os.path.dirname(os.path.realpath('__file__')), folderName1)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    if not os.path.exists(folderPath1):
        os.makedirs(folderPath1)
    cv2.namedWindow("FRAME 2", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("FRAME 2", 800,600)  
    
    while True:
        # read frames from live web cam stream
        (grabbed, frame) = stream.read(0)
        frame = cv2.flip(frame, 1)
        if grabbed==True:
        # resize the frames to be smaller and switch to gray scale
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         
         
         output = frame.copy()
         cv2.imshow("FRAME 2",output)
         cv2.imwrite(folderPath+"\\User0" + ".jpg",output)
         
         for filename in os.listdir(folderPath):
          try:
           print(filename)
           s3.upload_file('user2/User0.jpg','finals1',filename)
          except Exception as e: 
            print(e)
            PlaySound(None,SND_ASYNC)
            play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"aknc.wav"),SND_ASYNC)
            play() 
            time.sleep(4)
            print("No INTERNET CONNECTION OR WRONG KEYS....... ")
            cv2.destroyAllWindows()
            stream.release()
            #os.remove(folderPath+"/"+"User0.jpg")
            print("MEMORY FREED....STOPPING PROCESS!!!!") 
            main()
            sys.exit()
            
         print("\nImages uploaded to Bucket for Comparison")
         
         
         try:
          y=real_time_detect(output,stream) 
          
          
          cv2.imshow("FRAME 3",y)
          
         except Exception as e:
             
             print(e)
             cv2.imshow("FRAME 2",output)
             
          #cv2.imshow("FRAME 3",output)
         #cv2.destroyWindow("FRAME 3")
         #cv2.imshow("FRAME 3",output)
          
          
        
         
         
         
         #os.remove(exe+ "\\Output_image" +".jpg")     
           
        else:
            continue
        
            # draw a fancy border around the faces
        
        
        
            
        
        
    # cleanup

if __name__=='__main__':
 surv_detect()
 