import os
import random

# Correct paths based on your dataset structure
image_folder = "D:/Complexyolov4/Complex-YOLOv4-Pytorch/dataset/kitti/training/image_2"
output_train = "D:/Complexyolov4/Complex-YOLOv4-Pytorch/dataset/kitti/ImageSets/train.txt"
output_val = "D:/Complexyolov4/Complex-YOLOv4-Pytorch/dataset/kitti/ImageSets/val.txt"

# Get all image filenames
files = sorted([f.split('.')[0] for f in os.listdir(image_folder) if f.endswith('.png')])

# Shuffle and split into train/val sets (80/20 split)
random.shuffle(files)
split_idx = int(len(files) * 0.8)
train_files = files[:split_idx]
val_files = files[split_idx:]

# Write to train.txt and val.txt
os.makedirs(os.path.dirname(output_train), exist_ok=True)
with open(output_train, "w") as f:
    f.writelines("\n".join(train_files) + "\n")
with open(output_val, "w") as f:
    f.writelines("\n".join(val_files) + "\n")

print("train.txt and val.txt files created successfully!")
