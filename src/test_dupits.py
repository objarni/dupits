# coding: utf-8
import unittest

# #Generera samtliga substrängar
# Bygg chunkstruktur
# Hitta intressant chunk (den med störst dup-värde!)
# Skriv rapport


def generate_substrings(s):
    l = len(s)
    for i in range(l):
        for j in range(i, l):
            yield s[i:j + 1]


class TestGenerateSubstrings(unittest.TestCase):

    def eq(self, g1, g2):
        self.assertEqual(set(g1), set(g2))

    def test_finds_all_substrings_of_short_string(self):
        got = generate_substrings('abc')
        expected = 'a,b,c,ab,bc,abc'.split(',')
        self.eq(expected, got)

    def test_finds_long_substring_in_big_string(self):
        fatstring = ','.join(map(str, range(10 ** 2)))
        result = generate_substrings(fatstring)
        self.assertTrue(',45,' in result)

if __name__ == '__main__':
    unittest.main()
