import unittest

from duration import frames_to_seconds


class DurationTests(unittest.TestCase):
    def test_preserves_partial_seconds(self):
        for frames, fps, expected in ((45, 30, 1.5), (1, 25, 0.04), (0, 30, 0.0)):
            with self.subTest(frames=frames, fps=fps):
                result = frames_to_seconds(frames, fps)
                self.assertEqual(result, expected)
                self.assertIsInstance(result, float)

    def test_rejects_invalid_inputs(self):
        for frames, fps in ((-1, 30), (1, 0), (1, -30)):
            with self.subTest(frames=frames, fps=fps):
                with self.assertRaises(ValueError):
                    frames_to_seconds(frames, fps)
