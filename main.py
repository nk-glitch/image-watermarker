import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

window = tk.Tk()
window.title("Add Watermark to Your Images")
window.minsize(width=600, height=600)

# Global variable to keep a reference to the PhotoImage object
photo_image = None


def add_watermark(image, watermark_text):
    # Create an editable image
    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)

    # Define the font and size (you might need to adjust the font path to an existing font on your system)
    font = ImageFont.truetype("arial.ttf", 36)

    # Get the width and height of the image
    width, height = watermark_image.size

    # Calculate the position for the watermark text
    bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = bbox[2] - bbox[0], bbox[3] - bbox[1]
    position = (width - text_width - 10, height - text_height - 10)

    # Add the watermark text to the image
    draw.text(position, watermark_text, font=font, fill=(2, 67, 55, 128))

    return watermark_image


def upload_image():
    global photo_image  # Use the global keyword to modify the global variable

    # Open a file dialog to select the image file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.gif")])

    # Check if a file was selected
    if file_path:
        # Open the image file
        image = Image.open(file_path)
        print(file_path)

        # Add watermark to the image
        watermark_text = "Sample Watermark"  # You can change this to any text you want
        watermarked_image = add_watermark(image, watermark_text)

        # Convert the image to a PhotoImage object
        photo_image = ImageTk.PhotoImage(watermarked_image)

        # Display the image in the GUI
        image_label = tk.Label(window, image=photo_image)
        image_label.pack()

        # Save the watermarked image

        watermarked_image.save("../../Downloads/watermarked_image.png")

        Success_label = tk.Label(text="Watermarked image saved as 'watermarked_image.png'\nBe sure to make a copy of your file")
        Success_label.pack()

upload_button = tk.Button(window, text="Upload Image", command=upload_image)
upload_button.pack()

window.mainloop()
