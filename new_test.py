def predict(self, text):
    # Tokenize the input text
    inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")

    # Get model output (assuming outputs logits)
    outputs = self.model(**inputs)

    # Calculate probabilities from logits
    logits = outputs.logits
    probs = logits.softmax(dim=1)

    # Get the index of the maximum probability
    pred_label_idx = probs.argmax(dim=1)

    # Convert predicted label index to label name
    # Ensure your model config or some dictionary maps indices to label names
    pred_label = self.model.config.id2label[pred_label_idx.item()]

    return probs, pred_label_idx, pred_label