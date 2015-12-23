#!/usr/bin/env python

# http://kagerato.net/articles/software/libraries/jinja-quickstart.html

"""jinja2 demo script"""

import jinja2
import os

TEMPLATE_LOADER = jinja2.FileSystemLoader(searchpath='/')
TEMPLATE_ENV = jinja2.Environment(loader=TEMPLATE_LOADER)

TEMPLATE_FILE = '%s/test.jinja' % os.getcwd()
TEMPLATE = TEMPLATE_ENV.get_template(TEMPLATE_FILE)

# Here we add a new input variable containing a list.
# Its contents will be expanded in the HTML as a unordered list.

FAVORITES = ['chocolates', 'lunar eclipses', 'rabbits']

TEMPLATE_VARS = {'title': 'Test Example',
                 'description': 'A simple inquiry of function.',
                 'favorites': FAVORITES}

OUTPUT_TEXT = TEMPLATE.render(TEMPLATE_VARS)

with open('test.html', 'w') as f:
    f.write(OUTPUT_TEXT)
