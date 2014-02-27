from django.test import TestCase
from django import forms
from .validators import validate_youtube_url
from .youtubeurl import YoutubeUrl


class ContentViewsTests(TestCase):
    def test_validator(self):
        valid_urls = ('http://www.youtube.com/watch?v=C0DPdy98e4c',
                      'www.youtube.com/watch?v=C0DPdy98e4c',
                      'http://youtu.be/C0DPdy98e4c',
                      'http://www.youtube.com/embed/C0DPdy98e4c?rel=0"&frameborder="0"',
                      'https://www.youtube-nocookie.com/v/C0DPdy98e4c?version=3&amp;hl=en_US',
                      'http://www.youtube.com/watch?feature=player_detailpage&v=C0DPdy98e4c',
        )
        invalid_urls = ('http://www.youtube.com',
                        'http://www.youtube.com/qw',
                        'http://www.youtube.com/embed/C0DPdy98e4c?rel=0" frameborder="0"',
                        'http://www.youtube.com/watch?v=qw',
                        'http://youtu.be/?v=qw',
        )
        for url in invalid_urls:
            y = YoutubeUrl(url)
            try:
                validate_youtube_url(y)
            except forms.ValidationError as e:
                self.assertTrue(True, msg=e)

        for url in valid_urls:
            y = YoutubeUrl(url)
            try:
                validate_youtube_url(y)
            except forms.ValidationError as e:
                self.assertTrue(False, msg=e)
