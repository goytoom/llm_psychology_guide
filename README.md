# Overview
This is the repository to the "Evaluating Large Language Models for Psychological Research" project.
We provide all codes, data, and instructions to replicate the examples shown in the paper. We further provide the exact prompts as well as model parameters and the instructions to replicate our python programming environment.

## Data
No external data is necessary for replicating the examples shown in the paper. They require only prompting the model as shown in the code files and using the same model parameters.

## Code files
We provide a single python script (replication.py) that contains the prompts, model settings, and LLM queries. 

## LLM details
We used the opensource LLaMA-3 model, specifically its 8bit quantized version from huggingface:
[https://huggingface.co/LoneStriker/Meta-Llama-3-8B-Instruct-8.0bpw-h8-exl2](url). We used text-generation-web-ui as the backend to handle the model queries. We have forked the original repository by "oobabooga" to provide a long-term stable version that can replicate our specific results: [https://github.com/goytoom/text-generation-webui](https://github.com/goytoom/text-generation-webui).

# Instructions for replication
## Setting up the backend
- Download the repository of the backend. If using git from the command line run: `git clone https://github.com/goytoom/text-generation-webui`
- Enter the folder using `cd text-generation-webui`
- Run the start_linux.sh, start_windows.bat, start_macos.sh, or start_wsl.bat script depending on your OS.
- Select your GPU vendor when asked.
- Once the installation ends, browse to [http://localhost:7860](url)
- Navigate to the "Model" Tab
- Paste `https://huggingface.co/LoneStriker/Meta-Llama-3-8B-Instruct-8.0bpw-h8-exl2` in the download field and press download (this will download the model weights of the LLM)

## Setting up the programming environment
- Download this repository. If using git from the command line run: `git clone https://github.com/goytoom/llm_psychology_guide`
- In the command line run `conda create -n "replication" python==3.11` (this will create a virtual programming environment)
- In the command line run `conda activate replication`
- In the command line run `pip install -r requirements.txt` (this will install the necessary packages in this environment)

## Executing the replication
- Activate the backend by executing in the commandline `start_linux.sh`, `start_windows.bat`, `start_macos.sh`, or `start_wsl.bat` based on your operating system
- Choose and load your model in the Model tab after opening the backend interface in a browser: [http://localhost:7860](url)
- Activate the "api" function in the "Session" tab
- In the command line run `conda activate replication` to activate the python programming environment
- run the replication script in the command line: `python replication.py`

This should output the prompts used in the example and the model's response.


