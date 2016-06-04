from .. utils import TranspileTestCase, BuiltinFunctionTestCase, BuiltinTwoargFunctionTestCase


class DivmodTests(TranspileTestCase):
    pass


class BuiltinDivmodFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["divmod"]

    not_implemented = [
        'test_bool',
        'test_bytearray',
        'test_class',
        'test_complex',
        'test_dict',
        'test_float',
        'test_frozenset',
        'test_int',
        'test_list',
        'test_none',
        'test_set',
        'test_str',
        'test_tuple',
    ]


class BuiltinTwoargDivmodFunctionTests(BuiltinTwoargFunctionTestCase, TranspileTestCase):
    functions = ["divmod"]

    not_implemented = [
        'test_bool_bytearray',
        'test_bool_class',
        'test_bool_complex',
        'test_bool_dict',
        'test_bool_frozenset',
        'test_bool_set',
        'test_bytes_bytearray',
        'test_bytes_class',
        'test_bytes_complex',
        'test_bytes_dict',
        'test_bytes_frozenset',
        'test_bytes_set',
    ]
