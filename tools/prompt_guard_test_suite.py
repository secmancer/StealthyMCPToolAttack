import os

import inference
from transformers import pipeline

API_KEY_PATH = "../API_KEY"
TEST_TEXT_FILE_PATH = "../test/prompt_guard_test_case.txt"
TOKEN_NAME = "HF_TOKEN"


# Set the API key from the environment variable or a file
def set_api_key():
    API_KEY = open(API_KEY_PATH).read().strip()
    os.environ[TOKEN_NAME] = API_KEY


# Open a text file and return its contents
def open_text_file(file_path):
    with open(file_path, "r") as f:
        return f.read()


# Main function to run the prompt guard test suite
if __name__ == "__main__":
    # Set the API key and get the text to test
    set_api_key()
    text = open_text_file(TEST_TEXT_FILE_PATH)

    # Load the model and tokenizer
    model, tokenizer, device = inference.load_model_and_tokenizer(
        "meta-llama/Llama-Prompt-Guard-2-86M"
    )

    # Obtain the class scores for the texts
    scores = inference.get_class_scores(model, tokenizer, text)

    # Print the label for the text
    print("Label:", model.config.id2label[scores.argmax().item()])

    # Print the score for the text
    print("Score:", scores.max().item())
