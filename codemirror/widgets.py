from django import forms
from django.conf import settings
from django.core.serializers.json import json

css = 'css/codemirror.css'
js = 'js/codemirror.js'
default_config = getattr(settings, 'CODEMIRROR_CONFIG', {})


class CodeMirror(forms.Textarea):
    class Media:
        js = js
        css = {
            'all': css
        }

    def __init__(self, **kwargs):
        self.config = default_config
        self.config.update(kwargs)
        super(CodeMirror, self).__init__()

    def render(self, name, value, attrs=None, renderer=None):
        field = super(CodeMirror, self).render(name, value, attrs)

        return """%s
<script type="text/javascript">
    CodeMirror.fromTextArea(
        document.getElementById('%s'), %s
    );
</script>
""" % (field, attrs['id'], json.dumps(self.config))
