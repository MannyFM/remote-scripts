# uncompyle6 version 2.11.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jul 18 2017, 09:17:00) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/SliderElement.py
# Compiled at: 2017-06-21 09:03:47
from __future__ import absolute_import, print_function
import Live
from .EncoderElement import EncoderElement
from .InputControlElement import MIDI_NOTE_TYPE

class SliderElement(EncoderElement):
    """ Class representing a slider on the controller """

    def __init__(self, msg_type, channel, identifier, *a, **k):
        assert msg_type is not MIDI_NOTE_TYPE
        super(SliderElement, self).__init__(msg_type, channel, identifier, map_mode=Live.MidiMap.MapMode.absolute, *a, **k)