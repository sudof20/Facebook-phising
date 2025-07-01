import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from datetime import datetime

# Define the base directory of the project.
# Ensures the server locates files using the correct relative path.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the index.html file for root or /index.html path
        if self.path == '/' or self.path == '/index.html':
            file_path = os.path.join(BASE_DIR, 'static', 'index.html')
            self.send_html_file(file_path)
        # Serve 2fa.html for /2fa.html path
        elif self.path == '/2fa.html':
            file_path = os.path.join(BASE_DIR, 'static', '2fa.html')
            self.send_html_file(file_path)
        # Serve data.txt file from data directory
        elif self.path == '/data.txt':
            file_path = os.path.join(BASE_DIR, 'data', 'data.txt')
            self.send_text_file(file_path)
        else:
            # Respond with 404 for any unknown path
            self.send_error(404)

    def do_POST(self):
        # Handle POST request to /save endpoint
        if self.path == '/save':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = urllib.parse.parse_qs(post_data)

            # Append the submitted data to data/data.txt file with timestamp
            data_file_path = os.path.join(BASE_DIR, 'data', 'data.txt')
            with open(data_file_path, 'a') as f:
                f.write(f"\n\n{datetime.now()}\n")
                for key, value in data.items():
                    f.write(f"{key}: {value[0]}\n")

            # Respond with 200 OK status
            self.send_response(200)
            self.end_headers()
        else:
            # Respond with 404 Not Found for unsupported POST paths
            self.send_error(404)

    def send_html_file(self, file_path):
        """
        Helper method to serve HTML files.
        """
        try:
            with open(file_path, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, f"File not found: {file_path}")
        except Exception as e:
            self.send_error(500, f"Error serving file: {e}")

    def send_text_file(self, file_path):
        """
        Helper method to serve plain text files.
        """
        try:
            with open(file_path, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(file.read())
        except FileNotFoundError:
            self.send_error(404, f"File not found: {file_path}")
        except Exception as e:
            self.send_error(500, f"Error serving file: {e}")

def run():
    # Start the HTTP server on port 8080
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server running at http://localhost:8080')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
