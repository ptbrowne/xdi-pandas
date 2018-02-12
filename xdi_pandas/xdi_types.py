import dateutil.parser


def parse_enum(enum):
    return set(
        s.lower() for s in enum.strip().replace('\n', ' ').replace('  ', ' ').split(' ')
    )


allowed_symbols = parse_enum('''
H  He Li Be B  C  N  O  F  Ne Na Mg Al Si P  S
Cl Ar K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge
As Se Br Kr Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd
In Sn Sb Te I  Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd
Tb Dy Ho Er Tm Yb Lu Hf Ta W  Re Os Ir Pt Au Hg
Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U  Np Pu Am Cm
Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn
Uut Fl Uup Lv Uus Uuo
''')


allowed_edges = parse_enum('''
K L  L1 L2 L3 M  M1 M2 M3 M4 M5
N N1 N2 N3 N4 N5 N6 N7 O  O1 O2 O3 O4 O5 O6 O7
''')


def maybe(type):
    def validator(value):
        if value.lower() == 'none':
            return None
        else:
            return type(value)
    return validator


def isotime(v):
    return dateutil.parser.parse(v)


def human_bool(v):
    if v == 'yes':
        return True
    elif v == 'no':
        return False
    else:
        raise ValueError('%s is neither yes or no' % v)


def one_of(list, name):
    def validator(v):
        if v.lower() in list:
            return v
        else:
            raise ValueError('%s is not a valid %s.' % (v, name))
    return validator


def tuple_validator(*types):
    def validator(v):
        try:
            values = v.split(' ')
            return tuple([types[i](values[i]) for i, v in enumerate(types)])
        except (KeyError, ValueError) as e:
            raise ValueError('Could not convert %s to tuple(%s)' % (v, types))
    return validator


unit = str
def with_units(type):
    return tuple_validator(type, unit)


two_tuple_float = tuple_validator(float, float)

xdi_fields = {
    'Element.edge': one_of(allowed_edges, 'edge'),
    'Element.symbol': one_of(allowed_symbols, 'chemical symbol'),
    'Mono.d_spacing': float,
    'Athena.bkg_kweight': float,
    'Athena.clamps': two_tuple_float,
    'Athena.dk': float,
    'Athena.dr': float,
    'Athena.e0': float,
    'Athena.edge_step': float,
    'Athena.eshift': float,
    'Athena.fixed_step': human_bool,
    'Athena.importance': float,
    'Athena.k_range': two_tuple_float,
    'Athena.kweight': float,
    'Athena.normalization_range': two_tuple_float,
    'Athena.phase_correction': human_bool,
    'Athena.plot_multiplier': float,
    'Athena.post_edge_polynomial': str,
    'Athena.pre_edge_line': str,
    'Athena.pre_edge_range': two_tuple_float,
    'Athena.r_range': two_tuple_float,
    'Athena.rbkg': float,
    'Athena.spline_range_energy': two_tuple_float,
    'Athena.spline_range_k': two_tuple_float,
    'Athena.standard': maybe(str),
    'Athena.window': str,
    'Athena.y_offset': float,
    'Scan.start_time': isotime,
    'Scan.end_time': isotime,
    'Scan.edge_energy': with_units(float)
}
