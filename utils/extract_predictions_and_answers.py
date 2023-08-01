import argparse
from tqdm import tqdm
import json


def extract_predictions_and_answers(input_file: str, output_folder: str):
    with open(input_file, "r") as f:

        counter = 0
        for line in tqdm(f.readlines()):
            parts = line.lstrip().split()
            if parts:
                keyword = parts[0]
                if keyword == "Answer:":
                    with open(f"{output_folder}{counter}_answer.html", "w") as f:
                        print(" ".join(parts[1:]), file=f)
                elif keyword == "Prediction:":
                    with open(f"{output_folder}{counter}_prediction.html", "w") as f:
                        print(" ".join(parts[1:]), file=f)
                elif keyword == "Normed":
                    with open(f"{output_folder}{counter}.json", "w") as f:
                        # The line starts with "Normed ED:", first two parts must be discarded
                        json.dump({"normed_ed": float(parts[2])}, f, indent=2)
                elif keyword == "Bleu:":
                    with open(f"{output_folder}{counter}.json", "r") as f:
                        dict_tmp = json.load(f)
                    dict_tmp["bleu"] = float(parts[1])
                    with open(f"{output_folder}{counter}.json", "w") as f:
                        json.dump(dict_tmp, f, indent=2)
                    
                    # Last line for each sample processed, pass to the next one
                    counter+= 1
    return


if __name__ == "__main__":
    output_folder = "results/"
    input_file = "examples/results_validation_SynthBootstrap_1000_epoch_39.txt"

    # Initialize args parser
    parser = argparse.ArgumentParser(description="Extract original files and predictions from input text file and save them separately",
                                     usage="python3 extract_predictions_and_answers.py --input_file {input_file} --output_folder {output_folder}")
    parser.add_argument(
        "--input_file", help="Input file with predictions and answers logged during validation / testing loop")
    parser.add_argument("--output_folder",
                        help="Folder where the output files are saved")

    # Read args
    args = parser.parse_args()

    if args.output_folder:
        output_folder = args.output_folder
        if not output_folder.endswith("/"):
            output_folder = output_folder + "/"

    if args.input_file:
        input_file = args.input_file

    extract_predictions_and_answers(input_file, output_folder)
