# data una stringa, tokenizzarla con il tokenizer di OpenAI
import tiktoken
from dotenv import load_dotenv
from transformers import AutoTokenizer
from google.genai.local_tokenizer import LocalTokenizer

load_dotenv()

text="parlami della caduta dell'impero romano, spiega le cause che hanno portato alla caduta parlami della caduta dell'impero romano, spiega le cause che hanno portato alla caduta parlami della caduta dell'impero romano, spiega le cause che hanno portato alla caduta parlami della caduta dell'impero romano, spiega le cause che hanno portato alla caduta"

print(repr(text))


# openAI
def count_openai(text, encoding="o200k_base"):
    enc = tiktoken.get_encoding(encoding)
    ids = enc.encode(text)
    pieces = [enc.decode([id]) for id in ids]
    return ids,pieces

print("****************************************** OpenAI")
for encoding in ["o200k_base","cl100k_base"]:
    ids,pieces=count_openai(text,encoding)
    print(f"{encoding} -> {len(ids)} token")
    #print (f"pezzi: {pieces}")


# deepseek
tok_deepseek = AutoTokenizer.from_pretrained(
    "deepseek-ai/DeepSeek-V3", trust_remote_code=True
)

def count_deepseek(text):
    ids=tok_deepseek.encode(text,add_special_tokens=False)
    pieces=[tok_deepseek.decode([id]) for id in ids]
    return ids,pieces

ids,pieces=count_deepseek(text)
print("****************************************** Deepseek")
print(f"{len(ids)} token")
#print(f"pezzi: {pieces}")

# Gemini
print("****************************************** Gemini")
tok_gemini = LocalTokenizer(model_name="gemini-2.5-flash")

def count_gemini(text):
    return tok_gemini.count_tokens(text).total_tokens
tokens=count_gemini(text)
print(f"{tokens} token")