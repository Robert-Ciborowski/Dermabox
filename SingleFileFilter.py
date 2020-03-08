import cv2
import numpy as np

lower_threshold_colour = np.array([90.0, 40.0, 40.0])
upper_threshold_colour = np.array([200.0, 150., 150.0])

def read_single_file_blood(path, filtered_path):
    print("Starting to filter path")
    raw = cv2.imread(path)
    mask = cv2.inRange(raw, lower_threshold_colour, upper_threshold_colour)
    result = cv2.bitwise_and(raw, raw, mask=mask)
    cv2.imwrite(filtered_path, mask)
    count = cv2.countNonZero(mask)
    return float(count) / (raw.shape[0] * raw.shape[1])

if __name__ == '__main__':
    path="rawImages/013.jpg"
    filtered_path="unofilter/unoFilter.png"
    unoFilter(path, filtered_path)