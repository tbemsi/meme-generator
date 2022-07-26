import random
import os
from django.shortcuts import render
import requests
from flask import Flask, render_template, abort, request
import boto3
import dotenv

from QuoteEngine.Ingestor import Ingestor
from MemeGenerator.MemeEngine import MemeEngine
import meme

app = Flask(__name__)

meme = MemeEngine('./static')

load_dotenv()


def setup():
    """ Load all resources """

    s3 = boto3.resource(
        service_name='s3',
        region_name=os.environ.get('REGION'),
        aws_access_key_id=os.environ.get('ACCESS_KEY'),
        aws_secret_access_key=os.environ.get('SECRET_KEY')
    )

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for quote_file in quote_files:
        quotes += Ingestor.parse(quote_file)

    images_path = "./_data/photos/dog/"

    imgs = []
    for file in os.listdir(images_path):
        if file.endswith(".jpg"):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    if not request.form["image_url"]:
        return render_template('meme_form.html')

    image_url = request.form["image_url"]
    try:
        r = requests.get(image_url, verify=False)
        temp = f'./tmp/{random.randint(0, 100000000)}.png'
        img = open(temp, 'wb').write(r.content)
    except:
        print('Bad image URL')
        return render_template('meme_form.html')

    body = request.form['body']
    author = request.form['author']
    path = meme.make_meme(temp, body, author)

    os.remove(temp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
