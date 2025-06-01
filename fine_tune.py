from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from peft import LoraConfig, get_peft_model
from datasets import load_dataset
import torch

model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
model = AutoModelForCausalLM.from_pretrained(model_name, load_in_4bit=True, device_map="auto")
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

dataset = load_dataset("json", data_files="music_data.jsonl", split="train")
def preprocess(example):
    prompt = example["prompt"]
    completion = example["completion"]
    full_text = f"### Instruction: {prompt} ### Response: {completion}"
    return tokenizer(full_text, truncation=True, padding="max_length", max_length=128)

dataset = dataset.map(preprocess, batched=True)
dataset.set_format("torch", columns=["input_ids", "attention_mask"])

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, lora_config)

training_args = TrainingArguments(
    output_dir="./fine_tuned_mistral",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=3,
    save_steps=100,
    logging_steps=10,
    fp16=True,
    remove_unused_columns=False
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

trainer.train()
model.save_pretrained("./fine_tuned_mistral")
tokenizer.save_pretrained("./fine_tuned_mistral")