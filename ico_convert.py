from PIL import Image

# Open the image file
img = Image.open('a.png')  # Replace 'input.png' with your file path

# Save the image in ICO format
img.save('output.ico', format='ICO')  # Replace 'output.ico' with your desired output file path