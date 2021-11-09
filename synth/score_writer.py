import config


class ScoreWriter(object):
    """
    ScoreWriter is a class for representing scores in beat format. 60 bpm is default where every beat takes 1 second.
    """
    __NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    __BASE_NOTE = 9
    __BASE_OCTAVE = 4

    def __init__(self, bpm=60):
        self.__score = []
        self.__bpm = bpm

    def calculate_freq(self, note, octave):
        if note not in self.__NOTES:
            raise ValueError("Invalid note")
        if octave < 0:
            raise ValueError("Invalid octave")
        note_val = self.__NOTES.index(note)
        return config.BASE_FREQ * (2 ** ((note_val - self.__BASE_NOTE) / 12)) * (2 ** (octave - self.__BASE_OCTAVE))

    def write_note(self, note, octave, duration):
        if duration <= 0:
            raise ValueError("Invalid duration")
        elif not isinstance(duration, float) and not isinstance(duration, int):
            raise TypeError("Duration must be a float or integer")
        if octave < 0:
            raise ValueError("Invalid octave")

        freq = self.calculate_freq(note, octave)
        self.__score.append((freq, duration))

    def write_rest(self, duration):
        if duration <= 0:
            raise ValueError("Invalid duration")
        elif not isinstance(duration, float) and not isinstance(duration, int):
            raise TypeError("Duration must be a float or integer")
        self.__score.append((0, duration))

    def get_score(self):
        return self.__score

    def clear_score(self):
        self.__score = []

    def write_score_with_freq(self, score):
        if not isinstance(score, list):
            raise TypeError("Score must be a list")
        for freq, duration in score:
            if not isinstance(freq, float) and not isinstance(freq, int):
                raise TypeError("Frequency must be a float or integer")
            if duration <= 0:
                raise ValueError("Invalid duration")
            if freq < 0:
                raise ValueError("Invalid frequency")
            self.__score.append((freq, duration))
        self.__score = score
