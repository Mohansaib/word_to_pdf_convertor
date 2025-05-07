# 📝 Word to PDF Converter (Python + Flask)

This is a simple web-based application that converts Microsoft Word `.docx` files to PDF using **Python** and **Flask**. It uses the `docx2pdf` library under the hood, which leverages Microsoft Word (Windows/macOS) for conversion.

---

## 🚀 Features

- Upload `.docx` files via a web interface
- Convert them to `.pdf` with a single click
- Download the converted PDF instantly
- Simple and lightweight Flask app

---

## 🖥️ Demo
![WhatsApp Image 2025-05-07 at 23 12 14_bf3a866a](https://github.com/user-attachments/assets/2f8eb612-698f-400f-b5a5-a44e455d7c82)



## 📦 Requirements

- Python 3.7+
- Works on **Windows or macOS** only (due to `docx2pdf`)
- Microsoft Word must be installed

### 🔧 Python Libraries

Install required packages:

```bash
pip install flask docx2pdf
