# uncompyle6 version 2.11.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jul 18 2017, 09:17:00)
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_mkII/MiniLabMk2.py
# Compiled at: 2017-06-21 09:03:46
from __future__ import absolute_import, print_function

import time

import Live
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ControlSurface import ControlSurface
from _Framework.DeviceComponent import DeviceComponent
from _Framework.EncoderElement import EncoderElement
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.Layer import Layer
from _Framework.SessionComponent import SessionComponent

ANALOG_LAB_MEMORY_SLOT_ID = 1
LIVE_MEMORY_SLOT_ID = 8


""" Here we define some global variables """
CHANNEL = 0
session = None
mixer = None


class MiniArt(ControlSurface):
    session_component_type = SessionComponent
    encoder_msg_channel = 1
    encoder_msg_ids = (22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 52, 53, 54, 55)
    pad_channel = 10

    def __init__(self, c_instance):
        """everything except the '_on_selected_track_changed' override and 'disconnect' runs from here"""
        ControlSurface.__init__(self, c_instance)

        with self.component_guard():
            self._create_controls()
            self._create_device()

        self.log_message("Captain's last log stardate #0 ****")

    def _create_controls(self):
        self._device_controls = ButtonMatrixElement(rows=[
            [
                EncoderElement(MIDI_CC_TYPE, self.encoder_msg_channel, identifier,
                               Live.MidiMap.MapMode.relative_smooth_two_compliment,
                               name='Encoder_%d_%d' % (column_index, row_index))
                for column_index, identifier in enumerate(row)
            ]
            for row_index, row in enumerate((self.encoder_msg_ids[:4], self.encoder_msg_ids[8:12]))
        ])
        pass

    def _create_device(self):
        self._device = DeviceComponent(name='Device', is_enabled=False,
                                       layer=Layer(parameter_controls=self._device_controls),
                                       device_selection_follows_track_selection=True)
        self._device.set_enabled(True)
        self.set_device_component(self._device)

    def disconnect(self):
        """clean things up on disconnect"""
        self.log_message(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
                         + "--------------= ProjectX log closed =--------------")
        ControlSurface.disconnect(self)
        return None
