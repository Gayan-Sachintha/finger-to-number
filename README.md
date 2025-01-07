# Finger Number Recognition System

This project is a real-time finger counting system using OpenCV and MediaPipe. It uses a webcam to detect hands, count the number of extended fingers, and display the result.

---

## Features

- Real-time hand detection and finger counting.
- Supports both left and right hands.
- Simple and intuitive interface with live webcam feed.
- Uses MediaPipe for efficient hand tracking and OpenCV for visualization.

---

## Setup Instructions

### Prerequisites

- Python 3.6+
- OpenCV
- MediaPipe

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/finger-number-recognition.git
   cd finger-number-recognition
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install opencv-python mediapipe
   ```

4. Run the project:
   ```bash
   python finger_recognition.py
   ```

---

## How to Use

1. **Launch the Application:** Run the script using `python finger_recognition.py`.
2. **Show Your Hand:** Hold your hand in front of the webcam.
3. **View the Results:** The application detects the number of fingers extended and displays the count near the detected hand.
4. **Exit the Application:** Press the `Q` key to quit the program.

---

## Project Structure

```plaintext
.
├── finger_recognition.py    # Main script for finger counting
├── README.md                # Project documentation
```

---

## Pros and Cons

### Pros
- Lightweight and easy to set up.
- Uses modern hand-tracking technology (MediaPipe).
- Works in real-time with high accuracy.

### Cons
- Requires good lighting for optimal hand detection.
- Limited to finger counting; no additional gesture recognition.
- Performance depends on webcam quality.

---

## Future Enhancements
- Add support for gesture recognition beyond finger counting.
- Include multi-hand tracking and finger counting for multiple users.
- Optimize for low-light conditions.
- Package the application for cross-platform deployment.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
