import unittest

from synth.score_writer import ScoreWriter


class TestScoreWriter(unittest.TestCase):
    def test_write_score(self):
        score_writer = ScoreWriter()
        score_writer.write_note("A", 4, 1)
        score_writer.write_note("A", 3, 1)
        score_writer.write_note("A", 2, 1)
        score_writer.write_rest(1)
        score = score_writer.get_score()
        # Test that the score is correct
        self.assertAlmostEqual(score[0][0], 440, delta=0.1)
        self.assertAlmostEqual(score[1][0], 220, delta=0.1)
        self.assertAlmostEqual(score[2][0], 110, delta=0.1)
        self.assertAlmostEqual(score[3][0], 0, delta=0.1)
        # Test that the duration is correct
        self.assertAlmostEqual(score[0][1], 1, delta=0.1)
        self.assertAlmostEqual(score[1][1], 1, delta=0.1)
        self.assertAlmostEqual(score[2][1], 1, delta=0.1)
        self.assertAlmostEqual(score[3][1], 1, delta=0.1)

        # Test write_note with error
        with self.assertRaises(ValueError):
            score_writer.write_note("A", -1, 1)

        with self.assertRaises(ValueError):
            score_writer.write_note("AB", 0, 1)

        with self.assertRaises(ValueError):
            score_writer.write_note("A", 0, -1)

        with self.assertRaises(ValueError):
            score_writer.write_note("A", 0, 0)

        with self.assertRaises(TypeError):
            score_writer.write_note("A", 0, "A")

        with self.assertRaises(ValueError):
            score_writer.write_rest(-1)

        with self.assertRaises(TypeError):
            score_writer.write_rest("A")

        score_writer.clear_score()
        self.assertEqual(score_writer.get_score(), [])

        with self.assertRaises(TypeError):
            score_writer.write_score_with_freq({"Sample"})

        score_writer.write_score_with_freq([(440, 1)])
        score_writer.write_score_with_freq([(440, 1)])

        self.assertListEqual(score_writer.get_score(), [(440, 1)])

        # Test write_score_with_freq validation
        with self.assertRaises(ValueError):
            score_writer.write_score_with_freq([(440, 1), (440, -1)])

        with self.assertRaises(ValueError):
            score_writer.write_score_with_freq([(440, 1), (440, 0)])

        with self.assertRaises(ValueError):
            score_writer.write_score_with_freq([(-1, 1),])

        with self.assertRaises(TypeError):
            score_writer.write_score_with_freq([(440, 1), ("A", 1)])

        with self.assertRaises(TypeError):
            score_writer.write_score_with_freq([(440, 1), (440, "A")])
