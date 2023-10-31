def luas_persegi(panjang, lebar):
  """
  Menghitung luas persegi

  Args:
    panjang: panjang persegi
    lebar: lebar persegi

  Returns:
    luas persegi
  """

  if panjang <= 0 or lebar <= 0:
    raise ValueError("Nilai panjang atau lebar tidak boleh kurang dari atau sama dengan 0")

  return panjang * lebar
