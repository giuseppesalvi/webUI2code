import argparse
import os
import json
from tqdm import tqdm
from html_ted.main import calculate_ted_from_file_paths
from skimage.metrics import structural_similarity as ssim
import cv2
from matplotlib.figure import Figure
import numpy as np


def calculate_ssim_index(imageA_path, imageB_path, index_sample):
    imageA = cv2.imread(imageA_path)
    imageB = cv2.imread(imageB_path)

    imageB = cv2.resize(imageB, (imageA.shape[1], imageA.shape[0]))

    imageA_gray = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    imageB_gray = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    ssim_index, gradient, ssim_map = ssim(imageA_gray, imageB_gray, full=True, gradient=True)


    # Create a figure for the SSIM map
    fig_ssim = Figure(figsize=(6, 6))
    ax_ssim = fig_ssim.add_subplot(1, 1, 1)
    ax_ssim.imshow(ssim_map, cmap='Blues', vmin=-1, vmax=1)
    ax_ssim.set_title("SSIM map")
    fig_ssim.colorbar(ax_ssim.imshow(ssim_map, cmap="Blues", vmin=-1, vmax=1), ax=ax_ssim)
    fig_ssim.savefig(f"{folder}{index_sample}_ssim_map.png")

    # Create a figure for the gradient map
    gradient_magnitude = np.sqrt(np.square(gradient))
    fig_gradient = Figure(figsize=(6, 6))
    ax_gradient = fig_gradient.add_subplot(1, 1, 1)
    ax_gradient.imshow(gradient_magnitude, cmap="Blues")
    ax_gradient.set_title("Gradient map")
    fig_gradient.colorbar(ax_gradient.imshow(gradient_magnitude, cmap="Blues"), ax=ax_gradient)
    fig_gradient.savefig(f"{folder}{index_sample}_gradient_map.png")

    return ssim_index

def calculate_metrics(folder: str):
    json_files= [file for file in os.listdir(folder) if file.endswith('.json')] 

    sum_ted = 0
    sum_ssim_index = 0
    for json_file in tqdm(json_files):

        with open(folder + json_file, "r") as fr:
            json_dict = json.load(fr)

        answer_file_path = folder + json_file.replace(".json", "_answer_processed.html")
        prediction_file_path = folder + json_file.replace(".json", "_prediction_processed.html")
        
        # HTML Tree edit distance
        ted = calculate_ted_from_file_paths(answer_file_path, prediction_file_path)

        # Structural visual similarity
        answer_png_file_path = folder + json_file.replace(".json", "_answer_processed.png")
        prediction_png_file_path = folder + json_file.replace(".json", "_prediction_processed.png")

        ssim_index = calculate_ssim_index(answer_png_file_path, prediction_png_file_path, json_file.split(".")[0])

        json_dict["ted"] = ted
        json_dict["ssim_index"] = ssim_index 

        sum_ted += ted
        sum_ssim_index += ssim_index

        with open(folder + json_file, "w") as fw:
            json.dump(json_dict, fw, indent=2)
    return sum_ted/len(json_files), sum_ssim_index/len(json_files)

if __name__ == "__main__":
    folder = "results/"

    # Initialize args parser
    parser = argparse.ArgumentParser(description="Calculate metrics for predictions",
                                     usage="python3 calculate_metrics.py --folder {folder}")
    parser.add_argument("--folder",
                        help="Folder with files to calculate metrics")

    # Read args
    args = parser.parse_args()

    if args.folder:
        folder = args.folder
        if not folder.endswith("/"):
            folder = folder + "/"

    avg_ted, avg_ssim_index = calculate_metrics(folder)
    print(f"Avg HTML Tree Edit Distance = {avg_ted:.2f}")
    print(f"Avg SSIM indesx = {avg_ssim_index:.2f}")
