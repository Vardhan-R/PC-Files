import matplotlib.pyplot as plt

txt_file = open("python_files/sample_data.txt", 'r')
full_lst = txt_file.readlines()
txt_file.close()

x = []
y = []

for i in range(len(full_lst)):
    x.append(i)
    y.append(float(full_lst[i][:7]))

plt.plot(x, y)
plt.show()
