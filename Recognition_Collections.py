
def real_time_detect(output,stream):
    global x
    import os
    import boto3
    import cv2
    import sys
    from winsound import PlaySound,SND_ASYNC
    from Login_surv import initiate_surv
    import time
    from Face_Recognition_App import main
    
    from PIL import Image
    folderName = "user2"    
    folderPath = os.path.join(os.path.dirname(os.path.realpath('__file__')), folderName)
    folderName1 = "Suspected"                                      # creating the person or user folder
    
    folderPath1 = os.path.join(os.path.dirname(os.path.realpath('__file__')), folderName1)
    
    image=Image.open(folderPath+"\\"+"User0.jpg")
    imgWidth, imgHeight = image.size  
    print(imgWidth, imgHeight )
    ids = []
    names = []  
    c='project2'
    
    try:
        client = boto3.client('rekognition')
        
        response = client.index_faces(
        CollectionId = 'project2',
        Image={
            'S3Object': {
                'Bucket': 'finals1',
                'Name': 'User0.jpg',
            }
        },
        ExternalImageId='.....',
        DetectionAttributes=[
            'ALL',
        ]
        )
        
    
    
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
             except Exception as e: 
              print(e)
              print(response['FaceRecords'][i]['Face'])
              height = response['FaceRecords'][i]['Face']['BoundingBox']['Height'] 
              width = response['FaceRecords'][i]['Face']['BoundingBox']['Width']
              top = response['FaceRecords'][i]['Face']['BoundingBox']['Top']
              left = response['FaceRecords'][i]['Face']['BoundingBox']['Left']
              x1 = int(imgWidth *left)
              x2 = int(imgHeight *top)
              y1 = int(imgWidth * width)
              y2 = int(imgHeight * height)
              try:
                   client.delete_faces(
                   CollectionId = c,
                   FaceIds = ids,
                    )
              except Exception as e:
                  print(e)
                  continue
                         #print(response['FaceMatches'][0]['Face']['ExternalImageId'])
              x = cv2.imread(folderPath+"\\"+"User0.jpg")
              cv2.putText(x,"UNKNOWN", (x1,x2-20), cv2.FONT_HERSHEY_SIMPLEX,.6,(0,255,0),1)
              
              PlaySound(None,SND_ASYNC)
              play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"beep.wav"),SND_ASYNC)
              play()            
              x = cv2.rectangle(x, (x1,x2), (y1+x1,x2+y2), (0,0,255), 2)
              cv2.imwrite(folderPath+"\\User0" + ".jpg",x)
              z=time.localtime()
              print(folderPath1+"\\%d-%d-%d(%d:%d:%d)"%(z[2],z[1],z[0],z[3],z[4],z[5]) + ".jpg")
              
              cv2.imwrite(folderPath1+"\\"+"%d-%d-%d(%d:%d:%d)"%(z[2],z[1],z[0],z[3],z[4],z[5]) + ".jpg",x)
              continue  
            
             #print(names)      
             #print("ye neeche:")
             #print(response1)  
             
             #try:
                 #
                     #names.append(response1['FaceMatches'][i]['Face']['ExternalImageId'])
                     #print(response1['FaceMatches'][i]['Face']['ExternalImageId'])
             text_name=response1['FaceMatches'][0]['Face']['ExternalImageId'].upper()
                         
             height = response['FaceRecords'][i]['Face']['BoundingBox']['Height'] 
             width = response['FaceRecords'][i]['Face']['BoundingBox']['Width']
             top = response['FaceRecords'][i]['Face']['BoundingBox']['Top']
             left = response['FaceRecords'][i]['Face']['BoundingBox']['Left']
             x1 = int(imgWidth *left)
             x2 = int(imgHeight *top)
             y1 = int(imgWidth * width)
             y2 = int(imgHeight * height)
              
             try:
                   client.delete_faces(
                   CollectionId = c,
                   FaceIds = ids,
                    )
             except Exception as e:
                  print(e)
                  continue            
             x = cv2.imread(folderPath+"\\"+"User0.jpg")
             cv2.putText(x,text_name, (x1,x2-20), cv2.FONT_HERSHEY_SIMPLEX,.6,(0,255,0),1)
                         
             x = cv2.rectangle(x, (x1,x2), (y1+x1,x2+y2), (255,0,0), 2)
             cv2.imwrite(folderPath+"\\User0" + ".jpg",x)
             
             
    except Exception as e: 
       
     print(e)
     
     
     PlaySound(None,SND_ASYNC)
     play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"nerrta.wav"),SND_ASYNC)
     play() 
     
     cv2.destroyAllWindows()
     
     initiate_surv() 
     sys.exit()
    print("yaha 3 ids:",ids) 
    try:
         client.delete_faces(
         CollectionId = c,
         FaceIds = ids,
         )
    except Exception as e: 
             print(e)
             #print("No one in Camera!")
             cv2.destroyWindow("FRAME 3")
             
             del x
             #cv2.imshow("FRAME 3",output)
    print(names)
    key = cv2.waitKey(1) & 0xFF 
        # press r to break out of the loop
    if key ==27:
            try:
                   client.delete_faces(
                   CollectionId = c,
                   FaceIds = ids,
                    )
                   print("yaha ids deleted exit:",ids)
            except Exception as e:
                  print(e)
                  pass  
            PlaySound(None,SND_ASYNC)
            play = lambda: PlaySound(os.path.join(os.path.dirname(os.path.realpath('__file__')),"tm.wav"),SND_ASYNC)
            play()
            time.sleep(1)
            
            cv2.destroyAllWindows()
            stream.release()
            main()
            return
   try:
       
     return x
    except Exception as e: 
         print(e)
         print("None here , so return!")
         
         return None
if __name__=='__main__':
 real_time_detect(output,stream)
     
    


