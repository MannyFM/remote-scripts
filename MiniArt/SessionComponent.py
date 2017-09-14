# uncompyle6 version 2.11.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jul 18 2017, 09:17:00)
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_mkII/SessionComponent.py
# Compiled at: 2017-06-21 09:03:46
from __future__ import absolute_import, print_function
from itertools import product
from _Framework.ClipSlotComponent import ClipSlotComponent as ClipSlotComponentBase
from _Framework.SceneComponent import SceneComponent as SceneComponentBase
from _Arturia.SessionComponent import SessionComponent as SessionComponentBase
EMPTY_VALUE = 0
TRIGGERED_TO_RECORD_VALUE = 1
RECORDING_VALUE = 1
TRIGGERED_TO_PLAY_VALUE = 4
STARTED_VALUE = 4
STOPPED_VALUE = 5


class ClipSlotComponent(ClipSlotComponentBase):

    def __init__(self, *a, **k):
        super(ClipSlotComponent, self).__init__(*a, **k)
        self._led = None
        return

    def set_led(self, led):
        self._led = led

    def update(self):
        super(ClipSlotComponent, self).update()
        self._update_led()

    def _update_led(self):
        if self.is_enabled() and self._led is not None:
            value_to_send = self._feedback_value()
            if value_to_send in (None, -1):
                value_to_send = EMPTY_VALUE
            self._led.send_value((value_to_send,))
        return

    def _feedback_value(self):
        if self._clip_slot is not None:
            if self.has_clip():
                clip = self._clip_slot.clip
                if clip.is_triggered:
                    if clip.will_record_on_start:
                        return TRIGGERED_TO_RECORD_VALUE
                    return TRIGGERED_TO_PLAY_VALUE
                else:
                    if clip.is_playing:
                        if clip.is_recording:
                            return RECORDING_VALUE
                        return STARTED_VALUE
                    return STOPPED_VALUE

        return


class SceneComponent(SceneComponentBase):
    clip_slot_component_type = ClipSlotComponent


class SessionComponent(SessionComponentBase):
    scene_component_type = SceneComponent

    def set_clip_slot_leds(self, leds):
        assert not leds or leds.width() == self._num_tracks and leds.height() == self._num_scenes
        if leds:
            for led, (x, y) in leds.iterbuttons():
                scene = self.scene(y)
                slot = scene.clip_slot(x)
                slot.set_led(led)

        else:
            for x, y in product(xrange(self._num_tracks), xrange(self._num_scenes)):
                scene = self.scene(y)
                slot = scene.clip_slot(x)
                slot.set_led(None)

        return
