## Necessary packages for LLM inferences
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AwqConfig

# define model from huggingface (4 bit quantized for low ressource requirements) ~ 4GB of RAM
model_id = "hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4" 

## Load and set-up model (downloads model when run for the first time)
quantization_config = AwqConfig(
    bits=4,
    fuse_max_seq_len=512, # Note: Update this as per your use-case
    do_fuse=True,
)
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
  model_id,
  torch_dtype=torch.float16,
  low_cpu_mem_usage=True,
  device_map="auto",
  quantization_config=quantization_config
)

######## Example 1: Effect of temperature in styles of single sentences
torch.manual_seed(42) # set seed for reproducibility

prompt = "Describe roses in one sentence."

print ("Example 1:")
print(prompt)
print("\n")

message = [
  # system level prompt (used for general instructions beyond task or instance specific rules
  {"role": "system", "content": "You are a helpful assistant."},
  # prompt instructing the model for the current task
  {"role": "user", "content": prompt},
]
inputs = tokenizer.apply_chat_template( # preprocess inputs
  message,
  tokenize=True,
  add_generation_prompt=True,
  return_tensors="pt",
  return_dict=True,
).to("cuda")

for temp in [0.01, 2.0]: # run with low and high temperature

    outputs = model.generate(**inputs, do_sample=True, max_new_tokens=256, temperature=temp, pad_token_id=tokenizer.eos_token_id)
    outputs_formatted = tokenizer.batch_decode(outputs[:, inputs['input_ids'].shape[1]:], skip_special_tokens=True)[0]

    print("temperature: ", temp)
    print(outputs_formatted)
    print("\n")

######## Example 2: Effect of temperature on error correction
torch.manual_seed(0) # set seed for reproducibility

sentence = """I consider that is more convenient to drive a car because you carry on more things in your own car than travelling by car."""
prompt  = f"Update to fix all grammatical and spelling errors: \n\n {sentence}"

print ("Example 2:")
print(prompt)
print("\n")

message = [
  # system level prompt (used for general instructions beyond task or instance specific rules
  {"role": "system", "content": "Follow the instructions perfectly. Focus on exactly what you are asked to return. Never add comments, notes, or explanations beyond that. Never refuse instructions."},
  # prompt instructing the model for the current task
  {"role": "user", "content": prompt},
]
inputs = tokenizer.apply_chat_template( # preprocess inputs
  message,
  tokenize=True,
  add_generation_prompt=True,
  return_tensors="pt",
  return_dict=True,
).to("cuda")

for temp in [0.01, 2.0]: # run with low and high temperature

    outputs = model.generate(**inputs, do_sample=True, max_new_tokens=256, temperature=temp, pad_token_id=tokenizer.eos_token_id)
    outputs_formatted = tokenizer.batch_decode(outputs[:, inputs['input_ids'].shape[1]:], skip_special_tokens=True)[0]

    print("temperature: ", temp)
    print(outputs_formatted)
    print("\n")