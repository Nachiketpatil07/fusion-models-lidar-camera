import cv2
import os

def draw_bounding_boxes(image_path, label_path):
    # Load the image
    image = cv2.imread(image_path)

    # Read the label file
    with open(label_path, 'r') as f:
        labels = f.readlines()

    # Parse the bounding box information and draw it
    for label in labels:
        parts = label.split()
        class_name = parts[0]
        x_min, y_min, x_max, y_max = map(float, parts[4:8])

        # Draw the bounding box
        cv2.rectangle(image, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)
        cv2.putText(image, class_name, (int(x_min), int(y_min) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Show the image with bounding boxes
    cv2.imshow("Bounding Boxes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_dir = r"D:/lyft/kitti_format/image_2"
label_dir = r"D:/lyft/kitti_format/label_2"

# Test with the first image
image_file = os.path.join(image_dir, "0a53822f7679c70fa3da58f935a300212acc50ddedaf8872b9eb2dc6dd87d1bb.png")
label_file = os.path.join(label_dir, "0a53822f7679c70fa3da58f935a300212acc50ddedaf8872b9eb2dc6dd87d1bb.txt")
draw_bounding_boxes(image_file, label_file)
