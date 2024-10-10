import cv2
import numpy as np

# Kamera ile görüntü yakala (veya bir video dosyası da kullanılabilir)
cap = cv2.VideoCapture(0)

# Blue renk için genişletilmiş HSV aralığı1
lower_blue_1 = np.array([75, 100, 100])
upper_blue_1 = np.array([130, 255, 255])

lower_blue_2 = np.array([180, 50, 200])
upper_blue_2 = np.array([240, 255, 255])

while True:
    # Kameradan görüntü al
    ret, frame = cap.read()
    
    # Görüntüyü HSV renk uzayına çevir2
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Blue renk için maskeler oluştur3
    mask_1 = cv2.inRange(hsv, lower_blue_1, upper_blue_1)
    mask_2 = cv2.inRange(hsv, lower_blue_2, upper_blue_2)
    
    # Maskeleri birleştir
    mask = cv2.bitwise_or(mask_1, mask_2)
    
    # Maskeyi kullanarak Blue bölgeyi tespit et
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Orijinal görüntü ve sonuçları göster
    cv2.imshow('Orijinal Görüntü', frame)
    cv2.imshow('Mavi Obje Tespiti', result)
    
    # 'q' tuşuna basılana kadar bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Her şey tamamlanınca pencereyi kapat
cap.release()
cv2.destroyAllWindows()