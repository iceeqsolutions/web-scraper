from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def home():
    searchTerm = "4080"
    url = f"https://www.data-systems.fi/?s={searchTerm}&post_type=product"
    result = requests.get(url).text
    doc = BeautifulSoup(result, "html.parser")
    page_text = doc.find('p', class_="woocommerce-result-count").text

    # print(page_text)

    return render_template("index.html", page_text=page_text)

if __name__ == "__main__":
    app.run(debug=True)