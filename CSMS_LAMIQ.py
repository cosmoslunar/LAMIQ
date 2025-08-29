import subprocess, sys, torch
from colorama import Fore, init
init(autoreset=True)

def install(pkg):
    try: __import__(pkg)
    except ImportError:
        print(Fore.GREEN+"[INFO] Installing "+pkg)
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

for package in ["torch", "transformers", "bitsandbytes", "colorama"]:
    install(package)

from transformers import AutoTokenizer, AutoModelForCausalLM

print(Fore.GREEN+"{poweredbyqwen×cosmos_LAMIQ(localaimodelsincludingqwen)}")
print(Fore.GREEN+"[INFO] Type 'exit' anytime to quit the program.")

use_gpu = input(Fore.GREEN+"Do you have a GPU? (y/n): ").lower().strip()

if use_gpu == "y" and torch.cuda.is_available():
    MODEL_NAME = "TheBloke/Qwen-14B-Chat-GPTQ"
    device = "cuda"
else:
    MODEL_NAME = "TheBloke/Qwen-7B-Chat-GPTQ"
    device = "cpu"

print(Fore.GREEN+"[INFO] Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto" if device=="cuda" else "cpu",
    low_cpu_mem_usage=(device=="cpu")
)

while True:
    prompt = input(Fore.GREEN+"You> ")
    if prompt.lower() in ("exit", "quit"):
        print(Fore.GREEN+"[INFO] Exiting...")
        break

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(Fore.GREEN+"AI >", response)