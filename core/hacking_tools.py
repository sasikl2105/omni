import socket

def port_scan(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        s.close()
        return f"Port {port} on {host} is OPEN"
    except:
        return f"Port {port} on {host} is CLOSED"
