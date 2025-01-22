import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
import pytesseract
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from fpdf import FPDF
import docx

# Specify the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\pgaur\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Function to perform OCR on the selected image
def perform_ocr():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
    if file_path:
        img = Image.open(file_path)

        try:
            text = pytesseract.image_to_string(img)
        except pytesseract.TesseractError:
            text = ""
            messagebox.showerror("Error", "No text found in the selected image")

        result_text.delete("1.0", "end")
        result_text.insert("1.0", text)

        # Update the image and text boxes
        update_image_and_text_boxes(img, text)

        # Calculate the conversion percentage
        conversion_percentage = calculate_conversion_percentage(img, text)

        # Open the graph window
        open_graph_window(conversion_percentage)

# Function to calculate the conversion percentage
def calculate_conversion_percentage(img, text):
    total_pixels = img.width * img.height
    converted_characters = len(text)
    return (converted_characters / total_pixels) * 100

# Function to update the image and text boxes
def update_image_and_text_boxes(img, text):
    img.thumbnail((400, 400))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)
    image_label.image = img

    result_text.delete("1.0", "end")
    result_text.insert("1.0", text)

# Function to open a new window with the pie chart
def open_graph_window(conversion_percentage):
    graph_window = tk.Toplevel(app)
    graph_window.title("Conversion Percentage")
    graph_window.geometry("500x500")  # Slightly larger graph window

    # Create and display the pie chart in the new window
    data = [100 - conversion_percentage, conversion_percentage]
    labels = ['Converted', 'Unconverted']
    colors = ['#e72426', '#36b631']

    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, colors=colors, autopct='%1.1f%%')
    ax.axis('equal')

    # Embed the pie chart in the tkinter window
    pie_chart = FigureCanvasTkAgg(fig, master=graph_window)
    pie_chart_widget = pie_chart.get_tk_widget()
    pie_chart_widget.pack()

# Function to save the converted text
def save_text():
    text_to_save = result_text.get("1.0", "end")
    if not text_to_save.strip():
        messagebox.showerror("Error", "No text to save.")
        return

    save_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("PDF Files", "*.pdf")])

    if save_path:
        if save_path.endswith(".txt"):
            with open(save_path, "w") as txt_file:
                txt_file.write(text_to_save)
        elif save_path.endswith(".pdf"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, text_to_save)
            pdf.output(save_path)

# Create the main application window
app = tk.Tk()
app.title("Image to Text Converter")

# Set the window size to maximize to screen size
app.geometry(f"{app.winfo_screenwidth()}x{app.winfo_screenheight()}")

# Load and display a background image
bg_image = Image.open("background2.jpg")
bg_image = bg_image.resize((app.winfo_screenwidth(), app.winfo_screenheight()))
bg_image = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(app, image=bg_image)
background_label.grid(row=0, column=0, columnspan=3, rowspan=4, sticky='nsew')  # Use grid to center background

# Create a big title label and place it at the top
title_label = tk.Label(app, text="iMAGEN", font=("Baskerville Old Face", 48), bg="white")
title_label.grid(row=0, column=0, columnspan=3, pady=(50, 20))

# Create a label for the image box
image_label = tk.Label(app)
image_label.grid(row=1, column=0, columnspan=3)

# Create a text widget to display the extracted text
result_text = tk.Text(app, wrap=tk.WORD, height=20, width=40)
result_text.grid(row=2, column=0, columnspan=3)

# Create a more prominent "Select Image" button
select_button = tk.Button(app, text="Select Image", command=perform_ocr, font=("Helvetica", 14), bg="blue", fg="white", padx=20, pady=10)
select_button.grid(row=3, column=1, pady=(20, 50))

# Create a "Save As" button
save_button = tk.Button(app, text="Save As", command=save_text, font=("Helvetica", 14), bg="green", fg="white", padx=20, pady=10)
save_button.grid(row=3, column=2, pady=(20, 50))

# Configure grid for centering
for row in range(4):
    app.grid_rowconfigure(row, weight=1)
for col in range(3):
    app.grid_columnconfigure(col, weight=1)

app.mainloop()
