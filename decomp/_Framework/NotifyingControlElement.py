# uncompyle6 version 2.11.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jul 18 2017, 09:17:00) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/_Framework/NotifyingControlElement.py
# Compiled at: 2017-06-21 09:03:47
from __future__ import absolute_import, print_function
from .SubjectSlot import Subject, SubjectEvent
from .ControlElement import ControlElement

class NotifyingControlElement(Subject, ControlElement):
    """
    Class representing control elements that can send values
    """
    __subject_events__ = (
     SubjectEvent(name='value', doc=' Called when the control element receives a MIDI value\n                             from the hardware '),)