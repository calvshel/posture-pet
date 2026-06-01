import unittest

import posture_pet


class PosturePetTests(unittest.TestCase):
    def test_interval_seconds(self):
        self.assertEqual(posture_pet.interval_seconds(45), 2700)
        self.assertEqual(posture_pet.interval_seconds(1.5), 90)

    def test_interval_seconds_rejects_zero(self):
        with self.assertRaises(ValueError):
            posture_pet.interval_seconds(0)

    def test_icon_sizes(self):
        self.assertEqual(posture_pet.make_icon(True).size, (64, 64))
        self.assertEqual(posture_pet.make_icon(False).size, (64, 64))


if __name__ == "__main__":
    unittest.main()
