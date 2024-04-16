import os
import shutil

# Define the paths to the images and labels folders
images_folder = r'C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData1\images'
labels_folder = r'C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData1\labels'
new_images_folder = r'C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData2\images'
new_labels_folder = r'C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData2\labels'

# Create the folders if they don't exist
if not os.path.exists(new_images_folder):
    os.makedirs(new_images_folder)
if not os.path.exists(new_labels_folder):
    os.makedirs(new_labels_folder)
    
# Create subfolders for train, val, and test sets
train_folder = os.path.join(new_images_folder, 'train')
val_folder = os.path.join(new_images_folder, 'val')
test_folder = os.path.join(new_images_folder, 'test')
train_labels_folder = os.path.join(new_labels_folder, 'train')
val_labels_folder = os.path.join(new_labels_folder, 'val')
test_labels_folder = os.path.join(new_labels_folder, 'test')

# Create the "train", "val" and "test" folders if they don't exist
for folder in [train_folder, val_folder, test_folder, train_labels_folder, val_labels_folder, test_labels_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to copy images and labels to the specified folder
def copy_data(paths, image_folder, label_folder, new_image_folder, new_label_folder):
    for path in paths:
        image_name = os.path.basename(path)
        image_path = os.path.join(image_folder, image_name)
        label_path = os.path.join(label_folder, image_name.replace('.jpg', '.txt'))

        if os.path.exists(image_path):
            shutil.copy(image_path, new_image_folder)

        if os.path.exists(label_path):
            shutil.copy(label_path, new_label_folder)

# Read the paths from the txt files
with open(r'C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData1\train\train.txt', 'r') as file:
    train_paths = file.read().splitlines()
with open(r'C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData1\val\val.txt', 'r') as file:
    val_paths = file.read().splitlines()
with open(r'C:\Users\OrcaJump\Desktop\yolov9\DataSets\myData1\test\test.txt', 'r') as file:
    test_paths = file.read().splitlines()

# Move the images and labels to the corresponding folders
copy_data(train_paths, images_folder, labels_folder, train_folder, train_labels_folder)
copy_data(val_paths, images_folder, labels_folder, val_folder, val_labels_folder)
copy_data(test_paths, images_folder, labels_folder, test_folder, test_labels_folder)

print("数据已成功复制到新的文件夹。")
