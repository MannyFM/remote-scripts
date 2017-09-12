# uncompyle6 version 2.11.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jul 18 2017, 09:17:00) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_mkII/HardwareSettingsComponent.py
# Compiled at: 2017-06-21 09:03:46
from __future__ import absolute_import, print_function
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.SubjectSlot import subject_slot
from _Arturia.ArturiaControlSurface import OFF_VALUE, ON_VALUE
LIVE_MEMORY_SLOT_INDEX = 7


class HardwareSettingsComponent(ControlSurfaceComponent):
    __subject_events__ = ('live_mode', )

    def __init__(self, *a, **k):
        super(HardwareSettingsComponent, self).__init__(*a, **k)
        self._memory_slot_selection = None
        self._hardware_live_mode_switch = None
        return

    def set_memory_slot_selection(self, selection):
        self._memory_slot_selection = selection
        self._on_memory_slot_changed.subject = selection

    def set_hardware_live_mode_switch(self, switch):
        self._hardware_live_mode_switch = switch

    @subject_slot('value')
    def _on_memory_slot_changed(self, slot_data):
        slot_index = slot_data[0]
        in_live_mode = slot_index == LIVE_MEMORY_SLOT_INDEX
        self.notify_live_mode(in_live_mode)
        if self._hardware_live_mode_switch is not None:
            self._hardware_live_mode_switch.send_value((
             ON_VALUE if in_live_mode else OFF_VALUE,))
        return
