# Distributed-Logging-System-Python

A simple yet powerful distributed logging system where multiple client processes send structured logs to a centralized server in real-time using sockets and multithreading.

## 🚀 Features
- Parallel log sending by multiple client processes
- Server receives logs using socket communication
- Logs include timestamped headers and structured JSON payloads
- Logs are stored in order per client in distributed buffer slots

## 📌 Tech Stack
- Python
- Socket Programming
- Multithreading
- JSON
- Timestamps (`datetime`)

## 📁 Project Structure
distributed_logger/
├── client.py # Sends logs from multiple threads
├── server.py # Receives and stores incoming logs
└── README.md


## 📸 Sample Log Format
```json
{
  "timestamp": "2025-07-23T17:20:00",
  "pid": 1234,
  "message": "User login successful"
}

📦 Future Improvements
Persist logs to file or database

Add message acknowledgment and retry logic

Visual dashboard for live log monitoring
