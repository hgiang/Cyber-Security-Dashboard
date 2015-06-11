import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template

clients = []

class MainHandler(tornado.web.RequestHandler):
  def get(self):
    # loader = tornado.template.Loader(".")
    self.render('norse.html')

class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    # print 'connection opened...'
    # self.write_message("The server says: 'Hello'. Connection was accepted.")
    print "Connected"
    clients.append(self)

  def on_message(self, message):
    print 'received:', message
    for client in clients:
	    client.write_message(message)
	    

  def on_close(self):
    print 'connection closed...'

application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
  (r"/(.*)", tornado.web.StaticFileHandler, {"path": "."}),
])

if __name__ == "__main__":
  application.listen(9090, address='192.168.1.129')
  tornado.ioloop.IOLoop.instance().start()
