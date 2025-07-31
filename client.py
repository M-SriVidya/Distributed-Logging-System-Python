import socket
import threading
import time
import json
from parse_csv_log import load_logs_from_csv

log_file_path = "data.csv"  # your CSV file

def send_log(logs_to_send):
    for log in logs_to_send:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(('localhost', 9999))
            s.send(log.encode())
            s.close()
        except:
            pass
        time.sleep(0.1)  # simulate delay

if __name__ == "__main__":
    all_logs = load_logs_from_csv(log_file_path)
    
    num_threads = 5
    chunk_size = len(all_logs) // num_threads
    threads = []

    for i in range(num_threads):
        chunk = all_logs[i * chunk_size : (i + 1) * chunk_size]
        t = threading.Thread(target=send_log, args=(chunk,))
        #print(f"[CLIENT] Sent log from pid {json.loads(log)['pid']}")
        t.start()   
        threads.append(t)

    for t in threads:
        t.join()
