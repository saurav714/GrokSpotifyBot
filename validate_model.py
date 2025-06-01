import os
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from sklearn.metrics import accuracy_score

model_path = os.path.join(os.path.dirname(__file__), "fine_tuned_distilbert")
model = AutoModelForSequenceClassification.from_pretrained(model_path).to("cpu")
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Sample test data
test_data = [
    {"text": "This song is so depressing!", "label": 0},
    {"text": "Love this uplifting track!", "label": 1},
    {"text": "It’s an okay song.", "label": 2}
]

predictions = []
true_labels = []
for item in test_data:
    inputs = tokenizer(item["text"], return_tensors="pt", padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_class = torch.argmax(outputs.logits, dim=1).item()
    predictions.append(predicted_class)
    true_labels.append(item["label"])

accuracy = accuracy_score(true_labels, predictions)
print(f"Model accuracy: {accuracy:.2f}")