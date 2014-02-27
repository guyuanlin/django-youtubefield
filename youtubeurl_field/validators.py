#-*- coding: utf-8 -*-
import re
import urllib2
import urlparse
from django.utils.translation import ugettext_lazy as _
from django import forms


def validate_youtube_url(value):
    pattern = (
        r'(https?://)?'
        '(www\.)?'
        '(youtube|youtu|youtube-nocookie)\.(com|be)/'
        '(watch\?v=|embed/|v/|.+\?v=|v/|.+\&v=)?([^&=%\?]{11})'
    )

    if not value.is_empty():
        if not urlparse.urlparse(value.value).scheme:
            value.value = "http://" + value.value
        try:
            con = urllib2.urlopen(value.value)
        except urllib2.HTTPError:
            raise forms.ValidationError(_(u'Not a valid Youtube URL'))
        if con.code != 200:
            raise forms.ValidationError(_(u'Not a valid Youtube URL'))
        if value.value[:16] == 'http://youtu.be/':
            if re.match(r'\w+', value.value[16:]) is None:
                raise forms.ValidationError(_(u'Not a valid Youtube URL'))
        elif re.match(pattern, value.value) is None:
            raise forms.ValidationError(_(u'Not a valid Youtube URL'))
