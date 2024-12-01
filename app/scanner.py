import nmap
import time

class NetworkScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.host = None
        self.interval = None
        self.scripts = None

    def scan_host(self, host, scripts=''):
        try:
            result = self.nm.scan(hosts=host, arguments=scripts)
            return result
        except Exception as e:
            return {'error': str(e)}

    def scan_vulnerability(self, host):
        try:
            result = self.nm.scan(hosts=host, arguments='--script=vuln')
            return result
        except Exception as e:
            return {'error': str(e)}

    def schedule_scan(self, host, interval, scripts):
        self.host = host
        self.interval = interval
        self.scripts = scripts

    def run_scheduled_scans(self):
        while True:
            if self.host is not None and self.interval is not None:
                self.scan_host(self.host, self.scripts)
                time.sleep(self.interval)
            else:
                break  # Exit if the host or interval is not set
