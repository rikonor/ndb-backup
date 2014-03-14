import webapp2

from routes import route_list

app = webapp2.WSGIApplication(route_list, debug=True)
