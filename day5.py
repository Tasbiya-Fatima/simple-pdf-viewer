import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import fitz

# Global variables
doc = None
page_num = 0
zoom = 2.0
photo = None


def open_pdf():
    global doc, page_num

    file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    if file:
        doc = fitz.open(file)
        page_num = 0
        show_page()


def show_page():
    global photo

    if doc is None:
        return

    page = doc.load_page(page_num)

    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))

    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    photo = ImageTk.PhotoImage(img)

    canvas.delete("all")
    canvas.create_image(0, 0, anchor="nw", image=photo)

    canvas.config(scrollregion=canvas.bbox("all"))

    page_label.config(text=f"Page {page_num+1} / {len(doc)}")


def next_page():
    global page_num

    if doc and page_num < len(doc) - 1:
        page_num += 1
        show_page()


def prev_page():
    global page_num

    if doc and page_num > 0:
        page_num -= 1
        show_page()


def zoom_in():
    global zoom

    if doc:
        zoom += 0.25
        show_page()


def zoom_out():
    global zoom

    if doc and zoom > 0.5:
        zoom -= 0.25
        show_page()


# ---------------- Window ----------------
root = tk.Tk()
root.title("Simple PDF Viewer")
root.geometry("900x700")

# Top Frame
top = tk.Frame(root)
top.pack(fill="x", pady=5)

tk.Button(top, text="Open PDF", command=open_pdf).pack(side="left", padx=5)
tk.Button(top, text="Previous", command=prev_page).pack(side="left", padx=5)
tk.Button(top, text="Next", command=next_page).pack(side="left", padx=5)
tk.Button(top, text="Zoom +", command=zoom_in).pack(side="left", padx=5)
tk.Button(top, text="Zoom -", command=zoom_out).pack(side="left", padx=5)

page_label = tk.Label(top, text="Page 0 / 0")
page_label.pack(side="right", padx=10)

# Canvas and Scrollbars
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

v_scroll = tk.Scrollbar(frame, orient="vertical")
v_scroll.pack(side="right", fill="y")

h_scroll = tk.Scrollbar(frame, orient="horizontal")
h_scroll.pack(side="bottom", fill="x")

canvas = tk.Canvas(
    frame,
    bg="gray",
    yscrollcommand=v_scroll.set,
    xscrollcommand=h_scroll.set
)

canvas.pack(side="left", fill="both", expand=True)

v_scroll.config(command=canvas.yview)
h_scroll.config(command=canvas.xview)

root.mainloop()