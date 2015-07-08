#!/usr/bin/env python

# http://kagerato.net/articles/software/libraries/jinja-quickstart.html

import jinja2
import os

templateLoader = jinja2.FileSystemLoader(searchpath="/")
templateEnv = jinja2.Environment(loader=templateLoader)

TEMPLATE_FILE = "%s/test.jinja" % os.getcwd()
template = templateEnv.get_template(TEMPLATE_FILE)

# Here we add a new input variable containing a list.
# Its contents will be expanded in the HTML as a unordered list.
FAVORITES = ["chocolates", "lunar eclipses", "rabbits"]

templateVars = {"title": "Test Example",
                "description": "A simple inquiry of function.",
                "favorites": FAVORITES
                }

outputText = template.render(templateVars)

with open('test.html', 'w') as f:
    f.write(outputText)
