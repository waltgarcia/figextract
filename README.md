# figextract
A simple Python script to extract high quality images from a PDF file.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Command-line Arguments](#command-line-arguments)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

This script extracts images from a PDF file using the PyMuPDF library to handle PDF files and the Pillow library to process and save images. It is designed to be run from the command line, allowing users to specify the input PDF file, output folder, image format, and quality.

## Features

- Extracts images from each page of a PDF file.
- Supports both JPEG and PNG output formats.
- Allows users to specify the output folder, image format, and image quality.
- Simple and easy-to-use.

## Requirements

- Python 3.x
- PyMuPDF
- Pillow

Install the required dependencies using the following command:

```bash
pip install pymupdf Pillow
```

### Usage
Run the script from the terminal using the following command:
```
python3 picextract.py pdf_path [--output_folder OUTPUT_FOLDER] [--image_format {JPEG,PNG}] [--quality QUALITY]
```
Replace pdf_path with the path to your PDF file. The optional arguments can be used to customize the extraction process.

### Command-line Arguments
pdf_path: Path to the input PDF file.
- output_folder OUTPUT_FOLDER: Output folder for extracted images. (default: "output")
- image_format {JPEG,PNG}: Output image format. (default: "JPEG")
- quality QUALITY: Image quality for JPEG format (1-95). (default: 95)

### Examples
Extract images from a PDF file with default settings:
```
python3 picextract.py path/to/your/Paper.pdf
```

Customize the output folder, image format, and quality:
```
python3 picextract.py path/to/your/Paper.pdf --output_folder extracted_images --image_format PNG --quality 90
```

### Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.

### License
This project is licensed under the MIT License.
