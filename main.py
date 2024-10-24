#flask application. contains home page with links to multiple tools that will be created in subpages

from flask import Flask, render_template, request, redirect, url_for
from PIL import Image, ImageDraw, ImageFont  # Import necessary modules from PIL
import qrcode  # Make sure to install the qrcode library
import requests  # Import the requests library
import os
import uuid

app = Flask(__name__)

@app.route('/')  # Route for the home page
def home():
    return render_template('index.html')  # Render the home page template

@app.route('/generate_qr', methods=['GET', 'POST'])  # Route for generating QR codes
def generate_qr():
    url = None  # Initialize url variable
    qr_code_url = None  # Initialize variable to hold QR code URL
    if request.method == 'POST':  # Check if the request method is POST
        url = request.form['url']  # Get the URL from the form input
        qr = qrcode.make(url)  # Generate the QR code from the URL
        qr.save('static/qr_code.png')  # Save the QR code image in the static directory
        qr_code_url = url_for('static', filename='qr_code.png')  # Get the URL for the QR code image
    return render_template('generate_qr.html', url=url, qr_code_url=qr_code_url)  # Render the form with QR code URL if available

@app.route('/dictionary', methods=['GET', 'POST'])  # Route for the dictionary tool
def dictionary_tool():
    definition = None  # Initialize variable to hold the definition
    synonyms = None  # Initialize variable to hold the synonyms
    word = None  # Initialize variable to hold the word
    if request.method == 'POST':  # Check if the request method is POST
        word = request.form['word']  # Get the word from the form input
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')  # Use requests.get instead of request.get
        if response.status_code == 200:
            data = response.json()
            if 'meanings' in data[0] and 'definitions' in data[0]['meanings'][0]:
                definition = data[0]['meanings'][0]['definitions'][0]['definition']  # Extract the definition
                if 'synonyms' in data[0]['meanings'][0]['definitions'][0]:
                    synonyms = data[0]['meanings'][0]['definitions'][0]['synonyms']  # Extract synonyms
    return render_template('dictionary.html', definition=definition, synonyms=synonyms, word=word)  # Render the dictionary template with the definition and synonyms if available

@app.route('/watermark', methods=['GET', 'POST'])  # Route for the image watermarking tool
def watermark():
    if request.method == 'POST':
        # Check if the image and watermark text are provided
        if 'image' not in request.files or 'watermark_text' not in request.form:
            return "Please provide both an image and watermark text.", 400
        
        image = request.files['image']  # Get the uploaded image file
        watermark_text = request.form['watermark_text']  # Get the watermark text

        try:
            img = Image.open(image)  # Open the uploaded image
        except IOError:
            return "Invalid image file.", 400

        draw = ImageDraw.Draw(img)  # Create a drawing object
        
        # Load the default font
        font = ImageFont.load_default()  # Use the default font
        
        # Define positions and colors
        # text_position = (10, 10)  # Position for the watermark text
        shadow_offset = (2, 2)  # Offset for the shadow effect
        shadow_color = "black"  # Shadow color
        text_color = "white"  # Text color
        
        # Calculate text size and position for centering using textbbox
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        text_position = ((img.width - text_width) / 2, (img.height - text_height) / 2)  # Center the text


        # Draw shadow by rendering the text in a slightly offset position
        draw.text((text_position[0] + shadow_offset[0], text_position[1] + shadow_offset[1]), 
                   watermark_text, fill=shadow_color, font=font)
        
        # Draw the main text over the shadow
        draw.text(text_position, watermark_text, fill=text_color, font=font)  # Add text watermark to the image

        # Generate a unique filename with the correct extension
        extension = os.path.splitext(image.filename)[1].lower()  # Get the file extension
        unique_filename = f'watermarked_{uuid.uuid4().hex}{extension}'
        save_path = os.path.join('static', unique_filename)
        
        img.save(save_path)  # Save the watermarked image
        
        watermarked_image_url = url_for('static', filename=unique_filename)  # Get the URL for the watermarked image
        return render_template('watermark.html', watermarked_image_url=watermarked_image_url)  # Render template with the watermarked image

    return render_template('watermark.html')  # Render the form for uploading images and adding watermarks

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode

