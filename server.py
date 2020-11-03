import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('talkbox.com', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket,keyfile='./thing.key', certfile='./key.crt', server_side=True)
httpd.serve_forever()
