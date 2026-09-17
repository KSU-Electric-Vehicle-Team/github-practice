import unittest

from speed import to_kmh


class SpeedTests(unittest.TestCase):
    def test_ten_metres_per_second(self) -> None:
        self.assertAlmostEqual(to_kmh(10), 36)


if __name__ == "__main__":
    unittest.main()
