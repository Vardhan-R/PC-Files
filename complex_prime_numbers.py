import matplotlib.pyplot as plt

composite_re_part = []
composite_im_part = []

max_real = 6
max_imaginary = 6

for a in range(max_real):
    for b in range(max_imaginary):
        for c in range(max_real):
            for d in range(max_imaginary):
                temp = (a + b * 1j) * (c + d * 1j) * int(not((a == 1 and b == 0) or (c == 1 and d == 0)))
                composite_re_part.append(temp.real)
                composite_im_part.append(temp.imag)

# for a in range(max_real):
#     for b in range(max_imaginary):
#         for c in range(max_real):
#             for d in range(max_imaginary):
#                 temp = (a + b * 1j) / (c + d * 1j) * int(not((a == 1 and b == 0) or (c == 1 and d == 0)))
#                 composite_re_part.append(temp.real)
#                 composite_im_part.append(temp.imag)

plt.scatter(composite_re_part, composite_im_part)
# plt.xlim(left=0)
plt.xlim(0, 5)
plt.ylim(0, 5)
plt.show()