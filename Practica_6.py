import cv2
import numpy as np

video = cv2.VideoCapture(0)

rojoBajo1 = np.array([0,100,20], np.uint8)
rojoAlto1 = np.array([8,255,255], np.uint8)

rojoBajo2 = np.array([175,100,20], np.uint8)
rojoAlto2 = np.array([179,255,255], np.uint8)

azulBajo1 = np.array([94,100,20], np.uint8)
azulAlto1 = np.array([126,255,255], np.uint8)

verdeBajo1 = np.array([35,100,20], np.uint8)
verdeAlto1 = np.array([75,255,255], np.uint8)


while True:
    ret,frame = video.read()
    if ret==True:
        frame_hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #Se genera una mascara con el rango de color ROJO
        mascara1_roja=cv2.inRange(frame_hsv, rojoBajo1, rojoAlto1)
        mascara2_roja=cv2.inRange(frame_hsv, rojoBajo2, rojoAlto2)
        mascara_roja=cv2.add(mascara1_roja, mascara2_roja)
        #                Detección de color Rojo 
        #Todo valor que está en el rango de la mascara se muestra 
        solo_rojo=cv2.bitwise_and(frame, frame, mask=mascara_roja)
        #                Supreción de color Rojo
        #Se muestra todo lo que está fuera del rango de la mascara
        mascara_sin_rojo=cv2.bitwise_not(mascara_roja)
        sin_rojo=cv2.bitwise_and(frame, frame, mask=mascara_sin_rojo)


        #Se genera una mascara con el rango de color VERDE
        mascara_verde=cv2.inRange(frame_hsv, verdeBajo1, verdeAlto1)
        #                Detección de color Verde
        #Todo valor que está en el rango de la mascara se muestra 
        solo_verde=cv2.bitwise_and(frame, frame, mask=mascara_verde)
        #                Supreción de color Verde
        #Se muestra todo lo que está fuera del rango de la mascara
        mascara_sin_verde=cv2.bitwise_not(mascara_verde)
        sin_verde=cv2.bitwise_and(frame, frame, mask=mascara_sin_verde)


        #Se genera una mascara con el rango de color AZUL
        mascara_azul=cv2.inRange(frame_hsv, azulBajo1, azulAlto1)
        #                Detección de color Azul
        #Todo valor que está en el rango de la mascara se muestra 
        solo_azul=cv2.bitwise_and(frame, frame, mask=mascara_azul)
        #                Supreción de color Azul
        #Se muestra todo lo que está fuera del rango de la mascara
        mascara_sin_azul=cv2.bitwise_not(mascara_azul)
        sin_azul=cv2.bitwise_and(frame, frame, mask=mascara_sin_azul)

        cv2.imshow('frame', frame)

        cv2.imshow('Mascara BINARIA Roja', mascara_roja)
        cv2.imshow('Mascara SOLO Rojo', solo_rojo)
        cv2.imshow('Mascara SIN Rojo', sin_rojo)

        cv2.imshow('Mascara BINARIA Verde', mascara_verde)
        cv2.imshow('Mascara SOLO Verde', solo_verde)
        cv2.imshow('Mascara SIN Verde', sin_verde)

        cv2.imshow('Mascara BINARIA Azul', mascara_azul)
        cv2.imshow('Mascara SOLO Azul', solo_azul)
        cv2.imshow('Mascara SIN Azul', sin_azul)

        if cv2.waitKey(1) & 0xFF== ord('s'):
            break

video.release()        
cv2.destroyAllWindows()