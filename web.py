import os
import  tornado.ioloop
import tornado.web

root = os.path.dirname(__file__)
port = 6629

application = tornado.web.Application([
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"})
])
# http://stackoverflow.com/questions/39880204/zeroconf-not-found-any-service#
if __name__ == '__main__':
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()