# Image Resizer App

This is a simple image resizer web application built using Flask and Pillow. It allows users to upload an image, specify the desired dimensions, and download the resized image.

## Live Demo

You can try the app live [here](https://circular-philomena-abhai-matta-96836434.koyeb.app/).


### Image Upload View
This is the initial view where you can upload your image and specify the desired dimensions.

![Upload View](https://github.com/mari0-0/Resize-Image/blob/main/upload.png?raw=true)

### Download View
After resizing, the user can download the resized image.

![Download View](https://github.com/mari0-0/Resize-Image/blob/main/download.png?raw=true)

### Image Input
This is image before resized.

![Input Image](https://github.com/mari0-0/Resize-Image/blob/main/katana.webp?raw=true)

### Resized Image Output
This is image after resized.

![Resized Output](https://github.com/mari0-0/Resize-Image/blob/main/resized_katana.webp?raw=true)



## Features

- **Upload an Image:** Users can upload any image in formats like JPG, PNG, etc.
- **Resize Image:** Specify the width and height to resize the image.
- **Download Resized Image:** Download the resized image in the desired dimensions.

## Tech Stack

- **Backend:** Flask
- **Image Processing:** Pillow
- **Frontend:** HTML, CSS (Tailwind)

## How to Use

1. **Upload an Image:**
   - Click on the "Choose File" button to select an image from your device.

2. **Specify Dimensions:**
   - Enter the desired width and height in the respective input fields.

3. **Resize and Download:**
   - Click on the "Resize Image" button. The resized image will be displayed along with a download button.

## Installation

To run the app locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/image-resizer-app.git
   cd image-resizer-app

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages:

    ```bash
    pip install -r requirements.txt

4. Run the Flask app:

    ```bash
    python app.py

5. Open your browser and go to http://127.0.0.1:5000 to use the app.


## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Pillow](https://python-pillow.org/)
- [Tailwind](https://tailwindcss.com/)

## Author
Abhai Matta
