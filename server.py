from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


HOST = "localhost"
PORT = 8080


class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path == "/":
                filename = "index.html"
            else:
                filename = self.path.lstrip("/")

            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(content.encode("utf-8"))

        except FileNotFoundError:
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(
                "<h1>404 — Страница не найдена</h1>".encode("utf-8")
            )

        except Exception:
            self.send_response(500)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(
                "<h1>500 — Внутренняя ошибка сервера</h1>".encode("utf-8")
            )

    def do_POST(self):
        try:
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)

            data = parse_qs(post_data.decode("utf-8"))

            name = data.get("name", [""])[0]
            email = data.get("email", [""])[0]
            message = data.get("message", [""])[0]

            print("Имя:", name)
            print("Email:", email)
            print("Сообщение:", message)

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(
                "Данные получены!".encode("utf-8")
            )

        except Exception:
            self.send_response(500)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            self.wfile.write(
                "<h1>500 — Внутренняя ошибка сервера</h1>".encode("utf-8")
            )


server = HTTPServer((HOST, PORT), MyServer)

print(f"Сервер запущен: http://{HOST}:{PORT}")

server.serve_forever()
