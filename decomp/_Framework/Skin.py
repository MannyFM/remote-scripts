# uncompyle6 version 2.11.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jul 18 2017, 09:17:00) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/Skin.py
# Compiled at: 2017-06-21 09:03:47
from __future__ import absolute_import, print_function
from itertools import chain

class SkinColorMissingError(Exception):
    pass


class Skin(object):

    def __init__(self, colors=None, *a, **k):
        super(Skin, self).__init__(*a, **k)
        self._colors = {}
        if colors is not None:
            self._fill_colors(colors)
        return

    def _fill_colors(self, colors, pathname=''):
        try:
            self._fill_colors(super(colors))
        except TypeError:
            map(self._fill_colors, colors.__bases__)

        for k, v in colors.__dict__.iteritems():
            if k[:1] != '_':
                if callable(v):
                    self._fill_colors(v, pathname + k + '.')
                else:
                    self._colors[pathname + k] = v

    def __getitem__(self, key):
        try:
            return self._colors[key]
        except KeyError:
            raise SkinColorMissingError, 'Skin color missing: %s' % str(key)

    def iteritems(self):
        return self._colors.iteritems()


def merge_skins(*skins):
    skin = Skin()
    skin._colors = dict(chain(*map(lambda s: s._colors.items(), skins)))
    return skin