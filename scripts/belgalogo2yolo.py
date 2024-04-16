import os
from PIL import Image
from sklearn.model_selection import train_test_split
import shutil
# 路径配置
label_path = r"C:\Users\OrcaJump\Desktop\yolov9\DataSets\belgalogos\labels"
image_folder = r"C:\Users\OrcaJump\Desktop\yolov9\DataSets\belgalogos\images"
annotation_file_path = r"C:\Users\OrcaJump\Desktop\yolov9\DataSets\belgalogos\labels.txt"
class_names_file_path = os.path.join(r"C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData1", 'classes.txt')
# 新数据集路径配置
# 原始数据集路径配置
original_label_path = r"C:\Users\OrcaJump\Desktop\yolov9\DataSets\belgalogos\labels"
original_image_folder = r"C:\Users\OrcaJump\Desktop\yolov9\DataSets\belgalogos\images"
annotation_file_path = r"C:\Users\OrcaJump\Desktop\yolov9\DataSets\belgalogos\labels.txt"
dataset_base_path = r"C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData1"
new_image_folder = os.path.join(dataset_base_path, 'images')
new_label_path = os.path.join(dataset_base_path, 'labels')
os.makedirs(new_image_folder, exist_ok=True)
os.makedirs(new_label_path, exist_ok=True)
# 读取标注文件
with open(annotation_file_path, 'r') as file:
    annotations = file.readlines()

# 创建一个集合，用于存储所有不同的商标名
class_names = set()

# 处理每一行标注来提取商标名
for ann in annotations:
    parts = ann.strip().split()
    class_name = parts[1]  # 商标名位于第二列
    class_names.add(class_name)

# 将商标名排序并分配类别索引
class_names = sorted(list(class_names))
class_indices = {name: index for index, name in enumerate(class_names)}

# 将商标名及其对应的索引写入到文件中
with open(class_names_file_path, 'w') as file:
    for index, class_name in enumerate(class_names):
        file.write(f"{index}:{class_name}\n")

# 创建一个字典，用于存储每个图像的所有标注
annotations_per_image = {}

# 重新处理每一行标注
for ann in annotations:
    parts = ann.strip().split()
    image_name, class_name = parts[2], parts[1]
    
    image_path = os.path.join(image_folder, image_name)
    if not os.path.exists(image_path):
        continue  # 如果图片不存在，跳过
    
    # 获取图片尺寸
    with Image.open(image_path) as img:
        img_width, img_height = img.size
    if image_name == '07707437.jpg':
        print(img_width, img_height)
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

    
    # 使用商标名对应的索引
    class_index = class_indices[class_name]
    
    # 准备YOLO格式的标注字符串
    annotation_str = f"{class_index} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
    if(image_name == '07707437.jpg'):
        print(annotation_str)
    # 将标注添加到字典中
    if image_name not in annotations_per_image:
        annotations_per_image[image_name] = []
    annotations_per_image[image_name].append(annotation_str)

# 删除没有对应标注文件的图片
for image_name in os.listdir(image_folder):
    txt_file_name = os.path.splitext(image_name)[0] + ".txt"
    txt_file_path = os.path.join(label_path, txt_file_name)
    if not os.path.exists(txt_file_path):
        os.remove(os.path.join(image_folder, image_name))

# 分割数据集
image_names = list(annotations_per_image.keys())
train_images, test_images = train_test_split(image_names, test_size=0.2, random_state=42)
val_images, test_images = train_test_split(test_images, test_size=0.5, random_state=42)

# 创建训练集、推理集和测试集的文件列表
def write_dataset_files(image_set, set_name):
    set_folder = os.path.join(dataset_base_path, set_name)
    os.makedirs(set_folder, exist_ok=True)
    with open(os.path.join(set_folder, f"{set_name}.txt"), 'w') as set_file:
        for image_name in image_set:
            # 写入新的图片路径
            set_file.write(os.path.join(new_image_folder, image_name) + '\n')
            # 复制图片到新的图片文件夹
            shutil.copy2(os.path.join(original_image_folder, image_name),
                         os.path.join(new_image_folder, image_name))
            # 写入新的标注字符串到新的标注文件夹
            txt_file_name = os.path.splitext(image_name)[0] + ".txt"
            with open(os.path.join(new_label_path, txt_file_name), 'w') as label_file:
                for annotation_str in annotations_per_image[image_name]:
                    label_file.write(annotation_str + '\n')


# 写入数据集文件
write_dataset_files(train_images, "train")
write_dataset_files(val_images, "val")
write_dataset_files(test_images, "test")
print("数据集划分完成并写入新文件夹。")