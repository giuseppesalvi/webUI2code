import argparse
import os
import json
from tqdm import tqdm
from html_ted.main import calculate_ted, extract_html_tree
from skimage.metrics import structural_similarity as ssim
import cv2
from matplotlib.figure import Figure
import numpy as np
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction
from nltk import edit_distance

import multiprocessing
from itertools import product

import time


def calculate_ssim_index(folder, imageA_path, imageB_path, index_sample):
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


def calculate_metric(args):
    json_file, folder = args
    with open(folder + json_file, "r") as fr:
            json_dict = json.load(fr)

    answer_file_path = folder + json_file.replace(".json", "_answer_processed.html")
    prediction_file_path = folder + json_file.replace(".json", "_pred_processed.html")
    
    with open(prediction_file_path, 'r') as f:
        pred = f.read()
        pred_html = extract_html_tree(pred)

    with open(answer_file_path, 'r') as f:
        answer = f.read()
        answer_html = extract_html_tree(answer)

    # HTML Tree edit distance
    ted = calculate_ted(answer_html, pred_html)
    # Normalized Edit Distance
    ed_score = edit_distance(pred, answer) / max(len(pred), len(answer))
    
    # Bleu Score
    bleu_score = corpus_bleu([[answer]], [pred], smoothing_function=SmoothingFunction().method4)
   
    # Structural visual similarity
    answer_png_file_path = folder + json_file.replace(".json", "_answer_processed.png")
    prediction_png_file_path = folder + json_file.replace(".json", "_pred_processed.png")

    ssim_index = calculate_ssim_index(folder, answer_png_file_path, prediction_png_file_path, json_file.split(".")[0])
    json_dict["bleu"] = bleu_score
    json_dict["ed"] = ed_score 
    json_dict["ted"] = ted
    json_dict["ssim_index"] = ssim_index 
    with open(folder + json_file, "w") as fw:
        json.dump(json_dict, fw, indent=2)      
    
    return ted, ssim_index, ed_score, bleu_score                
    
if __name__ == "__main__":
    folder = "results/demo"

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
    json_files= [file for file in os.listdir(folder) if file.endswith('.json')]
    print(f"Number of files: {len(json_files)}")
    start = time.time()
    pool_size = multiprocessing.cpu_count()

    with multiprocessing.Pool(processes=pool_size) as pool:
        results = []
        for result in tqdm(pool.imap_unordered(func=calculate_metric, iterable=[(filename, folder) for filename in json_files]), total=len(json_files)):
            results.append(result)

    teds, ssims, eds, bleus = zip(*results)
    avg_ted = np.mean(teds)
    avg_ssim_index = np.mean(ssims)
    avg_ed = np.mean(eds)
    avg_bleu = np.mean(bleus)



    print(f"Avg HTML Tree Edit Distance = {avg_ted:.3f}")
    print(f"             Avg SSIM index = {avg_ssim_index:.3f}")
    print(f"   Avg Normed Edit Distance = {avg_ed:.3f}")
    print(f"             Avg Bleu Score = {avg_bleu:.3f}")
    
    print(f"/nExecution time: {time.time() - start}")
    


