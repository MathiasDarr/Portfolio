#!/usr/bin/env python
try:
    from urllib.request import urlopen
except ImportError:
    from urllib3 import urlopen
import json
import sys

# Modify COMPONENT_NAME to name your component differently.
COMPONENT_NAME = 'Gist'

gist_url ='https://gist.githubusercontent.com/MathiasDarr/d271c02e6fbef12386d260e6f46fcbe4/raw/6153dd26dd8fc2cce3f19bbb9e65b8b1dbf4c826/'

gist = json.loads(urlopen(gist_url).read())
html = gist['div']
stylesheet = urlopen(gist['stylesheet']).read()

with open('{:s}.vue'.format(COMPONENT_NAME), 'w') as f:
    f.write('<template>{:s}</template>'.format(html))
    f.write("<script>export default {{ name: '{:s}' }}</script>".format(COMPONENT_NAME))
    f.write('<style>{:s}</style>'.format(stylesheet))