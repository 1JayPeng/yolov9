# 图片大小
img_width, img_height = 800, 619

# 原始标注数据
parts = ['Adidas_0827', 'Adidas', '07707437.jpg', 'logo', '0', '319', '544', '31', '568']

# 提取坐标
x_min, y_min, x_max, y_max = map(float, parts[5:9])

# 修正坐标，确保不超出图片范围
x_min = max(x_min, 0)
y_min = max(y_min, 0)
x_max = min(x_max, img_width)
y_max = min(y_max, img_height)

# 归一化坐标和尺寸
x_center = (x_min + x_max) / 2 / img_width
y_center = (y_min + y_max) / 2 / img_height
width = (x_max - x_min) / img_width
height = (y_max - y_min) / img_height

# 确保中心点坐标在0到1之间
x_center = max(min(x_center, 1), 0)
y_center = max(min(y_center, 1), 0)

# 确保宽度和高度为非负数，且加上中心点后不超过1
width = max(width, 0)
height = max(height, 0)

# 转换为字符串，准备写入文件
yolo_format = '{} {:.6f} {:.6f} {:.6f} {:.6f}'.format(parts[4], x_center, y_center, width, height)
print(yolo_format)
