# Phishing Detection with ML

More information [here][1].

## Dataset:
* 8400 benign URLs (source: Alexa Top Websites).
* 8400 malicious URLs (source:  OpenPhish’s Feed from July 05-08 of 2024, and the rest from PhishTank database).

### Features:
External/Whois features:

* Registration Date.
* Expiration Date.

### Lexical Features:

* Having IP address in the URL.
* Having port in the URL.
* Number of “.”.
* Number of “@”.
* Number of “-“.
* Number of “//”.
* Number of “/”.
* Number of special characters (; += _ ? = & [ ]).
* Number of “www”.
* Number of “.com”.
* Number of protocols.
* Number of subdomains.
* HTTP check.
* URL length.
* Short URLs.
* Number of digits.

## Results

| Algorithm                       | Accuracy (%) | 
| :------------------------------:| :----------: | 
| Decision Tree                   | 97.53        | 
| Support Vector Machine (SVM)    | 95.48        |
| Kernel SVM                      | 97.29        |
| Random Forest                   | 98.45        |


## Testing against new URLs

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"url":"http://example.com"}'
```
