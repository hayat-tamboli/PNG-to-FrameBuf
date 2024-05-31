from PIL import Image
import io
import os
import print_frame_buffer

# Step 1: Open the 32-bit PNG image
input_image_path = "Zero_image.png"
img = Image.open(input_image_path)

# Step 2: Convert the image to grayscale
grayscale_img = img.convert("L")

# Step 3: Apply thresholding to binarize the image
# Here, we use a threshold value of 128 for simplicity.
# This value can be adjusted based on the specific needs.
threshold_value = 175
binary_img = grayscale_img.point(lambda x: 255 if x > threshold_value else 0, '1')

# Step 4: Save the image in 1-bit per pixel format
output_image_path = "output_1bit.png"
binary_img.save(output_image_path)

# Step 5: SUse the 1 bit output png to convert to a bmp format
input_image_path2 = "output_1bit.png"
output_image_path2 = "image.bmp"

with Image.open(input_image_path2) as img:
    # Convert and save the image in BMP format
    img.save(output_image_path2, "BMP")

img = Image.open("image.bmp")

# Step 6: deleting the intermediate 1 bit png
# comment this to see intermediary state
os.remove(output_image_path)

print(f"Image converted and saved as {output_image_path2}")

# Step 7: command terminal and use convert/magick to convert a bmp file to pbm format
os.system("magick image.bmp image.pbm")

# Step 8: print the frame buffer
print_frame_buffer.main()
