from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
from bs4 import BeautifulSoup as bs
import requests

app = Flask(__name__)
# #@app.route('/')
#
@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def get_price():
    url = "https://www.metal.com/Lithium-ion-Battery/202303240001"
    try:
        page = requests.get(url)
        page.raise_for_status()
        soup = bs(page.content, 'html.parser')
        price_tag = soup.select_one("#__next div.main___1ft3R.detail___2oeiJ div.left___wCEQV div:nth-child(3) div.metalsContent___3T_m3 div.priceContent___3lf_D div div:nth-child(1) span.strong___1JlBD.priceDown___2TbRQ")
        if price_tag:
            price = price_tag.get_text()
            return jsonify({"price": price})
        else:
            return jsonify({'message': 'Something is Wrong'}), 404

    except requests.exceptions.RequestException as e:
        return jsonify({'error':str(e)}, 404)




if __name__ == '__main__':
    app.run(port=8080,debug=True)




