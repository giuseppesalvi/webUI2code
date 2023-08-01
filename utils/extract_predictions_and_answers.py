import argparse


def extract_predictions_and_answers(input_file: str, output_folder: str):
    with open(input_file, "r") as f:

        counter_prediction = 0
        counter_answer = 0
        for line in f.readlines():
            parts = line.lstrip().split()
            if parts:
                keyword = parts[0]
                if keyword == "Answer:":
                    with open(f"{output_folder}{counter_answer}_answer.html", "w") as fa:
                        print(" ".join(line.lstrip().split()[1:]), file=fa)
                    counter_answer += 1
                elif keyword == "Prediction:":
                    with open(f"{output_folder}{counter_prediction}_prediction.html", "w") as fp:
                        print(" ".join(line.lstrip().split()[1:]), file=fp)
                        counter_prediction += 1
    return


if __name__ == "__main__":
    output_folder = "results/"
    input_file = "examples/results_validation_SynthBootstrap_1000_epoch_39.txt"

    # Initialize args parser
    parser = argparse.ArgumentParser(description="Extract original files and predictions from input text file and save them separately",
                                     usage="python3 extract_predictions_and_answers.py --input_file {input_file} --output_folder {output_folder}")
    parser.add_argument("--input_file", help="Input file with predictions and answers logged during validation / testing loop")
    parser.add_argument("--output_folder", help="Folder where the output files are saved")

    # Read args
    args = parser.parse_args()

    if args.output_folder:
        output_folder = args.output_folder
        if not output_folder.endswith("/"):
            output_folder = output_folder + "/"

    if args.input_file:
        input_file = args.input_file

    extract_predictions_and_answers(input_file, output_folder)
