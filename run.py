import os
import tornado.web
import tornado.wsgi
from tornado.ioloop import PeriodicCallback,IOLoop

from flask_app import app
from chatserver import NowHandler


wsgi_app = tornado.wsgi.WSGIContainer(app)
 
application = tornado.web.Application([
    (r'/now', NowHandler),
    (r'.*', tornado.web.FallbackHandler,{'fallback': wsgi_app})
])

#PeriodicCallback(NowHandler.echo_now,1000).start()

port = int(os.environ.get("PORT", 5000))
application.listen(port)
IOLoop.instance().start()
