# 🎤 Voice Analyzer (Python)

A Python-based voice analysis tool that extracts meaningful information from an audio file such as duration, loudness, pitch, and silence vs sound time using real-world audio processing libraries.

This is my **first audio analysis project**, built during my **first semester**, to understand how sound can be represented and analyzed using Python.

---

## 📌 Features

- Load and process `.wav` audio files  
- Calculate audio duration and sample rate  
- Visualize audio waveform  
- Measure overall loudness (energy)  
- Estimate average pitch of the sound  
- Detect sound vs silence duration  
- Generate a clean, human-readable analysis report  

---

## 🛠️ Technologies Used

- **Python**
- **librosa** – audio processing
- **numpy** – numerical computation
- **matplotlib** – waveform visualization

---

## 📂 Project Structure

voice-analyzer-python/
│
├── audio/
│ └── mixkit-footsteps-on-tall-grass-532.wav
│
├── main.py
└── README.md


---

## ▶️ How to Run the Project

### 1️⃣ Install required libraries

```bash
pip install librosa numpy matplotlib soundfile
```

### 2️⃣ Place your audio file

Add a .wav file inside the audio/ folder

Update the file path in main.py if needed

### 3️⃣ Run the script
```bash
python main.py
```

### Sample output
```bash
VOICE ANALYSIS REPORT
--------------------
Sample Rate       : 22050 Hz
Total Duration    : 23.10 seconds
Average Loudness  : 0.00001492
Average Pitch     : 2014.44 Hz
Sound Duration    : 12.40 seconds
Silence Duration  : 10.70 seconds
Sound Percentage  : 53.7 %
Pitch Type        : High / Non-voice sound
Loudness Level    : Quiet recording
```
