import argparse
import os

# parser = argparse.ArgumentParser(description='Make json files from movies')
# parser.add_argument('openpose', type=str, help='openpose directory path')
# parser.add_argument('input', type=str, help='input path')
# path = parser.parse_args().input+'/'
import sys

"""
This generator is used for process multiple videos in a folder and only one video for one each label, by openpose, from video to skeleton
"""

openpose_path = "/home/zhihaoliu/openpose160/openpose-1.6.0"
# input_folder = '/home/zhihaoliu/ml_data/zhihao_video/debug/'
openpose_bin = '/home/zhihaoliu/openpose160/openpose-1.6.0/build/examples/openpose/openpose.bin'
VIDEO_FOLDER = "/home/zhihaoliu/ml_data/hrc_dataset_0609_clipped/assembly/video_clips/clips/"
# TEST_FOLDER = "/home/zhihaoliu/ml_data/zhihao_video/clips_test/"


def run_openpose(video_path, save=None, custom_model=False, custom_model_pose=False, hand=False, show=False, norm=False,
                 two_people=True):
    write_json = ''
    display = ''
    option_hand = ''
    keypoint_scale = None
    max_people = None
    if save != None:
        write_json = '--write_json %s' % (save)
    if custom_model:
        model_folder = '--model_folder /home/zhihaoliu/openpose160/openpose-1.6.0/models/'
    if custom_model_pose:
        model_pose = '--model_pose COCO'
    if hand:
        option_hand = '--hand'
    if not show:
        display = '--display 0 --render_pose 0'
    if norm:
        keypoint_scale = '--keypoint_scale 3'
    if two_people:
        max_people = '--number_people_max 2'

    openpose = openpose_bin + ' '
    option = '--video %s %s %s %s %s %s %s %s' % (video_path, option_hand, model_folder, model_pose, write_json,
                                                        display, keypoint_scale, max_people)

    # print(openpose + option)
    os.system(openpose + option)  # run a shell command


# os.chdir(openpose_bin)

dirname = os.path.dirname(VIDEO_FOLDER) + '_skeleton/'
if not os.path.exists(dirname):
    os.mkdir(dirname)

"""
os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。
os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。
在Unix，Windows中有效。
"""
for (root, dirs, files) in os.walk(VIDEO_FOLDER):
    print((root, dirs, files))
    index = 0
    for fname in files:
        run_openpose(video_path=os.path.join(root, fname),
                     save=dirname + fname.split('.')[0],
                     custom_model=True,
                     custom_model_pose=True,
                     show=False,
                     norm=False,
                     two_people=False)
        index += 1
        print("[%d/%d] %s has been processed by openpose successfully!" % (index, len(files), fname.split('.')[0]))
print("ALL DONE!")
sys.exit()
