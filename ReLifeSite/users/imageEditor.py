import numpy as np
from PIL import Image
from ReLifeSite.settings import BASE_DIR


def crop_image(img_name: str) -> bool | None:
    img = Image.open(img_name)
    width, height = img.size
    if width == height:
        return None
    img = np.array(img)
    offset = int(abs(height - width) / 2)
    if width > height:
        img = img[:, offset:(width - offset), :]
    else:
        img = img[offset:(height - offset), :, :]
    img_new = Image.fromarray(img)
    img_new.resize((200, 200)).convert('RGB').save(fr'{img_name}')
    return True


def main():
    img_new = crop_image(r"test.png")


if __name__ == '__main__':
    main()

