from django.test import TestCase, override_settings
from django.utils.translation import gettext


class TranslationTests(TestCase):
	def test_gettext_respects_language_code(self):
		# Default LANGUAGE_CODE in settings.py is 'fr'
		self.assertIn('Bonjour', gettext('Hello World'))

	@override_settings(LANGUAGE_CODE='en')
	def test_gettext_english(self):
		self.assertIn('Hello', gettext('Hello World'))
