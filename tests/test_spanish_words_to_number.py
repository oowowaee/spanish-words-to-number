from spanish_words_to_number import spanish_words_to_number

class TestBasicCases:
    def test_single_digits(self):
        assert spanish_words_to_number('seis') == 6

    def test_ignores_case(self):
        assert spanish_words_to_number('SEIS') == 6

    def test_ignores_accents(self):
        assert spanish_words_to_number('un millón') == 1000000

    def test_plural(self):
        assert spanish_words_to_number('tres millones') == 3000000

    def test_ciento(self):
        assert spanish_words_to_number('DOS MILLONES CIENTO CATORCE MIL QUINIENTOS SIETE') == 2114507

    def test_handles_numbers_ending_in_tres(self):
        assert spanish_words_to_number('veintitres') == 23


class TestCompoundWords:

    def test_cuatrocientos(self):
        assert spanish_words_to_number('cuatrocientos') == 400

    def test_veinticinco(self):
        assert spanish_words_to_number('veinticinco') == 25

    def test_novecientos(self):
        assert spanish_words_to_number('novecientos') == 900

    def test_quinientos(self):
        assert spanish_words_to_number('quinientos') == 500

class TestComplexNumbers:
    def test_cuatrocientos_mil(self):
        assert spanish_words_to_number('cuatrocientos mil') == 400000

    def test_large_number(self):
        assert spanish_words_to_number('SEISCIENTOS VEINTICINCO MIL') == 625000

    def test_even_larger_number(self):
        assert spanish_words_to_number(
            'DOS MILLONES SEISCIENTOS VEINTICINCO MIL') == 2625000

    def test_6_terms(self):
        assert spanish_words_to_number(
            'UN MILLÓN NOVECIENTOS SESENTA Y OCHO MIL SETECIENTOS CINCUENTA') == 1968750

    def test_y_un_mil(self):
        assert spanish_words_to_number(
            'DIECISÉIS MILLONES TRESCIENTOS SETENTA Y UN MIL SEISCIENTOS') == 16371600

    def test_10_terms(self):
        assert spanish_words_to_number(
            'DIEZ MILLONES OCHOCIENTOS CUARENTA Y CUATRO MIL NOVECIENTOS SETENTA Y DOS') == 10844972
