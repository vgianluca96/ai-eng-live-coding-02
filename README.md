# AI Engineering Master Live Coding #02

Examples of tokenization using openai, deepseek and google tokenizers.

## Reuirements

* Python 3.12

## Quickstart

```powershell
# create python virtual env
python -m venv .venv

# activate virtual env
cd .venv
\scripts\activate

# install packages
pip install dotenv tiktoken transformers

# for google tokenization you can install this one
pip install --upgrade google-genai

# or you can install this one; note that the methods will change from the ones in this script
pip install "google-cloud-aiplatform[tokenization]"

```