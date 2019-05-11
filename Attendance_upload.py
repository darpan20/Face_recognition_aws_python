
def xmain():
 from winsound import PlaySound,SND_ASYNC
 from Recognition_menu import app
 from Face_Recognition_App import main
 import cv2 
 import pymysql
 import os 
 import boto3
 import pygame
 from Excel import excel
 import sys
 pygame.mixer.init()
 import time
 #s1=pygame.mixer.Sound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"ca.wav"))
 PlaySound(None,SND_ASYNC)
 s3 = boto3.client('s3')
 client = boto3.client('rekognition')
 bucket_name = 'finala'
 rds_host  = "rootsapp-rds-instance.caynmze7tthq.ap-south-1.rds.amazonaws.com"
 name = "rootsapp"
 password = "rootsapp"
 db_name = "rootsapp_database"
 play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"ca.wav"),SND_ASYNC)

 print("----------------FACE DETECTION OPENS--------------------")
 stream = cv2.VideoCapture(0)
 
 folderName2 = "Attendance"  
 folderName = "user1"                                                        # creating the person or user folder
 folderPath = os.path.join(os.path.dirname(os.path.realpath('__file__')), folderName)
 folderPath2 = os.path.join(os.path.dirname(os.path.realpath('__file__')), folderName2)
 if not os.path.exists(folderPath):
    os.makedirs(folderPath)
 fileList = os.listdir(folderPath)

 j=0 
 while True:
    # read frames from live web cam stream
    (grabbed, frame) = stream.read(0)
    frame = cv2.flip(frame, 1)
    cv2.namedWindow("Face Detection", cv2.WND_PROP_FULLSCREEN)  
    cv2.moveWindow("Face Detection",0,0) #????????        
    cv2.setWindowProperty("Face Detection", cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    
    cv2.imshow("Face Detection",frame)
    key = cv2.waitKey(1) & 0xFF
    if grabbed==True:
     if key == ord("s"): 
        cv2.imwrite(folderPath + "/User" +("%s"%j)+ ".jpg",
                    frame)
        play()
        break
    
    
 
    
    if key ==27:
        PlaySound(None,SND_ASYNC)
        play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"tq.wav"),SND_ASYNC)
        play()
        time.sleep(1)
        print("\n%s memory freed "%folderPath)
        print("---RETURNING TO MAIN WINDOW")
        
        for fileName in fileList:
         os.remove(folderPath+"/"+fileName)
        cv2.destroyAllWindows()
        stream.release()
        main()
        
 
# cleanup
 cv2.destroyAllWindows()
 stream.release()

 for filename in os.listdir(folderPath):
    try:
     s3.upload_file('user1/User0.jpg', bucket_name,filename)
     
     
    except:
        print("No INTERNET CONNECTION OR WRONG KEYS....... ")
        PlaySound(None,SND_ASYNC)
        play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"aknc.wav"),SND_ASYNC)
        play() 
        time.sleep(4)
        for fileName in fileList:
         os.remove(folderPath+"/"+fileName)
        print("MEMORY FREED....STOPPING PROCESS!!!!") 
        main()
 
 os.remove(folderPath+"/"+"User0.jpg")   
 print("\nImages uploaded to Bucket for Comparison")
 PlaySound(None,SND_ASYNC)
 play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"ur.wav"),SND_ASYNC)
 play() 
 c = 'project1'
 try:
     response = client.index_faces(
     CollectionId = c,
     Image={
         'S3Object': {
             'Bucket': 'finala',
             'Name': 'User0.jpg',
         }
     },
     ExternalImageId='saare',
     DetectionAttributes=[
         'ALL',
     ]
     )
     ids = []
     names = []
    
     for i in range(len(response['FaceRecords'])):
         ids.append(response['FaceRecords'][i]['Face']['FaceId'])
         response1 = client.search_faces(
                 CollectionId = c,
                 FaceId = response['FaceRecords'][i]['Face']['FaceId'],
                 FaceMatchThreshold = 80,
                 MaxFaces = 100,
                 )
         try:
             names.append(response1['FaceMatches'][0]['Face']['ExternalImageId'])
             
         except:
             
             continue
     try:    
      client.delete_faces(
         CollectionId = c,
         FaceIds = ids,
      )
     except Exception as e:
         print(e)
         PlaySound(None,SND_ASYNC)
         play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"nfd.wav"),SND_ASYNC)
         play() 
         app()
         sys.exit()
 except Exception as e:
     print(e)
         
     PlaySound(None,SND_ASYNC)
     play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"nerrta.wav"),SND_ASYNC)
     
     play() 
     app()
     sys.exit()
 print(names)

 try:
  for i in names:
     conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=3)
     print(i)
     with conn.cursor() as cur:
         cur.execute("""insert into testing_only (name) values( '%s') """ % (i))
         conn.commit()
         cur.close()
 except Exception as e:
     print(e)
     PlaySound(None,SND_ASYNC)
     play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"nerrta.wav"),SND_ASYNC)
     play() 
     app()
     sys.exit()
 excel(names)    
 PlaySound(None,SND_ASYNC)
 play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"pc.wav"),SND_ASYNC)
 play()
 os.startfile(folderPath2+"\\"+"Attendance_Register.xlsx")
 app()
       

if __name__=='__main__':
 xmain()   
 