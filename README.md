# Multithreaded Port Scanner

Welcome to my first cybersecurity project! This is a fast, lightweight command-line port scanner written in Python. It uses multithreading to efficiently scan a range of ports on a target host and identify which ones are open.

## 📌 Features
* **Host Resolution:** Automatically converts domain names (like `example.com`) into IP addresses.
* **Multithreading:** Launches multiple scans simultaneously, making the process much faster than a standard sequential scan.
* **Custom Ranges:** Allows you to specify exactly which start and end ports you want to check.

---

## 🚀 How to Use

### Prerequisites
Make sure you have Python 3 installed on your machine. No external libraries are required—the script uses built-in Python modules (`socket`, `threading`, `sys`).

### Running the Script
Open your terminal or PowerShell and run the script using the following format:

```bash
python port_scan.py <Target_IP_or_Domain> <Start_Port> <End_Port>
