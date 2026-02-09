#!/usr/bin/env python3
"""
Simple API using Python's http.server module
"""

import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    HTTP Request Handler for simple API
    """
    
    def _send_response(self, status_code, content_type, content):
        """
        Helper method to send HTTP response
        """
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(content.encode('utf-8'))
    
    def do_GET(self):
        """
        Handle GET requests
        """
        # Define routes
        if self.path == '/':
            # Root endpoint
            response_content = "Hello, this is a simple API!"
            self._send_response(200, 'text/plain', response_content)
        
        elif self.path == '/data':
            # JSON data endpoint
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            response_content = json.dumps(data)
            self._send_response(200, 'application/json', response_content)
        
        elif self.path == '/status':
            # Status endpoint
            response_content = "OK"
            self._send_response(200, 'text/plain', response_content)
        
        elif self.path == '/info':
            # Info endpoint (from expected output)
            info_data = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            response_content = json.dumps(info_data)
            self._send_response(200, 'application/json', response_content)
        
        else:
            # 404 for undefined endpoints
            response_content = "Endpoint not found"
            self._send_response(404, 'text/plain', response_content)
    
    def do_POST(self):
        """
        Handle POST requests - optional enhancement
        """
        response_content = "POST method not implemented"
        self._send_response(501, 'text/plain', response_content)


def run_server(port=8000):
    """
    Start the HTTP server
    """
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    
    print(f"Server running on port {port}")
    print(f"Access the API at:")
    print(f"  http://localhost:{port}/")
    print(f"  http://localhost:{port}/data")
    print(f"  http://localhost:{port}/status")
    print(f"  http://localhost:{port}/info")
    print(f"\nPress Ctrl+C to stop the server")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")


if __name__ == "__main__":
    # Start the server when script is run directly
    run_server()
