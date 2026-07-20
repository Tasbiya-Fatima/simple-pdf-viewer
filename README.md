<div align="center">

# 📄 Simple PDF Viewer

### A lightweight PDF Viewer built using **Python**, **Tkinter**, and **PyMuPDF**

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Tkinter-GUI-green?style=for-the-badge">
<img src="https://img.shields.io/badge/PyMuPDF-PDF-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Pillow-Image-red?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-purple?style=for-the-badge">

---

### 📖 Simple, Fast and Easy-to-use PDF Viewer

</div>

---

# 📌 Overview

This project is a **desktop PDF Viewer** developed in **Python** using **Tkinter** for the graphical interface and **PyMuPDF (fitz)** for rendering PDF pages.

The application allows users to:

- 📂 Open PDF files
- 📄 View pages
- ⬅ Navigate between pages
- ➕ Zoom In
- ➖ Zoom Out
- 📜 Scroll large PDF pages

The project is beginner-friendly and demonstrates how to build a desktop GUI application using Python.

---

# ✨ Features

- 📂 Open any PDF
- 📄 Display PDF pages
- ⬅ Previous Page
- ➡ Next Page
- 🔍 Zoom In
- 🔎 Zoom Out
- 📜 Vertical Scrolling
- ↔ Horizontal Scrolling
- 📖 Page Counter
- 🖥 Desktop GUI
- ⚡ Fast PDF Rendering

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Tkinter | GUI Development |
| PyMuPDF (fitz) | Render PDF Pages |
| Pillow (PIL) | Convert Images for Tkinter |

---

# 📁 Project Structure

```
Simple-PDF-Viewer/
│
├── main.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── home.png
    ├── open_pdf.png
    └── viewer.png
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/simple-pdf-viewer-python.git
```

```bash
cd simple-pdf-viewer-python
```

---

## Install Dependencies

```bash
pip install pymupdf pillow
```

or

```bash
pip install -r requirements.txt
```

---

# ▶ Run Project

```bash
python main.py
```

---

# 📸 Application Workflow

```
Launch Application
        │
        ▼
Open PDF
        │
        ▼
Render First Page
        │
        ▼
Display PDF
        │
 ┌──────┼─────────┐
 │      │         │
 ▼      ▼         ▼
Prev   Next     Zoom
 │      │         │
 └──────┼─────────┘
        │
        ▼
Update Display
```

---

# 📚 Functions Used

## open_pdf()

- Opens a PDF file.
- Loads the selected document.

---

## show_page()

- Renders the current page.
- Converts PDF page into an image.
- Displays it on the canvas.

---

## next_page()

Moves to the next page.

---

## prev_page()

Moves to the previous page.

---

## zoom_in()

Increases the zoom level.

---

## zoom_out()

Decreases the zoom level.

---

# 📦 Required Libraries

```text
tkinter
PyMuPDF
Pillow
```

Install:

```bash
pip install pymupdf pillow
```

---

# 📄 requirements.txt

```text
PyMuPDF
Pillow
```

---

# 🖥 GUI Components

| Component | Description |
|------------|-------------|
| Tk Window | Main Application |
| Frame | Organizes Widgets |
| Buttons | Navigation Controls |
| Canvas | Display PDF |
| Scrollbars | Navigate Large Pages |
| Label | Show Page Number |

---

# 🚀 Future Improvements

- 🔍 Search Text
- 📑 Jump to Page
- 🌙 Dark Mode
- 📌 Bookmark Pages
- 📄 Thumbnail Sidebar
- 📤 Print PDF
- 💾 Save Zoom Level
- 📚 Recent Files
- 🔖 Table of Contents
- 📝 Text Highlight
- 🔄 Rotate Pages
- 📥 Drag & Drop PDF
- 📱 Better Responsive UI

---

# 📷 Screenshots

Create a folder named **screenshots** and add:

```
screenshots/
│
├── home.png
├── open_pdf.png
└── viewer.png
```

Then add:

```markdown
## Home

![Home](screenshots/home.png)

## PDF Viewer

![Viewer](screenshots/viewer.png)

## Open PDF

![Open](screenshots/open_pdf.png)
```

---

# 🎯 Learning Outcomes

This project demonstrates:

- Python GUI Development
- Event-driven Programming
- File Handling
- Global Variables
- PDF Rendering
- Image Processing
- Canvas Operations
- Scrollbars
- GUI Layout Management
- Function-based Programming

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Tasbiya Shaikh**

Computer Engineering Student

⭐ If you found this project useful, don't forget to star the repository!
