# uncompyle6 version 2.11.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jul 18 2017, 09:17:00) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/MiniLab_mkII/__init__.py
# Compiled at: 2017-06-21 09:03:46
from __future__ import absolute_import, print_function
import _Framework.Capabilities as caps
from .MiniArt import MiniArt


def get_capabilities():
	return {
		caps.CONTROLLER_ID_KEY: caps.controller_id(vendor_id=7285, product_ids=[649], model_name=['Arturia MiniLab mkII']),
		caps.PORTS_KEY: [
			caps.inport(props=[caps.NOTES_CC, caps.SCRIPT, caps.REMOTE]),
			caps.outport(props=[caps.SCRIPT])
		]
	}


def create_instance(c_instance):
	return MiniArt(c_instance=c_instance)
