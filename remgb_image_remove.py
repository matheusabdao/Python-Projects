from  rembg import remove # pip install rembg
from PIL import Image # pip install Pillow

input_path = './image_example.jpeg'
output_path = './image_example.png'

inp = Image.open(input_path)

output = remove(inp)

output.save(output_path)

output_image = Image.open(output_path)
output_image.show()
