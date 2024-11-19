from  rembg import remove # pip install rembg
from PIL import Image # pip install Pillow

input_path = './ADB6D945-664C-415B-9C42-181EE7A5F784_1_105_c.jpeg'
output_path = './ADB6D945-664C-415B-9C42-181EE7A5F784_1_105_c.png'

inp = Image.open(input_path)

output = remove(inp)

output.save(output_path)

output_image = Image.open(output_path)
output_image.show()