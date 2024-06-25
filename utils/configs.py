import argparse


parser = argparse.ArgumentParser(description="Run the summarization model with custom parameters")
parser.add_argument("--max_length", type=int, default=56, help="The maximum length of the summary")
parser.add_argument("--chunk_size", type=int, default=4800, help="limit the length for the text")

args = parser.parse_args()