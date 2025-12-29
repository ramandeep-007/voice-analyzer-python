import librosa
import matplotlib.pyplot as plt
import numpy as np
def generate_report(sr, duration, energy, pitch, speech_time, silence_time):
    print("\nVOICE ANALYSIS REPORT")
    print("-" * 25)

    print(f"Sample Rate       : {sr} Hz")
    print(f"Total Duration    : {round(duration,2)} seconds")
    print(f"Average Loudness  : {energy:.8f}")
    print(f"Average Pitch     : {round(pitch,2)} Hz")
    print(f"Sound Duration    : {round(speech_time,2)} seconds")
    print(f"Silence Duration  : {round(silence_time,2)} seconds")

    sound_percent = (speech_time / duration) * 100
    print(f"Sound Percentage  : {round(sound_percent,2)} %")

    if pitch > 1000:
        print("Pitch Type        : High / Non-voice sound")
    elif pitch > 300:
        print("Pitch Type        : Medium pitch")
    else:
        print("Pitch Type        : Low pitch")

    if energy < 0.001:
        print("Loudness Level    : Quiet recording")
    else:
        print("Loudness Level    : Loud recording")


y,sr=librosa.load("audio\Recording.wav")

duration=len(y)/sr
plt.figure(figsize=(10,5))
plt.plot(y)
plt.title("Waveform of an audio")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.show()

energy=np.mean(y**2)

pitches,magnitude=librosa.piptrack(y=y,sr=sr)
pitch_values=pitches[pitches>0]
avg_pitch=pitch_values.mean()

intervals=librosa.effects.split(y,top_db=20)
speech_time=0

for i,j in intervals:
    speech_time+=(j-i)/sr
silence_time=duration-speech_time

generate_report(sr, duration, energy, avg_pitch, speech_time, silence_time)