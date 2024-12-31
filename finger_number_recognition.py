import cv2
import mediapipe as mp

# Initialize MediaPipe Hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize webcam
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks, hand_type):
    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4
    fingers = []

    # Thumb logic
    if hand_type == "Right":
        fingers.append(hand_landmarks[thumb_tip].x < hand_landmarks[thumb_tip - 1].x)
    else:
        fingers.append(hand_landmarks[thumb_tip].x > hand_landmarks[thumb_tip - 1].x)

    # Other fingers logic
    for tip in finger_tips:
        fingers.append(hand_landmarks[tip].y < hand_landmarks[tip - 2].y)

    return fingers.count(True)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_index, (hand_landmarks, handedness) in enumerate(zip(result.multi_hand_landmarks, result.multi_handedness)):
            # Draw landmarks and connections
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get hand type and count fingers
            hand_type = handedness.classification[0].label
            num_fingers = count_fingers(hand_landmarks.landmark, hand_type)
            
            # count near the hand
            x = int(hand_landmarks.landmark[0].x * frame.shape[1])
            y = int(hand_landmarks.landmark[0].y * frame.shape[0])
            cv2.putText(frame, f"{hand_type} Hand: {num_fingers} fingers", 
                        (x - 100, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Finger Number Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
