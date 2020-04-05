from BRImage.glitchcore.base import _Image

class _Overlay(_Image):
	@property
	def schema(self):
		if self._schema is None:
			return self._gimage.get_default_schema()
		return self._schema
	
	@schema.setter
	def schema(self, schema):
		self._schema = schema