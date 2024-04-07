import os

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return send_file('index.html')

@app.route("/api", methods=["POST"])
def api():
    # Print request body
    print("Request body: ")
    print(request.data.decode('utf-8'))

    # Print request parameters
    print("\nRequest parameters:")
    for key, value in request.args.items():
        print(f"{key}: {value}")
    
    # Print request headers
    print("\nRequest headers:")
    for header, value in request.headers.items():
        print(f"{header}: {value}")

    return "POST request received successfully!"


def main():
    app.run(port=int(os.environ.get('PORT', default=5000)))

if __name__ == "__main__":
    main()
