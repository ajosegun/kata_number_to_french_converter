class FrenchNumberTranslator:
    """
    NumberToFrench is a class designed to convert non-negative integers into their French
    word equivalents. It supports conversion for numbers ranging from 0 to 999,999.

    Attributes:
        lang (str): The language variant for conversion. Default is "fr" (French).
                    Another supported option is Belgian French, indicated by "be".

    Methods:
        convert_number(n: int) -> str:
            Converts a given non-negative integer n into its French word equivalent.
            Raises a ValueError if n is not a non-negative integer or is out of the supported range.

    Usage Example:
        converter = FrenchNumberTranslator()
        print(converter.convert_number(123))  # Outputs: "cent-vingt-trois"

        belgian_converter = FrenchNumberTranslator(lang="be")
        print(belgian_converter.convert_number(123))  # Outputs the Belgian French equivalent
    """

    def __init__(self, lang: str = "fr") -> None:
        self.lang = lang
        # Base number mappings
        self.units = [
            "zéro",
            "un",
            "deux",
            "trois",
            "quatre",
            "cinq",
            "six",
            "sept",
            "huit",
            "neuf",
        ]
        self.teens = ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize"]

        if self.lang == "fr":
            self.tens = [
                "",
                "dix",
                "vingt",
                "trente",
                "quarante",
                "cinquante",
                "soixante",
            ]

            self.special_tens = {
                70: "soixante-dix",
                71: "soixante-et-onze",
                80: "quatre-vingts",
                90: "quatre-vingt-dix",
            }
        elif self.lang == "be":
            self.tens = [
                "",
                "dix",
                "vingt",
                "trente",
                "quarante",
                "cinquante",
                "soixante",
                "septante",
                "huitante",
                "nonante",
            ]
        else:
            raise ValueError("Unsupported language variant")

    def _handle_tens(self, n):
        if n % 10 == 0:
            return self.tens[n // 10]
        if n % 10 == 1 and n != 11:
            return self.tens[n // 10] + "-et-un"
        return self.tens[n // 10] + "-" + self.units[n % 10]

    # Helper method to convert numbers less than 100
    def _two_digit_to_french(self, n):
        if n < 10:
            return self.units[n]
        elif n < 17:
            return self.teens[n - 10]
        elif n < 20:
            return "dix-" + self.units[n - 10]

        elif self.lang == "be" and n < 100:
            return self._handle_tens(n)
        elif n < 70:
            return self._handle_tens(n)
        elif n in self.special_tens:
            return self.special_tens[n]
        elif n < 80:
            return "soixante-" + self._two_digit_to_french(n - 60)
        else:
            return "quatre-vingt" + (
                "s" if n == 80 else "-" + self._two_digit_to_french(n - 80)
            )

    # Helper method to convert numbers less than 1000
    def _three_digit_to_french(self, n):
        if n < 100:
            return self._two_digit_to_french(n)
        elif n == 100:
            return "cent"
        else:
            hundreds = n // 100
            remainder = n % 100
            if hundreds == 1:
                return "cent" + (
                    ("-" + self._two_digit_to_french(remainder))
                    if remainder != 0
                    else ""
                )
            else:
                return (
                    self.units[hundreds]
                    + "-cent"
                    + (
                        ("-" + self._two_digit_to_french(remainder))
                        if remainder != 0
                        else "s"
                    )
                )

    # Helper method to convert numbers less than 1,000,000
    def convert_number(self, n):
        if n < 1000:
            return self._three_digit_to_french(n)
        elif n < 2000:
            return "mille" + (
                ("-" + self._three_digit_to_french(n % 1000)) if n % 1000 != 0 else ""
            )
        elif n < 1000000:
            thousands = n // 1000
            remainder = n % 1000
            return (
                self._three_digit_to_french(thousands)
                + "-mille"
                + (
                    ("-" + self._three_digit_to_french(remainder))
                    if remainder != 0
                    else "s"
                )
            )
        else:
            raise ValueError("Number out of supported range")


def translate_to_french(number: int, lang: str = "fr") -> str:
    if not isinstance(number, int) or number < 0:
        raise ValueError("Number must be a non-negative integer")
    return FrenchNumberTranslator(lang).convert_number(number)


def translate_to_french_list(list__of_numbers: list, lang: str = "fr"):
    if len(list__of_numbers) < 1:
        raise ValueError("Can't process an empty list")

    for number in list__of_numbers:
        yield translate_to_french(number, lang)
