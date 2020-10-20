from selenium import webdriver
from flask import Flask, Response, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    url = request.args.get("url", "")
    if not url:
        return "123"

    driver = webdriver.Firefox()
    driver.get(url)
    png = driver.get_screenshot_as_png()
    driver.quit()

    return Response(png, mimetype="image/png")

#RUN
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)