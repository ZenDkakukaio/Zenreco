import  cv2
import numpy  as np
import tensorflow as tf
from keras.models import load_model
import mediapipe as mp
import serial
import serial.tools.list_ports
import pyttsx3
import webbrowser



class ZenReco():
    def __init__(self):
        self.list_talk = ["ouverture de facebook", "ouverture de youtube", "bonjour comment vous allez"]


    def start_recognition(self):
        #initialisation des modèles

        #initialisation de mediapipe

        #algo de reconnaissance des mains
        mpHands = mp.solutions.hands

        mains = mpHands.Hands(max_num_hands = 1, min_detection_confidence=0.7)

        mpDraw = mp.solutions.drawing_utils




        #initialiser tensorflow
        #charger le modele de reconnaissance de gestes
        model = load_model("mp_hand_gesture")

        #charger les noms de classe
        f = open("zen_gesture.names", "r")

        classNames = f.read().split('\n')
        f.close()


        #lire les images d'une webcam

        cap = cv2.VideoCapture(0)

        while True:
            # lire chaque image de la webcam
            _, frame = cap.read()

            x, y, c = frame.shape

            # retourner le cadre verticalement
            frame = cv2.flip(frame, 1)
            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # obtenir la prédiction du point de repere de la main
            result = mains.process(framergb)

            # print(result)

            className = ''

            # post traiter le résultat
            if result.multi_hand_landmarks:
                landmarks = []
                for handslms in result.multi_hand_landmarks:
                    for lm in handslms.landmark:
                        # print(id, lm)
                        lmx = int(lm.x * x)
                        lmy = int(lm.y * y)

                        landmarks.append([lmx, lmy])

                    # Dessiner les reperes sur le cadre
                    mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

                    # Predire la gestuelle de la main
                    prediction = model.predict([landmarks])
                    # print(prediction)
                    classID = np.argmax(prediction)  #recuperer les indices de elements maximals definit depuis une surface en fonction des axes specifiés
                    className = classNames[classID]

            # afficher la prédiction sur le cadre
            cv2.putText(frame, className, (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)


            if className == "dire bonjour":
                engine_voice = pyttsx3.init('sapi5')
                engine_voice.say(self.list_talk[2])
                engine_voice.runAndWait()



            elif className == "ouvrir facebook":
                engine_voice = pyttsx3.init('sapi5')
                engine_voice.say(self.list_talk[0])
                engine_voice.runAndWait()
                webbrowser.open("https://www.facebook.com")




            elif className == "ouvrir youtube":
                engine_voice = pyttsx3.init('sapi5')
                engine_voice.say(self.list_talk[1])
                webbrowser.open("https://www.youtube.com")
                engine_voice.runAndWait()

                # while True:
                #     baud = 9600
                #     ports = serial.tools.list_ports.comports()
                #     for port in ports:
                #         arduino = serial.Serial("COM2", baud, bytesize=8, timeout=1)
                #     message = 6
                #     str_message = str(message)
                #     binary_result = ''.join(format(ord(c), 'b') for c in str_message)
                #     arduino.write(int(binary_result))

            else:
                print("aucun signe detecte")



            # afficher la sortie finale
            cv2.imshow("ZENRECO", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        # liberer la webcam et detruire toutes les fenêtres actives
        cap.release()

        cv2.destroyAllWindows()



