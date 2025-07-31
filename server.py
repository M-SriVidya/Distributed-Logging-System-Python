import socket
import threading
import json 

log_storage = []

def handle_client(conn, addr):
    try:
        data = conn.recv(2048)
        if not data:
            print("[SERVER] Received empty data!")
            return
        log = json.loads(data.decode())
        log_storage.append(log)
        print(f"[SERVER] Received log from: {log['pid']} | URL: {log['url']} | Status: {log['status']}")
        log_storage.append(log)
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(10)
    print("Server listening on port 9999...")

    try:
        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
    except KeyboardInterrupt:
        print("Shutting down...")
        # Sort and store logs
        sorted_logs = sorted(log_storage, key=lambda x: x['timestamp'])
        with open("aggregated_logs.json", "w") as f:
            json.dump(sorted_logs, f, indent=2)
        print("Logs saved to aggregated_logs.json")

start_server()
