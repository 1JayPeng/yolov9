import os

# 设置要检查的目录
directory = r"C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData1\labels"

# 遍历目录下的所有文件
for filename in os.listdir(directory):
    if filename.endswith(".txt"):  # 只检查.txt文件
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, 1):  # 逐行读取
                numbers = [float(num) for num in line.split()]  # 将行分割成数值
                if any(n < 0 for n in numbers):  # 检查是否存在负数
                    print(f"在文件 {filename} 的第 {line_number} 行发现负数: {line.strip()}")
