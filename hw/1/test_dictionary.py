import unittest
import dictionary


class Test(unittest.TestCase):
    """dictionary tests"""

    # 'гривен'
    # 'гривна'
    # 'гривны'
    def test_dictionary_uah(self):
        self.assertEqual(dictionary.dictionary_uah(1), 'гривна')
        self.assertEqual(dictionary.dictionary_uah(2), 'гривны')
        self.assertEqual(dictionary.dictionary_uah(3), 'гривны')
        self.assertEqual(dictionary.dictionary_uah(4), 'гривны')
        self.assertEqual(dictionary.dictionary_uah(5), 'гривен')
        self.assertEqual(dictionary.dictionary_uah(6), 'гривен')
        self.assertEqual(dictionary.dictionary_uah(11), 'гривен')
        self.assertEqual(dictionary.dictionary_uah(15), 'гривен')
        self.assertEqual(dictionary.dictionary_uah(20), 'гривен')
        self.assertEqual(dictionary.dictionary_uah(21), 'гривна')
        self.assertEqual(dictionary.dictionary_uah(53), 'гривны')
        self.assertEqual(dictionary.dictionary_uah(77), 'гривен')

# 'копейки'
# 'копеек'
# 'копейка'
    def test_dictionary_uah_kopiyky(self):
        self.assertEqual(dictionary.dictionary_uah_kopiyky(1), 'копейка')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(2), 'копейки')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(3), 'копейки')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(4), 'копейки')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(5), 'копеек')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(6), 'копеек')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(11), 'копеек')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(15), 'копеек')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(20), 'копеек')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(21), 'копейка')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(53), 'копейки')
        self.assertEqual(dictionary.dictionary_uah_kopiyky(77), 'копеек')


if __name__ == '__dictionary__':
    unittest.dictionary()
