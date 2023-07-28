import matplotlib.pyplot as plt, numpy as np
import wave

wave

f_1 = 4
f_2 = 8
t_max = 12

wv = lambda f: np.array(np.sin(2 * np.pi * f * np.linspace(0, t_max, 2000, endpoint=True)))

# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0

# wav_obj = wave.open("C:/Users/CSC/Desktop/2023-06-18 04-24-54.wav", 'r')
wav_obj = wave.open("C:/Users/CSC/Desktop/440.wav", 'r')

sample_freq = wav_obj.getframerate()
# print(sample_freq)

n_samples = wav_obj.getnframes()
# print(n_samples)

t_max = n_samples/sample_freq
print(t_max, "seconds")

signal_wave = wav_obj.readframes(n_samples)
wav_obj.close()

p = np.frombuffer(signal_wave, dtype=np.int16)
p = p[0:-1:1000]

# p = wv(f_1) + wv(f_2)

nN = len(p)
print(nN)
amp = np.zeros(nN)

base = np.e ** (-2j * np.pi * np.linspace(0, 1, nN) * t_max)

# for f in range(nN):
#     amp[f] = np.abs(np.dot(p, base ** f))

amp = np.array([np.abs(np.dot(p, base ** f)) for f in range(nN)])

# amp = np.fft.fft(p)

plt.plot(amp / nN)
plt.xlim(0, 250)
plt.show()