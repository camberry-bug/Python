import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
import io

class Actions:
    def text_plain(self):
        return "Received text/plain content type!"

    def application_json(self):
        return "Received application/json content type!"

    def default(self):
        return "Received unknown content type"

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World from GET!')

    def do_POST(self):
        content_type = self.headers.get('Content-Type')
        action_name = content_type.replace("/", "_").replace("-", "_")
        action_handler = getattr(Actions(), action_name, Actions().default)
        response = action_handler()
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        response_io = io.BytesIO()
        response_io.write(response.encode('utf-8'))
        self.wfile.write(response_io.getvalue())

def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Serving at port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
