import cv2
from PIL import Image



'''OpenCV画像をPIL形式の画像に変換'''
def cv2pil(img):
    new_img = img.copy()
    if new_img.ndim == 2:  # モノクロ
        pass
    elif new_img.shape[2] == 3:  # カラー
        new_img = new_img[:, :, ::-1]
    elif new_img.shape[2] == 4:  # 透過
        new_img = new_img[:, :, [2, 1, 0, 3]]
    new_img = Image.fromarray(new_img)
    return new_img


'''二値化(閾値を自動選択)'''
def binarize(img_path):
    img = cv2.imread(img_path, 0)
    thr, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    print('threshold: ', thr)
    pil_img_bin = cv2pil(img_bin)
    return pil_img_bin