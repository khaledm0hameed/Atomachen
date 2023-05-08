from PIL import Image

# Open the main image
image = Image.open('path/to/image.jpg')

# Open the logo image
logo = Image.open('path/to/logo.png')

# Resize the logo to a smaller size
logo = logo.resize((100, 100))

# Calculate the position of the logo
position = (image.width - logo.width, image.height - logo.height)

# Paste the logo onto the main image
image.paste(logo, position, logo)

# Save the resulting image
image.save('path/to/result.jpg')
