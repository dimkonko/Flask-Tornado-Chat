import tornado.web
import tornado.wsgi
from tornado.ioloop import PeriodicCallback,IOLoop

from flask_app import app
from chatserver import NowHandler
 
wsgi_app = tornado.wsgi.WSGIContainer(app)
 
application = tornado.web.Application([
    (r'/now', NowHandler),
    (r'.*', tornado.web.FallbackHandler,{'fallback':wsgi_app })
])
 

#PeriodicCallback(NowHandler.echo_now,1000).start()
 
application.listen(5000)
IOLoop.instance().start()
