#flask application. contains home page with links to multiple tools that will be created in subpages

from flask import Flask, render_template, request, redirect, url_for
import qrcode  # Make sure to install the qrcode library

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

@app.route('/show_qr')  # Route to display the generated QR code
def show_qr():
    return render_template('show_qr.html')  # Render the template to show the QR code

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
