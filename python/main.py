import webapp2


def home(req):
  resp = webapp2.Response()
  resp.write('Cloud Endpoints on non-default Module')
  return resp


app = webapp2.WSGIApplication([
  ('/', home)
  ], debug=True)
