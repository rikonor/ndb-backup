# This is the base handler, acting as a simple api 
# for requests to post responses through.

import os
import webapp2, jinja2

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(ROOT_DIR, 'templates')),
    extensions=['jinja2.ext.autoescape'])

#--------------------------------------------------------------
# Abstract Handler - for jinja template usage
#--------------------------------------------------------------
class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = JINJA_ENVIRONMENT.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
#--------------------------------------------------------------