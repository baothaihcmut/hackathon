import base64
import numpy as np
import cv2

def convertImageToCV(base64_str):
    image_data = base64.b64decode(base64_str[23:])
    np_arr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    print(frame.shape)
    return frame