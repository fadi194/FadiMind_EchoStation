#!/usr/bin/env python3
import http.server
import socketserver
import os
import socket

def find_free_port(start_port=5000):
    """Find a free port starting from start_port"""
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('0.0.0.0', port))
                return port
        except OSError:
            continue
    return None

PORT = find_free_port(5000)
if PORT is None:
    print("Could not find a free port")
    exit(1)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    print(f"Serving FadiMind Echo at http://0.0.0.0:{PORT}")
    httpd.serve_forever()