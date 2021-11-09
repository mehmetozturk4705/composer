from time import sleep

import sounddevice as sd
import numpy as np

if __name__ == '__main__':
    sd.play(np.sin(
                2 * np.pi * 440 * np.arange(int(1 * 44100)) / 44100,
                dtype=np.float32), samplerate=44100, blocking=True)

