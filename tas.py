# from pynput.keyboard import Key
# import pynput, time

# # keyboard = pynput.keyboard.Controller()
# all_times = []
# all_keys = []

# def on_press(key):
#     try:
#         return 'alphanumeric key {0} pressed'.format(
#             key.char)
#     except AttributeError:
#         pass

# def on_release(key):
#     # print('{0} released'.format(
#     #     key.char))
#     if key == pynput.keyboard.Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with pynput.keyboard.Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()
#     print(listener)
#     # if key in (Key.space, Key.up, Key.left, Key.down, Key.right):
#     #         all_times.append(time.time())
#     #         all_keys.append(key)


# # ...or, in a non-blocking fashion:
# # listener = pynput.keyboard.Listener(
# #     on_press=on_press,
# #     on_release=on_release)
# # listener.start()

# print(all_times)
# print(all_keys)



# import pygame, time

# all_times = []
# all_keys = []

# running = True

# scrn = pygame.display.set_mode((200, 200))

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.KEYDOWN:
#             curr_key = pygame.key.name(event.key)
#             if curr_key in ("space", "up", "left", "down", "right"):
#                 all_times.append(time.process_time())
#                 all_keys.append(curr_key)

# pygame.quit()

# print(all_times)
# print(all_keys)



# import keyboard, numpy as np, time

# all_times = []
# all_keys = []
# prev = False

# while True:
#     curr_key = keyboard.read_key()
#     if curr_key in ("space", "up", "left", "down", "right") and not(prev):
#         all_times.append(time.time())
#         all_keys.append(curr_key)
#         prev = True
#     elif curr_key == "esc":
#         break
#     else:
#         prev = False

# all_times = list(np.array(all_times) - np.array([all_times[0] - 5] + all_times[:-1]))

# print(all_times)
# print([' '] + [f"{{{x.upper()}}}" for x in all_keys[1:]])



# from pynput.keyboard import Key
# import pynput, time

# keyboard = pynput.keyboard.Controller()

# all_times = [5.0, 7.992378234863281, 9.388375282287598, 10.747880697250366, 11.521379470825195, 12.252097368240356, 13.620063781738281, 15.018600702285767, 16.75785517692566, 17.331881046295166, 17.745879888534546, 18.480449676513672, 18.935879707336426, 19.28401517868042, 19.617943286895752, 19.982378482818604, 20.184375524520874, 20.397918939590454, 20.827932119369507, 20.99142098426819, 21.3482928276062, 21.597907781600952, 21.838374853134155, 22.062378644943237, 22.428401231765747, 22.778908491134644, 23.031378746032715, 23.24736452102661, 23.820894479751587, 24.203836917877197, 24.590893268585205, 24.974915504455566, 25.255887985229492, 25.639894723892212, 25.87084412574768, 26.064380407333374, 26.426924228668213, 26.584379196166992, 26.986640453338623, 27.227421045303345, 27.460375785827637, 27.723930597305298, 28.064481258392334, 28.43181300163269, 28.716904878616333, 28.891154050827026, 30.91588306427002, 31.271955251693726, 31.66282320022583, 31.797791719436646, 32.157891511917114, 32.31061792373657, 32.469887495040894, 32.856908321380615, 33.00489950180054, 33.376890897750854, 34.09275412559509, 34.466737031936646, 34.811787128448486, 36.17587757110596]
# # all_keys = ['space', 'down', 'down', 'left', 'down', 'right', 'up', 'left', 'up', 'up', 'up', 'up', 'up', 'left', 'left', 'right', 'right', 'right', 'down', 'down', 'up', 'up', 'up', 'left', 'left', 'up', 'up', 'up', 'right', 'down', 'down', 'left', 'left', 'right', 'right', 'right', 'up', 'up', 'left', 'left', 'left', 'down', 'down', 'up', 'up', 'up', 'right', 'right', 'down', 'down', 'up', 'up', 'up', 'up', 'up', 'right', 'left', 'left', 'right', 'up']

