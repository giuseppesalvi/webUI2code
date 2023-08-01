import argparse
import os
import json
from tqdm import tqdm
from html_ted.main import calculate_ted_from_file_paths


def calculate_metrics(folder: str):
    json_files= [file for file in os.listdir(folder) if file.endswith('.json')] 

    sum_ted = 0
    for json_file in tqdm(json_files):

        with open(folder + json_file, "r") as fr:
            json_dict = json.load(fr)

        answer_file_path = folder + json_file.replace(".json", "_answer_processed.html")
        prediction_file_path = folder + json_file.replace(".json", "_prediction_processed.html")
        
        # HTML Tree edit distance
        ted = calculate_ted_from_file_paths(answer_file_path, prediction_file_path)

        # TODO: visual similarity
        # TODO: visual dissimilarity

        json_dict["ted"] = ted

        sum_ted += ted

        with open(folder + json_file, "w") as fw:
            json.dump(json_dict, fw, indent=2)
    return sum_ted/len(json_files)

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

    avg_ted = calculate_metrics(folder)
    print("Avg HTML Tree Edit Distance = ", avg_ted)
