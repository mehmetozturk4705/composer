from typing import Generator

import numpy as np

import config
from .base_synth import BaseSynthesizer
from .score_writer import ScoreWriter


class ClarinetSynthesizer(BaseSynthesizer):
    def __init__(self):
        super().__init__()
        self.name = "clarinet"
        self.square_factor = 4

    def synthesize(self, input_data: ScoreWriter) -> Generator[np.array, None, None]:
        """
        Synthesize a clarinet sound.
        :param input_data:
        :return:
        """
        if not isinstance(input_data, ScoreWriter):
            raise TypeError("Input data must be of type ScoreWriter")

        chunk = None
        for freq, duration in input_data.get_score():
            if freq == 0:
                sound = np.zeros((2, int(duration * config.SAMPLE_RATE)), dtype=np.float32)
            else:
                sound = self.get_sound(freq, duration)
            if chunk is not None:
                sound = np.concatenate((chunk, sound), axis=1)
            for i in range(sound.shape[1]//config.CHUNK_SIZE):
                chunk = sound[:, i*config.CHUNK_SIZE:(i+1)*config.CHUNK_SIZE]
                if chunk.shape[1] < config.CHUNK_SIZE:
                    break
                yield chunk

    def get_sound(self, freq, duration):
        """
        Generate a clarinet sound.

        :param freq:
        :param duration:
        :return:
        """
        if not isinstance(freq, int) and not isinstance(freq, float):
            raise TypeError("Frequency must be of type int or float")

        if not isinstance(duration, int) and not isinstance(duration, float):
            raise TypeError("Duration must be of type int or float")

        if freq < 0:
            raise ValueError("Frequency must be greater than or equals to 0")
        if duration <= 0:
            raise ValueError("Duration must be greater than 0")

        initial_sound = np.zeros((2, int(duration * config.SAMPLE_RATE)), dtype=np.float32)
        for i in range(self.square_factor):
            factor = (i * 2) + 1
            initial_sound += np.sin(
                2 * np.pi * freq * factor * np.arange(int(duration * config.SAMPLE_RATE)) / config.SAMPLE_RATE,
                dtype=np.float32) / factor
        return initial_sound
