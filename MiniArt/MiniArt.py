# uncompyle6 version 2.11.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jul 18 2017, 09:17:00)
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_mkII/MiniLabMk2.py
# Compiled at: 2017-06-21 09:03:46
from __future__ import absolute_import, print_function

import time

from _Framework.ButtonElement import ButtonElement
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE
from _Framework.MixerComponent import MixerComponent
from _Framework.SessionComponent import SessionComponent
from _Framework.SliderElement import SliderElement
from _Framework.TransportComponent import TransportComponent

ANALOG_LAB_MEMORY_SLOT_ID = 1
LIVE_MEMORY_SLOT_ID = 8


""" Here we define some global variables """
CHANNEL = 0
session = None
mixer = None


class MiniArt(ControlSurface):
    def __init__(self, c_instance):
        """everything except the '_on_selected_track_changed' override and 'disconnect' runs from here"""
        ControlSurface.__init__(self, c_instance)

        self.log_message(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime(
        )) + "--------------= ProjectX log opened =--------------")

        with self.component_guard():
            self._create_transport_control()
            self._create_mixer_control()
            self._create_session_control()

        self.request_rebuild_midi_map()
        self.log_message("Captain's last log stardate ****")

    def _create_transport_control(self):
        is_momentary = True

        self._transport = TransportComponent(is_enabled=True, name='Transport')
        """set up the buttons"""
        self._transport.set_play_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 61))
        self._transport.set_stop_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 63))
        self._transport.set_record_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 66))
        self._transport.set_overdub_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 68))
        self._transport.set_nudge_buttons(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 75),
                                          ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 73))
        self._transport.set_tap_tempo_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 78))
        self._transport.set_metronome_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 80))
        self._transport.set_loop_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 82))
        self._transport.set_punch_buttons(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 85),
                                          ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 87))
        self._transport.set_seek_buttons(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 90),
                                         ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 92))
        """set up the sliders"""
        self._transport.set_tempo_control(SliderElement(MIDI_CC_TYPE, CHANNEL, 26),
                                          SliderElement(MIDI_CC_TYPE, CHANNEL, 25))
        self._transport.set_song_position_control(SliderElement(MIDI_CC_TYPE, CHANNEL, 24))

        self.log_message("Captain's log stardate 1")

    def _create_mixer_control(self):
        is_momentary = True
        num_tracks = 7
        """Here we set up the global mixer"""
        global mixer
        mixer = MixerComponent(name='Mixer', num_tracks=num_tracks, is_enabled=False, num_returns=2)
        mixer.set_enabled(True)
        mixer.set_track_offset(0)
        self.song().view.selected_track = mixer.channel_strip(0)._track
        mixer.channel_strip(0)

        """set up the mixer buttons"""
        mixer.set_select_buttons(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 56), ButtonElement(
            is_momentary, MIDI_NOTE_TYPE, CHANNEL, 54))
        mixer.master_strip().set_select_button(ButtonElement(
            is_momentary, MIDI_NOTE_TYPE, CHANNEL, 94))
        mixer.selected_strip().set_mute_button(ButtonElement(
            is_momentary, MIDI_NOTE_TYPE, CHANNEL, 42))
        mixer.selected_strip().set_solo_button(ButtonElement(
            is_momentary, MIDI_NOTE_TYPE, CHANNEL, 44))
        mixer.selected_strip().set_arm_button(ButtonElement(
            is_momentary, MIDI_NOTE_TYPE, CHANNEL, 46))
        """set up the mixer sliders"""
        mixer.selected_strip().set_volume_control(SliderElement(
            MIDI_CC_TYPE, CHANNEL, 14))
        """note that we have split the mixer functions across two scripts, in order to have two session highlight 
        boxes (one red, one yellow), so there are a few things which we are not doing here... """

        self.log_message("Captain's log stardate 2")

    def _create_session_control(self):
        is_momentary = True
        num_tracks = 1
        num_scenes = 7
        global session
        session = SessionComponent(num_tracks, num_scenes)
        session.set_offsets(0, 0)
        """set up the session navigation buttons"""
        session.set_select_buttons(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 25),
                                   ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 27))
        session.set_scene_bank_buttons(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 51),
                                       ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 49))
        session.set_stop_all_clips_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 70))
        session.selected_scene().set_launch_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 30))
        """Here we set up the scene launch assignments for the session"""
        launch_notes = [60, 62, 64, 65, 67, 69, 71]
        for index in range(num_scenes):
            session.scene(index).set_launch_button(ButtonElement(is_momentary, MIDI_NOTE_TYPE,
                                                                 CHANNEL, launch_notes[index]))
        """Here we set up the track stop launch assignment(s) for the session"""
        stop_track_buttons = []
        for index in range(num_tracks):
            stop_track_buttons.append(ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, 58 + index))
        session.set_stop_track_clip_buttons(tuple(stop_track_buttons))
        """Here we set up the clip launch assignments for the session"""
        clip_launch_notes = [48, 50, 52, 53, 55, 57, 59]
        for index in range(num_scenes):
            session.scene(index).clip_slot(0).set_launch_button(
                ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, clip_launch_notes[index]))
        """Here we set up a mixer and channel strip(s) which move with the session"""

        self.log_message("Captain's log stardate 3")

    def _on_selected_track_changed(self):
        """This is an override, to add special functionality (we want to move the session to the selected track,
        when it changes) Note that it is sometimes necessary to reload Live (not just the script) when making changes
        to this function"""
        ControlSurface._on_selected_track_changed(self)
        """here we set the mixer and session to the selected track, when the selected track changes"""
        selected_track = self.song(
        ).view.selected_track
        mixer.channel_strip(0).set_track(selected_track)
        all_tracks = (
            (self.song().tracks + self.song().return_tracks) + (self.song().master_track,))
        index = list(all_tracks).index(selected_track)
        session.set_offsets(index, session._scene_offset)

    def disconnect(self):
        """clean things up on disconnect"""
        self.log_message(time.strftime("%d.%m.%Y %H:%M:%S", time.localtime())
                         + "--------------= ProjectX log closed =--------------")
        ControlSurface.disconnect(self)
        return None
