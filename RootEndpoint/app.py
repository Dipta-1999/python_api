from flask import Flask, jsonify, request, redirect
import socket
import datetime

app = Flask(__name__)

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def root_endpoint():
    host_name = socket.gethostname()
    ip_address_of_vm = socket.gethostbyname(host_name)


    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.bind(('localhost', 0))
    # port = s.getsockname()[1]
    # s.close()
    port = request.environ.get('SERVER_PORT')
    

    date_of_execution = datetime.date.today().strftime("%d%m%Y")
    result = { 
                'ip_address': ip_address_of_vm, 
                'port': port,
                'hostname': host_name, 
                'date': date_of_execution   
            }
    return jsonify(result)



@app.route("/status/<path:url>")
def status_endpoint(url):
    url = url.replace("-",".").replace("_",".")
    #return redirect(url_for('static', filename=new_url))
    return redirect("http://" + url)

if __name__ == "__app__":
    app.run(debug=True)