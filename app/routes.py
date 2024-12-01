from app import flask_app as app
from flask import render_template, request, redirect, url_for
from app.scanner import NetworkScanner
import threading

scanner = NetworkScanner()

@app.route('/')
def index():
    print("Index route has been called")
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    host = request.form['host']
    scripts = request.form.get('scripts', '')
    result = scanner.scan_host(host, scripts)
    # Pass the results to the HTML template
    return render_template('scan_results.html', result=result)

@app.route('/vulnerability_scan', methods=['POST'])
def vulnerability_scan():
    host = request.form['host']
    result = scanner.scan_vulnerability(host)
    return render_template('scan_results.html', result=result)

@app.route('/schedule_scan', methods=['GET', 'POST'])
def schedule_scan():
    if request.method == 'POST':
        host = request.form['host']
        interval = int(request.form['interval'])
        scripts = request.form.get('scripts', '')
        scanner.schedule_scan(host, interval, scripts)
        threading.Thread(target=scanner.run_scheduled_scans, daemon=True).start()
        return redirect(url_for('index'))
    return render_template('schedule_scan.html')

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')
