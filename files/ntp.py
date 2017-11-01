#!/usr/bin/env python

import json
import os
import re
import subprocess
import sys

content=dict()


version_re = re.compile('^ntpd\s+(?P<version>(?P<major>[0-9]+)[^ ]+)$')
try:
    result = subprocess.check_output(['/usr/bin/env', 'ntpd', '--version'], universal_newlines=True)
    match = version_re.search(result.strip())
    if match:
        content['version_full'] = match.group('version')
        content['version_major'] = match.group('major')
except subprocess.CalledProcessError as e:
    content['error'] = str(e)

if len(content) == 0:
    content = None

print(json.dumps(content))
sys.exit(0)
