import sounddevice
from scripy.io.wavfile import write

#sample write

fs=44100

#ask to enter ypur desired time for the recording

second = int(input("Enter the recording time in seconds: "))


print("Recording...\n")
record_voice + sounddevice.record(int(second * fs),samplerate=fs,channels=2)

sounddevice.wait()

write("My recording.wav",fs,record_voice)

print("Done! Your audio file is saved as 'My Recording.wav").