# Network Scanner
A Flask-based web application for scanning network hosts, identifying open ports, and scheduling periodic scans. This project leverages nmap to provide network scanning capabilities and offers a user-friendly interface to interact with.

---

## Features
**1. Network Scanning**: 
- Perform quick scans to identify open ports and running services on a target host.

**2. Vulnerability Scanning**: 
- Perform deeper scans with optional scripts to detect vulnerabilities.

**3. Scheduled Scans**: 
- Automate recurring scans at specified intervals.
**4. Web Interface**: 
- Provides an easy-to-use interface for initiating scans and viewing results.
---

## Getting Started
### Prerequisites

 - Python 3.10+
 - nmap command-line tool

---
### Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/network-scanner.git
cd network-scanner
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the application:

```bash
python run.py
```
4. Access the application at:

- Local: http://127.0.0.1:5000
- Network: http://<your-network-ip>:5000

---

## Usage
1. Perform a Scan
- Navigate to the home page.
- Enter the target host's IP address or domain.
- (Optional) Specify nmap scripts for enhanced scans.
- Submit to view the results.
2. Vulnerability Scan
- Similar to a regular scan but focuses on identifying vulnerabilities using specific nmap scripts.
3. Schedule a Scan
- Go to the "Schedule Scan" page.
- Enter the target host, interval (in minutes), and optional scripts.
- Once scheduled, the scans will run automatically.

---

## Dependencies
The following libraries are required:

**Flask**: Web framework
**python-nmap**: Python wrapper for nmap

**threading**: For managing scheduled scans

### Install them via:

```bash
pip install Flask python-nmap
```
---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

---
