# iMAGEN: Image to Text Converter with OCR and Analytics

iMAGEN is a Python-based desktop application that converts images to text using Optical Character Recognition (OCR). The application leverages **Tesseract OCR** to extract text and provides features such as conversion percentage analysis, pie chart visualization, and the ability to save results in text or PDF format.

---

## Features

1. **Image to Text Conversion**:
   - Converts images to text using Tesseract OCR.
   - Supports multiple image formats, including PNG, JPG, JPEG, BMP, GIF, PPM, and PGM.

2. **Conversion Percentage Analysis**:
   - Calculates the percentage of text successfully extracted compared to the total image size.
   - Displays results via a pie chart.

3. **Text Display**:
   - Shows the extracted text in a scrollable text box for easy review.

4. **Save Results**:
   - Save the extracted text as:
     - A `.txt` file.
     - A `.pdf` file using the **FPDF** library.

5. **Graphical User Interface (GUI)**:
   - Built with `Tkinter`, featuring an intuitive and responsive interface.
   - Includes a background image for enhanced aesthetics.

6. **Cross-Format Compatibility**:
   - Works with various image formats for text extraction.

---

## Requirements

### Software Requirements
- Python 3.6 or above
- **Tesseract OCR** installed on your system.
  - Download from: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
  - Update `pytesseract.pytesseract.tesseract_cmd` in the code with the path to your Tesseract executable.
- Libraries:
  - `pytesseract`
  - `tkinter` (built-in with Python)
  - `Pillow`
  - `matplotlib`
  - `fpdf`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-name/imagetext-converter.git
   cd imagetext-converter