# # print([f"{{{x.upper()}}}" for x in all_keys])

# # t_0 = time.time()
# # dt = 0.05

# for i in range(len(all_times)):
#     # while True:
#         # print(time.time() - t_0 - all_times[i])
#         # if time.time() - t_0 - all_times[i] > -dt:
#         #     if all_keys[i] == "space":
#         #         keyboard.press(Key.space)
#         #         keyboard.release(Key.space)
#         #     elif all_keys[i] == "up":
#         #         keyboard.press(Key.up)
#         #         keyboard.release(Key.up)
#         #     elif all_keys[i] == "left":
#         #         keyboard.press(Key.left)
#         #         keyboard.release(Key.left)
#         #     elif all_keys[i] == "down":
#         #         keyboard.press(Key.down)
#         #         keyboard.release(Key.down)
#         #     elif all_keys[i] == "right":
#         #         keyboard.press(Key.right)
#         #         keyboard.release(Key.right)
#         #     break
#     time.sleep(1)
#     keyboard.press(Key.left)
#     time.sleep(0.01)
#     keyboard.release(Key.left)



import cv2, keyboard as k, mss, numpy as np, pynput, time

# threshold = 58
threshold = 20
# threshold = 0
top = 1166
w = 10
h = 10
hold_tm = 0.05
keyboard = pynput.keyboard.Controller()

with mss.mss() as sct:
    # Part of the screen to capture
    # monitor_l = {"top": 1056, "left": 910, "width": 1083 - 910, "height": 1212 - 1046}
    # monitor_u = {"top": 1056, "left": 1083, "width": 1083 - 910, "height": 1212 - 1046}
    # monitor_d = {"top": 1056, "left": 1268, "width": 1083 - 910, "height": 1212 - 1046}
    # monitor_r = {"top": 1056, "left": 1453, "width": 1083 - 910, "height": 1212 - 1046}
    monitor_l = {"top": top, "left": 998, "width": w, "height": h}
    monitor_u = {"top": top, "left": 1179, "width": w, "height": h}
    monitor_d = {"top": top, "left": 1360, "width": w, "height": h}
    monitor_r = {"top": top, "left": 1541, "width": w, "height": h}

    while "Screen capturing":
        last_time = time.time()
        time.sleep(0.02)

        # Get raw pixels from the screen, save it to a Numpy array
        img_l = np.array(sct.grab(monitor_l))
        img_u = np.array(sct.grab(monitor_u))
        img_d = np.array(sct.grab(monitor_d))
        img_r = np.array(sct.grab(monitor_r))
        std_l = np.std(img_l)
        std_u = np.std(img_u)
        std_d = np.std(img_d)
        std_r = np.std(img_r)
        # print(std_l, std_u, std_d, std_r)
        if std_l > threshold:
            keyboard.press('a')
            time.sleep(hold_tm)
            keyboard.release('a')
            print('a')
        elif std_u > threshold:
            keyboard.press('w')
            time.sleep(hold_tm)
            keyboard.release('w')
            print('w')
        elif std_d > threshold:
            keyboard.press('s')
            time.sleep(hold_tm)
            keyboard.release('s')
            print('s')
        elif std_r > threshold:
            keyboard.press('d')
            time.sleep(hold_tm)
            keyboard.release('d')
            print('d')

        # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # print(f"fps: {1 / (time.time() - last_time)}")

        # Press "q" to quit
        # if cv2.waitKey(25) & 0xFF == ord("q"):
        #     cv2.destroyAllWindows()
        #     break

        if k.is_pressed('q'):
            break

# from pynput.mouse import Button
# import keyboard, pynput

# mouse = pynput.mouse.Controller()
# prev = False

# while True:
#     a = keyboard.is_pressed('a')
#     if a and not(prev):
#         print(mouse.position)
#         prev = True
#     elif not(a):
#         prev = False