# Flask Web Applications Suite

A collection of web applications built with Python and Flask. This project includes various tools.


## Features

- Home page with navigation links to multiple web applications and the following tools

 
## Tool 1: QR Code Generator

This tool allows users to generate QR codes from user-provided URLs. Users can enter a URL in the form, and the application will generate and display the corresponding QR code.

- QR code generation from user-provided URLs
- Display of generated QR codes
- Additional tools to be added in the future

## Tool 2: Dictionary Tool

This tool allows users to search for definitions, synonyms, and antonyms of words. Users can enter a word in the search form, and the application will display the relevant information.

- Word definitions, synonyms, and antonyms lookup
- User-friendly interface for searching words
- Future enhancements to include pronunciation and examples

## Tool 3: Watermark Adder

This tool allows users to add watermarks to images. Users can upload an image and specify the watermark text, position, and style. The application will then add the watermark to the image and provide the option to download the watermarked image.

- Image upload for adding watermarks
- Customizable watermark text, position, and style
- Download option for the watermarked image
- Future enhancements to include batch processing and image editing features

## Requirements

- Python 3.x
- Flask
- qrcode library
- nltk
- requests

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install Flask qrcode[pil] nltk requests
   ```

3. Download the NLTK data:
   ```bash
   nltk.download('wordnet')
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the home page.

3. Navigate to the QR code generator tool, enter a URL in the form, and submit to generate the QR code.

4. Navigate to the Dictionary Tool, enter a word in the search form, and submit to view the definitions, synonyms, and antonyms.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [qrcode](https://pypi.org/project/qrcode/) - The library used for generating QR codes.
- [NLTK](https://www.nltk.org/) - Natural Language Toolkit for text processing.
- [Requests](https://docs.python-requests.org/en/master/) - HTTP library for making requests.
