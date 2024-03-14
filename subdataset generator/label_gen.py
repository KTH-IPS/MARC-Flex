import argparse
import os
import json

# parser = argparse.ArgumentParser(description="Generate a summary file of the json data.")
# parser.add_argument("input", type=str, help="input path")
# path = parser.parse_args().input+"/"
import sys

# skeleton_folder = '/home/zhihaoliu/ml_data/zhihao_video/debug2_skeleton_merged/'
MERGED_SKELETON_FOLDER = "/home/zhihaoliu/ml_data/hrc_dataset_0522_clipped/assembly/video_clips/XView/train/"
summary = {}

for (root, dirs, files) in os.walk(MERGED_SKELETON_FOLDER):
    for fname in files:
        [name, ext] = os.path.splitext(fname)
        if ext != '.json':
            continue

        with open(os.path.join(root, fname)) as f:
            data = json.load(f)

        has_skeleton = (data["data"] != [])
        entry = {"has_skeleton": has_skeleton, "label": data["label"], "label_index": data["label_index"]}
        summary[name] = entry

output_json = os.path.dirname(MERGED_SKELETON_FOLDER)+"_label.json"
print(output_json)
with open(output_json, 'w') as output:
    json.dump(summary, output, indent=4, sort_keys=True)
print("Label Gen Done.")
sys.exit()
