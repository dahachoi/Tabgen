import subprocess
import os

import librosa
import librosa.display
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import demucs.separate

input_audio = "AudioFiles/Songs_and_Samples/Birds of a feather.mp3"  # Replace with your audio file path
output_directory = "AudioFiles/Seperated_Stems/BIRDS OF A FEATHER"         # Directory to save the stems


demucs.separate.main(["--mp3", "-n", "mdx_extra", input_audio])


#Audio for Summer Tracks
# bass_path = "SeperatedAudioStems/bass.wav"
# bass_signal, sr = librosa.load(bass_path, sr=None)
# ipd.Audio(filename=bass_path, rate=sr)

# plt.figure(figsize=(15, 17))
# plt.subplot(3, 1, 1)
# librosa.display.waveshow(bass_signal, alpha=0.5)
# plt.title("Bass of Summer")
# plt.ylim((-1, 1))
# plt.show()

# #drums_path = "Outputfile/htdemucs/Summer/drums.wav"

# drums_path = "SeperatedAudioStems/drums.wav"
# drums_signal, sr = librosa.load(drums_path, sr=None)

# plt.figure(figsize=(15, 17))
# plt.subplot(3, 1, 1)
# librosa.display.waveshow(drums_signal, alpha=0.5)
# plt.title("Drums of Summer")
# plt.ylim((-1, 1))
# plt.show()


# other_path = "SeperatedAudioStems/Summer/other.wav"
# other_signal, sr = librosa.load(other_path, sr=None)

# plt.figure(figsize=(15, 17))
# plt.subplot(3, 1, 1)
# librosa.display.waveshow(other_signal, alpha=0.5)
# plt.title("Other of Summer")
# plt.ylim((-1, 1))
# plt.show()

# vocal_path = "Outputfile/htdemucs/Summer/vocals.wav"
# vocal_signal, sr = librosa.load(vocal_path, sr=None)

# plt.figure(figsize=(15, 17))
# plt.subplot(3, 1, 1)
# librosa.display.waveshow(vocal_signal, alpha=0.5)
# plt.title("Vocals of Summer")
# plt.ylim((-1, 1))
# plt.show()

# # Keep durations
# start_time = 50
# end_time = 51
# duration = end_time - start_time

# start_sample = int (start_time * sr)
# end_sample = int(end_time * sr)
# vocal_audio_segment = vocal_signal[start_sample:end_sample]

# plt.figure(figsize=(15, 17))
# plt.subplot(3, 1, 1)
# librosa.display.waveshow(vocal_audio_segment, alpha=0.5)
# plt.title("Summer Vocals 50 ~ 51")
# plt.ylim((-1, 1))
# plt.show()

# #Fourier Transform
# vocal_ft = sp.fft.fft(vocal_audio_segment)
# magnitude = np.absolute(vocal_ft)
# frequency = np.fft.fftfreq(len(magnitude), 1 / sr)

# plt.figure(figsize=(15, 8))
# plt.plot(frequency[:5000], magnitude[:5000]) #magnitude spectrum 
# plt.xlim(0, 4000)  # Set x-axis limits to 0–300 Hz
# plt.xlabel("Frequency (Hz)")
# plt.ylabel("Magnitude")
# plt.title("Fourier Transform Vocals of Summer 50 ~ 51")
# plt.show()


# NOTE_FREQUENCIES = {
#     "C0": 16.35, "C#0": 17.32, "D0": 18.35, "D#0": 19.45, "E0": 20.60, "F0": 21.83, "F#0": 23.12, "G0": 24.50, "G#0": 25.96, "A0": 27.50, "A#0": 29.14, "B0": 30.87,
#     "C1": 32.70, "C#1": 34.65, "D1": 36.71, "D#1": 38.89, "E1": 41.20, "F1": 43.65, "F#1": 46.25, "G1": 49.00, "G#1": 51.91, "A1": 55.00, "A#1": 58.27, "B1": 61.74,
#     "C2": 65.41, "C#2": 69.30, "D2": 73.42, "D#2": 77.78, "E2": 82.41, "F2": 87.31, "F#2": 92.50, "G2": 98.00, "G#2": 103.83, "A2": 110.00, "A#2": 116.54, "B2": 123.47,
#     "C3": 130.81, "C#3": 138.59, "D3": 146.83, "D#3": 155.56, "E3": 164.81, "F3": 174.61, "F#3": 185.00, "G3": 196.00, "G#3": 207.65, "A3": 220.00, "A#3": 233.08, "B3": 246.94,
#     "C4": 261.63, "C#4": 277.18, "D4": 293.66, "D#4": 311.13, "E4": 329.63, "F4": 349.23, "F#4": 369.99, "G4": 392.00, "G#4": 415.30, "A4": 440.00, "A#4": 466.16, "B4": 493.88,
#     "C5": 523.25, "C#5": 554.37, "D5": 587.33, "D#5": 622.25, "E5": 659.25, "F5": 698.46, "F#5": 739.99, "G5": 783.99, "G#5": 830.61, "A5": 880.00, "A#5": 932.33, "B5": 987.77,
#     "C6": 1046.50, "C#6": 1108.73, "D6": 1174.66, "D#6": 1244.51, "E6": 1318.51, "F6": 1396.91, "F#6": 1479.98, "G6": 1567.98, "G#6": 1661.22, "A6": 1760.00, "A#6": 1864.66, "B6": 1975.53,
#     "C7": 2093.00, "C#7": 2217.46, "D7": 2349.32, "D#7": 2489.02, "E7": 2637.02, "F7": 2793.83, "F#7": 2959.96, "G7": 3135.96, "G#7": 3322.44, "A7": 3520.00, "A#7": 3729.31, "B7": 3951.07,
#     "C8": 4186.01
# }

# # Convert a frequency to the closest note
# def frequency_to_note(frequency):
#     if frequency < min(NOTE_FREQUENCIES.values()) or frequency > max(NOTE_FREQUENCIES.values()):
#         return None  # Out of the audible range for standard notes
#     closest_note = min(NOTE_FREQUENCIES, key=lambda note: abs(NOTE_FREQUENCIES[note] - frequency))
#     return closest_note

# def filter_unique_prominent_notes(frequencies, magnitudes):
#     note_magnitude_map = {}

#     # Map frequencies to notes and their magnitudes
#     for freq, mag in zip(frequencies, magnitudes):
#         note = frequency_to_note(freq)  # Convert frequency to closest note
#         if note:
#             root_note = note[:-1]  # Get the root note (e.g., "C" from "C4")
#             # Keep only the most prominent magnitude for each root note
#             if root_note not in note_magnitude_map or mag > note_magnitude_map[root_note][1]:
#                 note_magnitude_map[root_note] = (note, mag)

#     # Extract the most prominent notes, sorted by intensity (magnitude)
#     sorted_notes = sorted(note_magnitude_map.values(), key=lambda item: item[1], reverse=True)
#     return [note for note, _ in sorted_notes]


# positive_frequencies = frequency[:len(frequency)//2]
# positive_magnitude = magnitude[:len(magnitude)//2]

# # Find the prominent frequencies (peaks)
# threshold = 0.1 * max(positive_magnitude)  # Set a threshold for prominence
# prominent_indices = np.where(positive_magnitude > threshold)[0]
# prominent_frequencies = positive_frequencies[prominent_indices]
# notes = [frequency_to_note(freq) for freq in prominent_frequencies]

# filtered_prominent_notes = filter_unique_prominent_notes(prominent_frequencies, magnitude)

# #print("Corresponding Notes:", notes)
# print("Frequencies for summer vocal 50 ~ 51:", filtered_prominent_notes)

