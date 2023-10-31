import unittest

from module import luas_persegi


class TestLuasPersegi(unittest.TestCase):

  def test_luas_persegi_input_valid(self):
    """
    Test luas_persegi dengan input valid
    """
    self.assertEqual(luas_persegi(10, 20), 200)

  def test_luas_persegi_input_abnormal(self):
    """
    Test luas_persegi dengan input abnormal
    """
    with self.assertRaises(ValueError):
      luas_persegi(-10, 20)
    with self.assertRaises(ValueError):
      luas_persegi(10, -20)
    with self.assertRaises(ValueError):
      luas_persegi(0, 20)
    with self.assertRaises(ValueError):
      luas_persegi(10, 0)


if __name__ == "__main__":
  unittest.main()
