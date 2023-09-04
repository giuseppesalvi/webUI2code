import subprocess
import argparse
import os
import json
from tqdm import tqdm


def process_files(folder, suffix=".txt"):
    html_files = [file for file in os.listdir(folder) if file.endswith(suffix)] 
    for html_file_path in tqdm(html_files):
        if html_file_path.endswith("_processed" + suffix):
            # Already processed
            continue

        output_file_path = html_file_path.split(suffix)[0] + "_processed.html"
        errors_from_tidy = process_html(
            folder + html_file_path, folder + output_file_path)

        if html_file_path.endswith("pred" + suffix):
            dict_tmp = {}
            with open(folder + html_file_path.split("_pred")[0] + ".json", "w") as f:
                dict_tmp["errors"] =  cleanup_errors_from_tidy(errors_from_tidy)
                json.dump(dict_tmp, f, indent=2)


def process_html(input_file_path, output_file_path):
    command = f"tidy -indent -wrap 0 --drop-empty-elements no {input_file_path}"

    with open(output_file_path, "w") as f:
        result = subprocess.run(
            command, stdout=f, stderr=subprocess.PIPE, shell=True)

    errors = result.stderr.decode()

    return errors


def cleanup_errors_from_tidy(errors_original):
    lines = errors_original.splitlines()
    errors = []
    for line in lines:
        if line.startswith("Info"):
            break
        position = line.split("-")[0].rstrip()
        error_type = line.split("-")[1].split(":")[0].strip()
        error_message = line.split("-")[1].split(":")[1].lstrip()
        error = {}
        error["position"] = position
        error["error_type"] = error_type
        error["error_message"] = error_message
        errors.append(error)

    return errors


if __name__ == "__main__":
    folder = "results/demo"

    # Initialize args parser
    parser = argparse.ArgumentParser(description="post-processing of predictions and answers with correction of syntax errors",
                                     usage="python3 postprocessing.py --folder {folder}")
    parser.add_argument("--folder", help="Folder with files to process")

    # Read args
    args = parser.parse_args()

    if args.folder:
        folder = args.folder
        if not folder.endswith("/"):
            folder = folder + "/"

    process_files(folder)
