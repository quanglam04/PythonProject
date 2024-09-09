from PIL import Image

# Mở hình ảnh
image = Image.open("asset/1_player_btn.png")

# Lấy kích thước
width, height = image.size

print(f"Chiều rộng: {width}")
print(f"Chiều cao: {height}")