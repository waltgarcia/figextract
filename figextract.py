import io
import fitz  # PyMuPDF
from PIL import Image
import argparse
import os

def extract_images_from_pdf(pdf_path, output_folder, image_format="JPEG", quality=95):
    doc = fitz.open(pdf_path)

    for page_number in range(doc.page_count):
        page = doc[page_number]
        images = page.get_images(full=True)

        for img_index, img_info in enumerate(images):
            img_index += 1
            img_index_str = f"{page_number + 1}_{img_index}"

            image_index = img_info[0]  # Extract the image index
            base_image = doc.extract_image(image_index)
            image_bytes = base_image["image"]

            image = Image.open(io.BytesIO(image_bytes))
            image_path = f"{output_folder}/figure_{img_index_str}.{image_format.lower()}"

            # Save the image
            image.save(image_path, format=image_format, quality=quality)

    doc.close()

def main():
    parser = argparse.ArgumentParser(description='Extract images from a PDF file.')
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')
    parser.add_argument('--output_folder', type=str, default='output', help='Output folder for extracted images')
    parser.add_argument('--image_format', type=str, default='JPEG', choices=['JPEG', 'PNG'], help='Output image format (JPEG or PNG)')
    parser.add_argument('--quality', type=int, default=95, help='Image quality for JPEG format (1-95)')

    args = parser.parse_args()

    # Create the output folder if it doesn't exist
    os.makedirs(args.output_folder, exist_ok=True)

    extract_images_from_pdf(args.pdf_path, args.output_folder, args.image_format, args.quality)
    print(f"Images extracted from {args.pdf_path} to {args.output_folder}.")

if __name__ == "__main__":
    main()
