from sshtunnel import SSHTunnelForwarder
import requests

server = None

def main():
    global server
    try:
        server = SSHTunnelForwarder(
            '172.17.0.2',
            ssh_username="root",
            ssh_password="M3gusta_eltuneL",
            remote_bind_address=('127.0.0.1',80)
        )
        server.start()
        tunnel_port = server.local_bind_port
        print(tunnel_port)
        url = "http://localhost:{port}".format(
            port=tunnel_port
        )
        r = requests.get(url)
        print(r.text)
    except Exception as e:
        print("something was wrong: {error}".format(
            error=e
            )
        )
        server.stop()
        exit()

if __name__=="__main__":
    main()
    while "c" not in input():
        pass
    server.close()
