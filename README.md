# Phishing Detection with ML

![Diagram](/assets/phishing_diagram,svg)

**Dataset**:
* 8400 benign URLs (source: Alexa Top Websites).
* 8400 malicious URLs (source:  OpenPhish’s Feed from July 05-08 of 2024, and the rest from PhishTank database).

**Features**:
External/Whois features:

* Registration Date.
* Expiration Date.

Lexical Features:

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

**Results**
<style>
.table-center {
    margin: 0 auto; /* Center the table horizontally */
    text-align: center; /* Center the text within each cell */
    width: 100%; /* Optional: Ensure the table spans the available width */
}
</style>

| Algorithm                       | Accuracy (%) | 
| :------------------------------:| :----------: | 
| Decision Tree                   | 97.53        | 
| Support Vector Machine (SVM)    | 95.48        |
| Kernel SVM                      | 97.29        |
| Random Forest                   | 98.45        |
{: .table-center }

<style>
.image-gallery {
    display: flex;
    flex-wrap: wrap;
    row-gap: 10px; /* Adjust the vertical spacing between rows */
    column-gap: 10px; /* Adjust the horizontal spacing between columns */
    justify-content: center; /* Center the gallery */
    margin: 0 auto; /* Center the gallery within the page */
    max-width: 1200px; /* Maximum width of the gallery */
}

.gallery-item {
    position: relative; /* Position for overlay */
    flex: 1 1 calc(50% - 16px); /* 2 images per row with gap */
    max-width: calc(50% - 16px); /* Ensure images don’t exceed container width */
    margin: 0;
    padding: 0;
    overflow: hidden; /* Hide overflow */
}

.gallery-item3 {
    position: relative; /* Position for overlay */
    flex: 1 1 calc(33.33% - 20px); /* 3 images per row with gap */
    max-width: calc(33.33% - 20px); /* Ensure images don’t exceed container width */
    margin: 0;
    padding: 0;
    overflow: hidden; /* Hide overflow */
}

.gallery-item.large {
    flex: 1 1 calc(70% - 10px); /* Larger width item */
    max-width: calc(70% - 10px);
}

.gallery-item.small {
    flex: 1 1 calc(30% - 10px); /* Larger width item */
    max-width: calc(30% - 10px);
}

.gallery-image {
    width: 100%; /* Make image take up the full width of its container */
    height: auto; /* Allow image height to adjust proportionally */
    max-height: 100%; /* Limit image height to container height */
    object-fit: cover; /* Ensure the image covers the container without stretching */
    border: 0.5px solid #ddd; /* Border around each image */
    border-radius: 1px; /* Rounded corners */
    box-shadow: 0 1px 2px rgba(0,0,0,0.1); /* Subtle shadow */
    transition: transform 0.3s ease; /* Smooth hover effect */
}

.gallery-item:hover .gallery-image {
    transform: scale(1.05); /* Slightly enlarge image on hover */
}

</style>

<div class="image-gallery">
  <figure class="gallery-item">
    <img src="/assets/img/phishing/025.png" alt="025" class="gallery-image">
  </figure>
  <figure class="gallery-item">
    <img src="/assets/img/phishing/024.png" alt="024" class="gallery-image">
  </figure>
  <figure class="gallery-item">
    <img src="/assets/img/phishing/022.png" alt="022" class="gallery-image">
  </figure>
  <figure class="gallery-item">
    <img src="/assets/img/phishing/023.png" alt="023" class="gallery-image">
  </figure>
</div>

**Testing against new URLs**

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"url":"http://example.com"}'
```

More information [here][1]{:target="_blank"}.

[1]: https://mcfajao.com/posts/Phishing_URL_Detection_with_ML/
