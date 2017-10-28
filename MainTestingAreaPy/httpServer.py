from http.server import *


class myHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("hello, nikolay", "utf8"))


# configure server
port = 8080
server_address = ("127.0.0.1", port)
httpd = HTTPServer(server_address, myHandler)

# run server
httpd.serve_forever()
