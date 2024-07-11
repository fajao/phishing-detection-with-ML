import re
import pandas as pd
import joblib
import whois
import tldextract
from datetime import datetime
import pytz
from flask import Flask, request, jsonify, render_template
from urllib.parse import urlparse

# Extract Features from a URL
def extract_features(url):
    features = {
        'whois_regDate': get_whois_reg_date(url),
        'whois_expDate': get_whois_exp_date(url),
        'number_of.': url.count('.'),
        'url_length': len(url),
        'number_of_digits': sum(c.isdigit() for c in url),
        'number_of_special_charac': get_special_char_count(url),
        'number_of-': url.count('-'),
        'number_of//': url.count('//'),
        'number_of/': url.count('/'),
        'number_of@': url.count('@'),
        'number_of_.com': url.count('.com'),
        'number_of_www': url.count('www'),
        'number_of_subdomains': get_subdomain_count(url),
        'IP_in_URL': having_ip_address(url),
        'HTTP_check': get_protocol(url)
    }
    return pd.DataFrame([features])

# FEATURE FUNCTIONS

# Extracting whois/external features from URL
# Website age in days using URL created_date
def get_whois_reg_date(url):
    try:
        whois_result = whois.whois(url)
    except Exception:
        return -1

    created_date = whois_result.creation_date

    if created_date:
        if isinstance(created_date, list):
            created_date = created_date[0]

        if isinstance(created_date, str):
            try:
                created_date = datetime.datetime.strptime(created_date, "%Y-%m-%d")
            except ValueError:
                try:
                    created_date = datetime.datetime.strptime(created_date, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    return -1

        if isinstance(created_date, datetime):
            today_date = datetime.now()
            days = (today_date - created_date).days
            return days
        else:
            return -1
    else:
        return -1

# Website expiry date in days using URL expiration_date
def get_whois_exp_date(url):
    try:
        whois_result = whois.whois(url)
    except Exception:
        return -1

    expiration_date = whois_result.expiration_date

    if expiration_date:
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]

        if isinstance(expiration_date, str):
            try:
                expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
            except ValueError:
                try:
                    expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    return -1

        if expiration_date.tzinfo is None:
            expiration_date = expiration_date.replace(tzinfo=pytz.UTC)

        today_date = datetime.now(pytz.UTC)

        days = (expiration_date - today_date).days
        return days

    return -1

# Extracting lexical features from URLs
# Number of special characters = ';', '+=', '_', '?', '=', '&', '[', ']'
def get_special_char_count(url):
    count = 0
    special_characters = [';','+=','_','?','=','&','[',']']
    for each_letter in url:
        if each_letter in special_characters:
            count = count + 1
    return count

# HTTP check
def get_protocol(url):
    protocol = urlparse(url)
    if(protocol.scheme == 'http'):
        return 1
    else:
        return 0

# Number of subdomains (excluding "www")
def get_subdomain_count(url):
    # Extract the parts of the domain
    extracted = tldextract.extract(url)   
    # Strip 'www' from the subdomain part if present
    subdomain = extracted.subdomain.lstrip('www.')
    # Count the subdomains
    if subdomain: 
        subdomain_count = len(subdomain.split('.'))
    else:
        subdomain_count = 0
    return subdomain_count

# IPv4/IPv6 in URL check
def having_ip_address(url):
    # Regular expression for matching IPv4 addresses
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    # Regular expression for matching IPv6 addresses
    ipv6_pattern = r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b|\b(?:[A-Fa-f0-9]{1,4}:){1,7}:\b|\b::(?:[A-Fa-f0-9]{1,4}:){1,7}[A-Fa-f0-9]{1,4}\b'
    # Combine both patterns
    combined_pattern = f'({ipv4_pattern})|({ipv6_pattern})'
    
    # Search for either pattern in the URL
    return int(bool(re.search(combined_pattern, url)))

####################################################################################################################################################

# Load the Model
loaded_model = joblib.load('final_model.pkl')

# Flask Service
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    url = request.json['url']
    url_features = extract_features(url)
    prediction = loaded_model.predict(url_features)
    return jsonify({'url': url, 'prediction': 'Suspicious' if prediction[0] else 'Safe'})

if __name__ == '__main__':
    app.run(debug=True)