from PIL import Image, ImageDraw

# 图片路径
image_path = r'C:\Users\OrcaJump\Desktop\yolov9\DataSets\belgalogos\images\07707437.jpg'  # 替换为您的图片路径

# 矩形框的坐标 (x1, y1, x2, y2)
# (x1, y1) 是左上角的坐标
# (x2, y2) 是右下角的坐标
rect_coords = (319.0,544.0,31.0,169)  # 根据需要替换为实际坐标

# 打开图片
image = Image.open(image_path)

# 创建一个可以在图片上绘图的对象
draw = ImageDraw.Draw(image)

# 绘制矩形框
# outline参数用于设置矩形框的颜色
# width参数用于设置线条宽度
draw.rectangle(rect_coords, outline='red', width=2)

# 显示图片
image.show()

# 如果需要保存带有矩形框的图片，可以使用以下代码
# image.save(r'C:\path\to\your\new_image.jpg')  # 替换为您想要保存的路径和文件名
