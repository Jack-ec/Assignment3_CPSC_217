# This code sets up the web server for use in CPSC 217 only
# By Richard Zhao
# This file should not be edited in any way
# Your code should be created in a new, separate file called support_functions.py

from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse
import json
import os
import support_functions



# Server class
class S(BaseHTTPRequestHandler):

    username = ""
    memory = []
    codeMode = False
    # DO NOT copy this database into your own code. If you do that, your code will fail all test cases
    database = \
        {
            "name": "Hi! I am Avery. I can help you with some coding questions.",
            "variable": "A variable is a named reference that stores data values for use in a program.",
            "function": "A function is a reusable block of code designed to perform a specific task.",
            "list": "A list is an ordered, mutable collection of items that can store different data types.",
            "dictionary": "A dictionary is a collection of key-value pairs that allows fast access to data by keys.",
            "if": "An if statement allows conditional execution of code based on a specified condition.",
            "set": "A set in Python is an unordered collection of unique elements.",
            "tuple": "A tuple in Python is an ordered, immutable collection of elements.",
            "None of the above": "I'm sorry I don't understand your questions."
        }

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Private-Network", "true")
        self.end_headers()

    # handle GET
    def do_GET(self):
        rootdir = os.getcwd()

        try:
            path = self.path.split("?", 1)[0]
            # handle default file
            if path == '/':
                self.path += 'index.html'

            # handle endpoints
            elif path == '/greetings':

                self.username = self.path.split("?", 1)[1].split("=", 1)[1]

                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "*")
                self.send_header("Access-Control-Allow-Headers", "*")
                self.send_header("Access-Control-Allow-Private-Network", "true")
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                try:
                    result_string = support_functions.get_greetings(self.username)
                except AttributeError:
                    result_string = "Connected! But I can't reply because you didn't create get_greetings()."


                self.wfile.write(result_string.encode('utf-8'))


            # handle files
            elif self.path.endswith('.html'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            elif self.path.endswith('.js'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "application/javascript")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))
                f.close()
            else:
                self.send_error(404, 'file not supported')

        except IOError:
            self.send_error(404, 'file not found')

    # handle POST
    def do_POST(self):
        rootdir = os.getcwd()

        try:
            path = self.path.split("?", 1)[0]

            # handle endpoints
            if path == '/chat':

                # JSON string
                payload_string = self.rfile.read(int(self.headers['Content-Length']))

                # Converts to Python dictionary
                payload = json.loads(payload_string)

                message = str(payload['message'])
                self.username = str(payload['username'])

                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Methods", "*")
                self.send_header("Access-Control-Allow-Headers", "*")
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                try:
                    if message == "run":
                        result_string = support_functions.get_reply(message, S.memory, S.database)
                        S.memory.clear()
                        S.codeMode = False
                    elif message == "code":
                        S.memory.clear()
                        result_string = support_functions.get_reply(message, S.memory, S.database)
                        S.codeMode = True
                    elif S.codeMode:
                        S.memory.append(message)
                        result_string = support_functions.get_reply(message, S.memory, S.database)
                    else:
                        result_string = support_functions.get_reply(message, S.memory, S.database)

                    print("Return value from get_reply(): " + result_string)
                except AttributeError as err:
                    result_string = "Function does not exist or work. Have you created all the functions?"
                    print("Error:", err)


                # make a Python dictionary from the result
                result_obj = {"response": result_string}

                # convert Python dictionary to JSON string
                result_string = json.dumps(result_obj)

                self.wfile.write(result_string.encode('utf-8'))

            else:
                self.send_error(404, 'endpoint not supported')

        except IOError:
            self.send_error(404, 'endpoint not found')


def run(server_class=HTTPServer, handler_class=S, addr="127.0.0.1", port=8081):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting web server... Running.")
    httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple server")
    parser.add_argument(
        "-l",
        "--listen",
        default="127.0.0.1",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8081,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()

    # start the server
    run(addr=args.listen, port=args.port)

