from flask import Flask, render_template
import requests
import os

master_ip = os.environ.get('MASTER_IP', '10.146.0.5:8080')
namespace = os.environ.get('NAMESPACE', 'default')

app = Flask(__name__)


@app.route('/')
def rolling_update_demo():
    data = requests.get('http://{}/api/v1/namespaces/{}/pods'.format(master_ip, namespace))
    pod_dict = data.json()
    items = pod_dict['items']
    ip_list = [item['status']['podIP'] for item in items if 'rolling-express' in item['metadata']['name']]
    server_list = []
    for ip in ip_list:
        page = requests.get('http://{}:8080'.format(ip))
        server_list.append(page.json())

    return render_template('index.html', servers=server_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
