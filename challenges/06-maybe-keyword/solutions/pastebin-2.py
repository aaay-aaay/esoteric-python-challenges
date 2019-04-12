from ctypes import *
from sys import *
from sys import _getframe
from types import *
from random import *

# there is no source code for this function

class PatchedLocals(dict):
    __getitem__ = FunctionType(CodeType(
        2, 0, 2, 10, 0, b'd\0\x83\0j\0d\1\x19\0d\2k\2r\x1cd\5d\3d\4\x83\1\x83\1S\0d\6j\1d\0\x83\0j\0d\7\x19\0d\0\x83\0j\0d\1\x19\0\x83\2S\0', (_getframe, 'item', 'Maybe', getrandbits, 1, bool, dict, 'self'),
        ('f_locals', '__getitem__'), ('self', 'item'), __file__, '__getitem__', 7, b'', (), ('__class__',)
    ), {})
    def __setitem__(self, item, value):
        if item == 'Maybe':
            raise SyntaxError("can't assign to keyword")
        super().__setitem__(item, value)
    def __delitem__(self, item):
        if item == 'Maybe':
            raise SyntaxError("can't delete keyword")
        super().__delitem__(item)

py_object.from_address(id(locals()) + sizeof(c_ssize_t)).value = PatchedLocals
