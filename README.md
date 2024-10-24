# Flask Web Applications Suite

A collection of web applications built with Python and Flask. This project includes various tools, with the QR code generator being Tool 1.


## Features

- Home page with navigation links to multiple web applications and the following tools

 
## Tool 1: QR Code Generator

This tool allows users to generate QR codes from user-provided URLs. Users can enter a URL in the form, and the application will generate and display the corresponding QR code.

- QR code generation from user-provided URLs
- Display of generated QR codes
- Additional tools to be added in the future

## Requirements

- Python 3.x
- Flask
- qrcode library

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install Flask qrcode[pil]
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to access the home page.

3. Navigate to the QR code generator tool, enter a URL in the form, and submit to generate the QR code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [qrcode](https://pypi.org/project/qrcode/) - The library used for generating QR codes.
