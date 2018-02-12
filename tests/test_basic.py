# -*- coding: utf-8 -*-

from .context import xdi_pandas

import unittest

class BasicTestSuite(unittest.TestCase):

    def test_basic_structure(self):
        df = xdi_pandas.parse('./tests/data/Agri1_dig_sol_3refs_sc1.lcf')
        assert df.shape == (237, 7)
        eq = lambda l: l[0] == l[1]
        assert all(map(eq, zip(df.columns, [
            'wavelength inverse Angstrom',
            'data',
            'fit',
            'residual',
            'AZP',
            'Zn-Methionine',
            'nano-3_(A-2016)'
        ])))


    def test_metadata(self):
        metadata = xdi_pandas.parse_metadata('./tests/data/Agri1_dig_sol_3refs_sc1.lcf')

        assert metadata['Version'] == ('XDI/1.0', 'Athena/0.9.26')
        assert metadata['Column']['1'] == 'wavelength inverse Angstrom'
        assert metadata['Column']['2'] == 'data'
        assert metadata['Column']['3'] == 'fit'
        assert metadata['Column']['4'] == 'residual'
        assert metadata['Column']['5'] == 'AZP'
        assert metadata['Column']['6'] == 'Zn-Methionine'
        assert metadata['Column']['7'] == 'nano-3_(A-2016)'

        assert metadata['Element']['edge'] == 'K'
        assert metadata['Element']['symbol'] == 'Zn'

        assert metadata['Athena']['e0'] ==  9663.5
        assert metadata['Athena']['eshift'] ==  0
        assert metadata['Athena']['rbkg'] ==  1.0
        assert metadata['Athena']['importance'] ==  1
        assert metadata['Athena']['standard'] ==  None
        assert metadata['Athena']['bkg_kweight'] ==  3
        assert metadata['Athena']['edge_step'] ==  1.0008537
        assert metadata['Athena']['fixed_step'] ==  False
        assert metadata['Athena']['pre_edge_range'] ==  (-113.000, -30.000)

        assert metadata['Comments'][0] == 'LCF fit of Zn_Clos_dig_sol_fame+SSRL as chi(k) from 2.5 to 10.6'
        assert metadata['Comments'][-1] == '.         sum ........... 1.032'

    def test_values(self):
        df = xdi_pandas.parse('./tests/data/Agri1_dig_sol_3refs_sc1.lcf')
        assert df['data'][56] == -3.2621329
        assert df['residual'][11] == -0.083962380


if __name__ == '__main__':
    unittest.main()
