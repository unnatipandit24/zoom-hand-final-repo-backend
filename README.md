
# Zoom Hand Detection Backend

Real-time hand gesture detection backend for zooming via camera input

## 🚀 Project Overview

Developed a backend system that uses computer vision and gesture recognition to detect “zoom in” and “zoom out” hand gestures and trigger corresponding actions. Built with Python and Flask for lightweight API handling, using MediaPipe (via OpenCV) for hand-tracking and gesture recognition, and integrated machine-learning inference for reliable gesture classification.

## 🔧 Key Features

* Real-time hand tracking using MediaPipe’s hand landmark detection and OpenCV to process video frames.
* Gesture classification logic for zoom in/out actions — enabling touch-free interaction and enhanced user accessibility.
* RESTful API built with Flask to expose endpoints for gesture detection results.
* Modular design with separate utility modules (e.g., `zoom_utils.py`) for maintainability and easy extension.

## 🛠 Tech Stack

| Component           | Technology                                              |
| ------------------- | ------------------------------------------------------- |
| Backend framework   | Python + Flask                                          |
| Computer vision     | OpenCV, MediaPipe Hands                                 |
| Gesture logic       | Custom Python modules (`hand_zoom.py`, `zoom_utils.py`) |
| Dependencies        | Specified in `requirements.txt`                         |
| Runtime environment | Suitable for local machine or containerized deployment  |

## 📂 Project Structure

```
├── app.py             ← Flask application entry‐point  
├── hand_zoom.py       ← Core logic for capturing and interpreting hand gestures  
├── zoom_utils.py      ← Helper functions (e.g., preprocessing, gesture classification)  
├── requirements.txt   ← Python dependencies  
```

## 🎯 Getting Started

### Prerequisites

* Python 3.x installed
* Webcam or camera input device
* Virtual environment (recommended)

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/unnatipandit24/zoom-hand-final-repo-backend.git
   cd zoom-hand-final-repo-backend
   ```
2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Launch the backend server:

   ```bash
   python app.py
   ```

   The API will start (default port 5000). Access via `http://localhost:5000`.

### Usage

* With your webcam enabled and pointing at your hand, the system tracks hand landmarks and determines zoom gestures (in/out).
* The Flask API endpoints will return gesture detection results (e.g., `"zoom_in"`, `"zoom_out"`, `"no_gesture"`) which can be consumed by a front-end or other system for interactive response.

## ✅ Example Response

```json
{
  "status": "success",
  "gesture": "zoom_in",
  "confidence": 0.85
}
```

## 🧪 Testing & Validation

* Test the system by making clear zoom-in (spread fingers) or zoom-out (pinch fingers) gestures in view of the camera.
* Adjust lighting and background to improve detection accuracy for your environment.
* You can enhance the logic by tuning thresholds or adding more gesture categories.

## 📈 Future Enhancements

* Containerize the backend using Docker for easier deployment and scalability.
* Expose WebSocket or streaming endpoints for live video feedback rather than single snapshot API calls.
* Integrate with a front-end (e.g., an Android app) to trigger UI zooming or application control based on detected gestures.
* Add more gesture types (e.g., rotate, swipe) for richer interactive controls.
* Implement model persistence (e.g., using TensorFlow or PyTorch) if a learning-based classifier is introduced.

## 👤 Author

Developed by **Unnati Pandit — Computer Science & AI enthusiast (@ University of Lucknow).
Feel free to explore the code, raise issues, or open pull requests for improvements.

This project is open-source under the [MIT License](LICENSE) (or whichever license you choose to apply).

---

*Thank you for exploring this project — I hope it inspires more creative, gesture-driven interactions!*
