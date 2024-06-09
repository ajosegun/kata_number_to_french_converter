import unittest
from converter import translate_to_french


class TestTranslateToFrench(unittest.TestCase):
    def test_single_digit_french(self):
        self.assertEqual(translate_to_french(0), "zéro")
        self.assertEqual(translate_to_french(1), "un")
        self.assertEqual(translate_to_french(5), "cinq")

    def test_single_digit_belgian(self):
        self.assertEqual(translate_to_french(0, lang="be"), "zéro")
        self.assertEqual(translate_to_french(1, lang="be"), "un")
        self.assertEqual(translate_to_french(5, lang="be"), "cinq")

    def test_two_digits_french(self):
        self.assertEqual(translate_to_french(10), "dix")
        self.assertEqual(translate_to_french(11), "onze")
        self.assertEqual(translate_to_french(15), "quinze")
        self.assertEqual(translate_to_french(20), "vingt")
        self.assertEqual(translate_to_french(21), "vingt-et-un")
        self.assertEqual(translate_to_french(30), "trente")
        self.assertEqual(translate_to_french(35), "trente-cinq")
        self.assertEqual(translate_to_french(50), "cinquante")
        self.assertEqual(translate_to_french(51), "cinquante-et-un")
        self.assertEqual(translate_to_french(68), "soixante-huit")
        self.assertEqual(translate_to_french(70), "soixante-dix")
        self.assertEqual(translate_to_french(71), "soixante-et-onze")
        self.assertEqual(translate_to_french(72), "soixante-douze")
        self.assertEqual(translate_to_french(74), "soixante-quatorze")
        self.assertEqual(translate_to_french(75), "soixante-quinze")
        self.assertEqual(translate_to_french(99), "quatre-vingt-dix-neuf")

    def test_two_digits_belgian(self):
        self.assertEqual(translate_to_french(10, lang="be"), "dix")
        self.assertEqual(translate_to_french(11, lang="be"), "onze")
        self.assertEqual(translate_to_french(15, lang="be"), "quinze")
        self.assertEqual(translate_to_french(20, lang="be"), "vingt")
        self.assertEqual(translate_to_french(21, lang="be"), "vingt-et-un")
        self.assertEqual(translate_to_french(30, lang="be"), "trente")
        self.assertEqual(translate_to_french(35, lang="be"), "trente-cinq")
        self.assertEqual(translate_to_french(50, lang="be"), "cinquante")
        self.assertEqual(translate_to_french(51, lang="be"), "cinquante-et-un")
        self.assertEqual(translate_to_french(68, lang="be"), "soixante-huit")
        self.assertEqual(translate_to_french(70, lang="be"), "septante")
        self.assertEqual(translate_to_french(71, lang="be"), "septante-et-un")
        self.assertEqual(translate_to_french(72, lang="be"), "septante-deux")
        self.assertEqual(translate_to_french(74, lang="be"), "septante-quatre")
        self.assertEqual(translate_to_french(75, lang="be"), "septante-cinq")
        self.assertEqual(translate_to_french(80, lang="be"), "huitante")
        self.assertEqual(translate_to_french(81, lang="be"), "huitante-et-un")
        self.assertEqual(translate_to_french(90, lang="be"), "nonante")
        self.assertEqual(translate_to_french(99, lang="be"), "nonante-neuf")

    def test_three_digits_french(self):
        self.assertEqual(translate_to_french(100), "cent")
        self.assertEqual(translate_to_french(101), "cent-un")
        self.assertEqual(translate_to_french(105), "cent-cinq")
        self.assertEqual(translate_to_french(111), "cent-onze")
        self.assertEqual(translate_to_french(123), "cent-vingt-trois")
        self.assertEqual(translate_to_french(168), "cent-soixante-huit")
        self.assertEqual(translate_to_french(171), "cent-soixante-et-onze")
        self.assertEqual(translate_to_french(175), "cent-soixante-quinze")
        self.assertEqual(translate_to_french(199), "cent-quatre-vingt-dix-neuf")
        self.assertEqual(translate_to_french(200), "deux-cents")
        self.assertEqual(translate_to_french(201), "deux-cent-un")
        self.assertEqual(translate_to_french(555), "cinq-cent-cinquante-cinq")
        self.assertEqual(translate_to_french(999), "neuf-cent-quatre-vingt-dix-neuf")

    def test_three_digits_belgian(self):
        self.assertEqual(translate_to_french(100, lang="be"), "cent")
        self.assertEqual(translate_to_french(101, lang="be"), "cent-un")
        self.assertEqual(translate_to_french(105, lang="be"), "cent-cinq")
        self.assertEqual(translate_to_french(111, lang="be"), "cent-onze")
        self.assertEqual(translate_to_french(123, lang="be"), "cent-vingt-trois")
        self.assertEqual(translate_to_french(168, lang="be"), "cent-soixante-huit")
        self.assertEqual(translate_to_french(171, lang="be"), "cent-septante-et-un")
        self.assertEqual(translate_to_french(175, lang="be"), "cent-septante-cinq")
        self.assertEqual(translate_to_french(199, lang="be"), "cent-nonante-neuf")
        self.assertEqual(translate_to_french(200, lang="be"), "deux-cents")
        self.assertEqual(translate_to_french(201, lang="be"), "deux-cent-un")
        self.assertEqual(
            translate_to_french(555, lang="be"), "cinq-cent-cinquante-cinq"
        )
        self.assertEqual(translate_to_french(999, lang="be"), "neuf-cent-nonante-neuf")

    def test_four_digits_french(self):
        self.assertEqual(translate_to_french(1000), "mille")
        self.assertEqual(translate_to_french(1001), "mille-un")
        self.assertEqual(translate_to_french(1111), "mille-cent-onze")
        self.assertEqual(translate_to_french(2000), "deux-milles")
        self.assertEqual(translate_to_french(2001), "deux-mille-un")
        self.assertEqual(translate_to_french(2020), "deux-mille-vingt")
        self.assertEqual(translate_to_french(2021), "deux-mille-vingt-et-un")
        self.assertEqual(
            translate_to_french(2345), "deux-mille-trois-cent-quarante-cinq"
        )
        self.assertEqual(
            translate_to_french(9999), "neuf-mille-neuf-cent-quatre-vingt-dix-neuf"
        )

    def test_four_digits_belgian(self):
        self.assertEqual(translate_to_french(1000, lang="be"), "mille")
        self.assertEqual(translate_to_french(1001, lang="be"), "mille-un")
        self.assertEqual(translate_to_french(1111, lang="be"), "mille-cent-onze")
        self.assertEqual(translate_to_french(2000, lang="be"), "deux-milles")
        self.assertEqual(translate_to_french(2001, lang="be"), "deux-mille-un")
        self.assertEqual(translate_to_french(2020, lang="be"), "deux-mille-vingt")
        self.assertEqual(translate_to_french(2021, lang="be"), "deux-mille-vingt-et-un")
        self.assertEqual(
            translate_to_french(2345, lang="be"), "deux-mille-trois-cent-quarante-cinq"
        )
        self.assertEqual(
            translate_to_french(9999, lang="be"), "neuf-mille-neuf-cent-nonante-neuf"
        )

    def test_large_numbers_french(self):
        self.assertEqual(translate_to_french(10000), "dix-milles")
        self.assertEqual(translate_to_french(11111), "onze-mille-cent-onze")
        self.assertEqual(
            translate_to_french(12345), "douze-mille-trois-cent-quarante-cinq"
        )
        self.assertEqual(
            translate_to_french(123456),
            "cent-vingt-trois-mille-quatre-cent-cinquante-six",
        )
        self.assertEqual(
            translate_to_french(654321),
            "six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un",
        )
        self.assertEqual(
            translate_to_french(999999),
            "neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf",
        )

    def test_large_numbers_belgian(self):
        self.assertEqual(translate_to_french(10000, lang="be"), "dix-milles")
        self.assertEqual(translate_to_french(11111, lang="be"), "onze-mille-cent-onze")
        self.assertEqual(
            translate_to_french(12345, lang="be"),
            "douze-mille-trois-cent-quarante-cinq",
        )
        self.assertEqual(
            translate_to_french(123456, lang="be"),
            "cent-vingt-trois-mille-quatre-cent-cinquante-six",
        )
        self.assertEqual(
            translate_to_french(654321, lang="be"),
            "six-cent-cinquante-quatre-mille-trois-cent-vingt-et-un",
        )
        self.assertEqual(
            translate_to_french(999999, lang="be"),
            "neuf-cent-nonante-neuf-mille-neuf-cent-nonante-neuf",
        )


if __name__ == "__main__":
    unittest.main()
