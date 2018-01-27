# -*- coding: utf-8 -*-

from .context import xdi_pandas

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_parse_xdi(self):
        df = xdi_pandas.parse('./tests/data/Agri1_dig_sol_3refs_sc1.lcf')
        assert df.shape == (237, 7)
        assert list(df.columns) == [
            'wavelength inverse Angstrom',
            'data',
            'fit',
            'residual',
            'AZP',
            'Zn-Methionine',
            'nano-3_(A-2016)'
        ]

if __name__ == '__main__':
    unittest.main()
