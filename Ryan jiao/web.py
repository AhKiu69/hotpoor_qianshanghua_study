import tornado.ioloop
import tornado.web
import sys


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class ReadDemoHandler(tornado.web.RequestHandler):
    def get(self):
        f = open("demo.txt").read()
        self.write(f)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/demo", ReadDemoHandler)
    ])


port = 8888

if __name__ == "__main__":
    a = sys.argv
    b = a[1:]
    c = {}
    for i in range(0, len(b), 2):
        c[b[i]] = b[i + 1]
    port = int(c.get("--port", "8888"))
    app = make_app()
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
