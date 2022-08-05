import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
from math import sqrt
import win32api
import mouse
 
 
 
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cursor_speed = 1.5
clicks = 0
min_movement = [3,0]
prev_pos = [0,0]
reqdPoints = ['HandLandmark.INDEX_FINGER_TIP','HandLandmark.THUMB_TIP']
monitorDimensions = [win32api.GetSystemMetrics(0),win32api.GetSystemMetrics(1)]
print(monitorDimensions)
 
video = cv2.VideoCapture(0)
 
with mp_hands.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.9) as hands: 
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         
        image = cv2.flip(image, 1)
 
        imageHeight, imageWidth, _ = image.shape
 
        results = hands.process(image)
   
 
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                         )
 
        if results.multi_hand_landmarks != None:
          for handLandmarks in results.multi_hand_landmarks:
            for point in mp_hands.HandLandmark:
 
                point_i=str(point)
                if (point_i not in reqdPoints):
                    continue
    
                normalizedLandmark = handLandmarks.landmark[point]
                
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
    
                point=str(point)
 
                if point=='HandLandmark.INDEX_FINGER_TIP':
                 try:
                    #indexfingertip_x=pixelCoordinatesLandmark[0]
                    indexfingertip_x=int(normalizedLandmark.x*monitorDimensions[0])
                    #indexfingertip_y=pixelCoordinatesLandmark[1]
                    indexfingertip_y=int(normalizedLandmark.y*monitorDimensions[1])
                    new_pos = [int(indexfingertip_x*cursor_speed),int(indexfingertip_y*cursor_speed)]
                    if abs(new_pos[0]-prev_pos[0])>min_movement[0] and abs(new_pos[1]-prev_pos[1])>min_movement[1]:
                        win32api.SetCursorPos(new_pos)
                        prev_pos = new_pos
 
                 except Exception as e:
                    print(e)

                if point=='HandLandmark.MIDDLE_FINGER_TIP':
                 try:
                    middlefingertip_x=int(normalizedLandmark.x*monitorDimensions[0])
                    middlefingertip_y=int(normalizedLandmark.y*monitorDimensions[1])
 
                 except Exception as e:
                    print(e)
 
                if point=='HandLandmark.THUMB_TIP':
                 try:
                    thumbfingertip_x=int(normalizedLandmark.x*monitorDimensions[0])
                    thumbfingertip_y=int(normalizedLandmark.y*monitorDimensions[1])
                    #print("thumb",thumbfingertip_x)
 
                 except:
                    pass
 
                #left click
                try:
                    Distance_x = indexfingertip_x-thumbfingertip_x
                    Distance_y = indexfingertip_y-thumbfingertip_y
                    #print(indexfingertip_x-thumbfingertip_x,indexfingertip_y-thumbfingertip_y)
                    if abs(Distance_x)<20:
                        #print(Distance_y)
                        if abs(Distance_y)<50:
                            clicks+=1
                            if clicks%3 == 0:
                                mouse.click()                            
                except:
                    pass
                #right click
                try:
                    Distance_x = middlefingertip_x-thumbfingertip_x
                    Distance_y = middlefingertip_y-thumbfingertip_y
                    print(Distance_x,Distance_y)
                    #print(indexfingertip_x-thumbfingertip_x,indexfingertip_y-thumbfingertip_y)
                    if abs(Distance_x)<20:
                        #print(Distance_y)
                        if abs(Distance_y)<50:
                            clicks+=1
                            if clicks%3 == 0:
                                mouse.right_click()                            
                except:
                    pass
 
        cv2.imshow('Hand Tracking', image)
 
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
 
video.release()