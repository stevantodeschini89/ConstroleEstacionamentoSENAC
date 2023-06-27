import cv2
import numpy as np

vaga1 = [174, 235,  46,  90]
vaga2 = [218, 236,  52,  88]
vaga3 = [271, 238,  48,  83]
vaga4 = [320, 240,  49,  85]
vaga5 = [373, 241,  47,  85]
vaga6 = [424, 241,  50,  88]
vaga7 = [477, 240,  50,  83]
vaga8 = [532, 241,  48,  79]
vaga9 = [587, 240,  45,  81]
vaga10 = [637, 241,  47,  86]
vaga11 = [691, 241,  46,  80]
vaga12 = [749, 241,  44,  82]
vaga13 = [796, 240,  48,  89]
vaga14 = [851, 243,  46,  77]
vaga15 = [905, 244,  46,  84]
vaga16 = [584, 440,  45,  94]
vaga17 = [636, 440,  45,  84]
vaga18 = [692, 439,  42,  93]
vaga19 = [745, 441,  44,  87]
vaga20 = [797, 440,  45,  88]
vaga21 = [851, 439,  44,  87]
vaga22 = [903, 439,  47,  83]
vaga23 = [903, 550,  43,  92]
vaga24 = [848, 553,  44,  86]
vaga25 = [793, 552,  48,  93]
vaga26 = [743, 554,  42,  82]
vaga27 = [687, 553,  48,  88]
vaga28 = [637, 552,  48,  87]
vaga29 = [583, 552,  44,  82]


vagas = [vaga1, vaga2, vaga3, vaga4, vaga5, vaga6, vaga7, vaga8, vaga9, vaga10, vaga11, vaga12, vaga13, vaga14, vaga15, vaga16, vaga17, vaga18, vaga19, vaga20, vaga21, vaga22, vaga23, vaga24, vaga25, vaga26, vaga27, vaga28, vaga29]
video = cv2.VideoCapture('C:\\Users\\User\\OneDrive\\Área de Trabalho\\Projeto Estacionamento\\carPark.mp4')

while True:
    check, img = video.read()
    if not check:
        break

    imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(imgCinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgBlur = cv2.medianBlur(imgTh, 5)
    kernel = np.ones((3, 3), np.int8)
    imgDil = cv2.dilate(imgBlur, kernel)

    qtVagasAbertas = 0
    for x, y, w, h in vagas:
        recorte = imgDil[y:y+h, x:x+w]
        qtPxBranco = cv2.countNonZero(recorte)
        cv2.putText(img, str(qtPxBranco), (x, y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if qtPxBranco > 1000:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
        else:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            qtVagasAbertas += 1

    cv2.rectangle(img, (90, 0), (415, 60), (255, 0, 0), -1)
    cv2.putText(img, f'LIVRE: {qtVagasAbertas}/29', (95, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5)

    cv2.imshow('video', img)
    cv2.imshow('imgDil', imgDil)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
