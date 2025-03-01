from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

def fetch_cve_data(start_index=0, results_per_page=10):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?startIndex={start_index}&resultsPerPage={results_per_page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()['result']['CVE_Items']
    else:
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cves')
def cves():
    cve_items = fetch_cve_data(start_index=0, results_per_page=10)
    return jsonify(cve_items)

if __name__ == '__main__':
    app.run(debug=True)