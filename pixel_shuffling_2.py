from PIL import Image
import matplotlib.pyplot as plt, numpy as np, random

r = [x for x in range(256)]
g = r.copy()
b = r.copy()
random.seed(10)
random.shuffle(r)
random.shuffle(g)
random.shuffle(b)

r = np.array(r)
g = np.array(g)
b = np.array(b)

# im = Image.open("ai_dataset/category_0/category_0_img_0.jpg", 'r')
# pixels_lst = list(im.getdata())
# img_size = im.size

# pix = im.load()

# for i in range(len(pixels_lst)):
#     temp = pixels_lst[i]
#     pix[i % img_size[0], i // img_size[0]] = (r[temp[0]], g[temp[1]], b[temp[2]])

# # plt.figure()
# # plt.imshow(im)
# # plt.show()

# im.save("ai_dataset/category_0/category_0_img_0_edited.png")

im = Image.open("ai_dataset/category_0/category_0_img_0_edited.png", 'r')
pixels_lst = list(im.getdata())
img_size = im.size

pix = im.load()

for i in range(len(pixels_lst)):
    temp = pixels_lst[i]
    pix[i % img_size[0], i // img_size[0]] = (np.argwhere(r == temp[0])[0][0], np.argwhere(g == temp[1])[0][0], np.argwhere(b == temp[2])[0][0])

plt.figure()
plt.imshow(im)
plt.show()

# im.save("ai_dataset/category_0/category_0_img_0_restored.png")