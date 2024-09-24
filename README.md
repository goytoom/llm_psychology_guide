# Overview
This is the repository to the paper "Evaluating Large Language Models for Psychological Research: A Reporting Guideline".
We provide all codes, data, and instructions to replicate the examples shown in the paper. We further provide the exact prompts as well as model parameters and the instructions to replicate our python programming environment.

## Hardware Overview/Recommendations
We tested the model on an NVIDIA RTX 4090 with 24GB VRAM on a Linux machine (Ubuntu 22.04 and Windows Subsystem for Linux).
The model requires around 4GB of VRAM and should work on any modern NVIDIA GPU (e.g., Pascal architecture or newer).
It should also work on systems without GPU (CPU inference).

It does currently not work on Macs but support for Macs with M-series chips will be added soon.

## Data
No external data is necessary for replicating the examples shown in the paper. They require only prompting the model as shown in the code files and using the same model parameters.

We provide the files `environment.yaml` and `requirements.txt` to reproduce the python environment with conda and pip.

## Code Files
We provide a single python script (`replication.py`) that contains the prompts, model settings, and LLM queries for replicating the examples in the paper. 

## LLM Details
We used the opensource LLaMA-3.1 model, specifically a 4bit quantized version from huggingface:
[hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4](url). 

# Instructions for replication
## Setting up the python environment
- Download this repository. If using git from the command line run: `git clone https://github.com/goytoom/llm_psychology_guide`
- Enter the directory using `cd llm_psychology_guide`
- Using the command line run `conda env create --file environment.yml` (this will create a virtual python environment with the required python version)
- Using the command line run `conda activate replication` (activate the environment)
- Using the command line run `pip install -r requirements.txt` (this will install the necessary packages in this environment)

## Executing the replication
- Using the command line run `conda activate replication` to activate the python programming environment
- Run the replication script in the command line: `python replication.py`

This should output the prompts used in the example and the model's response:

![alt text](image.png)
