#!/usr/bin/env python
import os
import jinja2
import webapp2


template_dir = os.path.join(os.path.dirname(__file__), "pages")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        self.render_template("index.html")

class PretvornikHandler(BaseHandler):
    def post(self):
        
        stevilo = self.request.get("stevilo")
        enota1 = self.request.get("enota1")
        enota2 = self.request.get("enota2")
        stevilo = float(stevilo)

        if enota1 == "mm" and enota2 == "mm":
            rezultat = stevilo
        elif enota1 == "cm" and enota2 == "mm":
            rezultat = 10*stevilo
        elif enota1 == "m" and enota2 == "mm":
            rezultat = 1000*stevilo
        elif enota1 == "km" and enota2 == "mm":
            rezultat = 1000000*stevilo

        elif enota1 == "mm" and enota2 == "cm":
            rezultat = 0.1*stevilo
        elif enota1 == "cm" and enota2 == "cm":
            rezultat = stevilo
        elif enota1 == "m" and enota2 == "cm":
            rezultat = 100*stevilo
        elif enota1 == "km" and enota2 == "cm":
            rezultat = 100000*stevilo

        elif enota1 == "mm" and enota2 == "m":
            rezultat = 0.001*stevilo
        elif enota1 == "cm" and enota2 == "m":
            rezultat = 0.01*stevilo
        elif enota1 == "m" and enota2 == "m":
            rezultat = stevilo
        elif enota1 == "km" and enota2 == "m":
            rezultat = 1000*stevilo

        elif enota1 == "mm" and enota2 == "km":
            rezultat = 0.000001*stevilo
        elif enota1 == "cm" and enota2 == "km":
            rezultat = 0.00001*stevilo
        elif enota1 == "m" and enota2 == "km":
            rezultat = 0.001*stevilo
        elif enota1 == "km" and enota2 == "km":
            rezultat = stevilo

        else:
            print("neznana operacija")

        rezultat = float(rezultat)


        params = {"stevilo": stevilo, "enota1": enota1, "enota2": enota2, "rezultat": rezultat}

        self.render_template("pretvornik.html", params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/pretvornik', PretvornikHandler),

], debug=True)