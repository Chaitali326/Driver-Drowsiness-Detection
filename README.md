# 🚗 Driver Drowsiness Detection System

A real-time AI-based Driver Drowsiness Detection System built using Python, OpenCV, and MediaPipe that detects eye closure and yawning to alert sleepy drivers and help prevent accidents.

---

## 📌 Features

✅ Real-time webcam monitoring  
✅ Eye Aspect Ratio (EAR) based drowsiness detection  
✅ Mouth Aspect Ratio (MAR) based yawn detection  
✅ Audio alarm alert system  
✅ Face landmark detection using MediaPipe  
✅ Lightweight and fast performance  
✅ Simple and easy-to-understand implementation  

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core Programming Language |
| OpenCV | Video processing and webcam handling |
| MediaPipe | Facial landmark detection |
| NumPy | Mathematical calculations |
| Pygame | Alarm sound system |
| Threading | Background alarm handling |

---

## 📂 Project Structure

```text
Driver-Drowsiness-Detection/
│
├── Driver_Drowsiness_Detection.py
├── alert.wav
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Chaitali326/Driver-Drowsiness-Detection.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd Driver-Drowsiness-Detection
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv mediapipe_env
```

### 4️⃣ Activate Virtual Environment

#### Windows

```bash
mediapipe_env\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python Driver_Drowsiness_Detection.py
```

---

## 🧠 Working Principle

The system continuously captures webcam frames and performs:

### 👁️ Eye Detection
- Detects eye landmarks using MediaPipe
- Computes Eye Aspect Ratio (EAR)
- If EAR drops below threshold for a certain duration, driver is considered drowsy

### 😮 Yawn Detection
- Detects mouth landmarks
- Computes Mouth Aspect Ratio (MAR)
- Large MAR indicates yawning

### 🔔 Alert System
- Alarm sound is triggered when:
  - Eyes remain closed
  - Excessive yawning detected

---

## 📸 MediaPipe Face Mesh

The project uses MediaPipe Face Mesh with 468 facial landmarks for accurate facial tracking.

### Important Landmark Indices

| Feature | Landmark Points |
|---|---|
| Left Eye | 33, 160, 158, 133, 153, 144 |
| Right Eye | 362, 385, 387, 263, 373, 380 |
| Mouth | 13, 14, 78, 308 |

---

## 📊 Threshold Values

| Parameter | Value |
|---|---|
| Eye Threshold (EAR) | 0.20 |
| Mouth Threshold (MAR) | 0.6 |
| Frame Counter | 20 Frames |

---

## 🚨 Future Improvements

- Head pose estimation
- Mobile app integration
- SMS emergency alert
- Night vision enhancement
- Driver identity recognition
- Deep learning based fatigue analysis

---

## 📷 Output

The system displays:

- Real-time webcam feed
- EAR and MAR values
- Drowsiness warning
- Alarm activation

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit changes
4. Push to branch
5. Open Pull Request

---

## 📜 License

This project is developed for educational and research purposes.

---

## 👩‍💻 Author

**Aditya Modi**
**Ankit Lanjewar**
**Chaitali Nadekar**
**Dhaneswari Bhatia**

GitHub:  
:contentReference[oaicite:0]{index=0}

---

## ⭐ Support

If you liked this project:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others
