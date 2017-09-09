# Transport.py
# This is a stripped-down script, which uses the Framework classes to assign MIDI notes to play, stop and record.
# Central base class for scripts based on the new Framework
from _Framework.ControlSurface import ControlSurface
# Class encapsulating all functions in Live's transport section
from _Framework.TransportComponent import TransportComponent
# Class representing a button a the controller
from _Framework.ButtonElement import ButtonElement
from _Framework.Layer import Layer


class Transport(ControlSurface):
	def __init__(self, c_instance):
		ControlSurface.__init__(self, c_instance)

		self.log_message("Captain's log stardate 1/2")

		with self.component_guard():
			self._create_controls()
			self._create_transport()

	def _create_controls(self):
		self._pad_ids = None
		self._pad_channel = None
		self._pads = None
		self._sliders = None
		self._encoders = None
		self._stop_button = ButtonElement(True, 0, 0, 63)
		self._play_button = ButtonElement(True, 0, 0, 61)
		self._record_button = ButtonElement(True, 0, 0, 66)
		self._control_buttons = None

	def _create_transport(self):
		self._transport = TransportComponent(is_enabled=True, name='Transport') #Instantiate a Transport Component
		self._transport.layer = Layer(play_button=self._play_button, stop_button=self._stop_button, record_button=self._record_button)
		self.log_message("Captain's log stardate 2/2")
