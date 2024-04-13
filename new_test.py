import pickle
import io
import torch

class CPU_Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == 'torch.storage' and name == '_load_from_bytes':
            return lambda b: torch.load(io.BytesIO(b), map_location='cpu')
        else:
            return super().find_class(module, name)

#contents = pickle.load(f) becomes...


model_file_path = './model/trained_model_cuda.sav'
with open(model_file_path, 'rb') as f:
    # Use the custom unpickler to load the model file
    model = CPU_Unpickler(f).load()

print(model)


input_data = "หวัดดี"  # Replace with your actual input data

# Convert input data to a PyTorch tensor
input_tensor = torch.tensor(input_data)

# 2. Set the model to evaluation mode
model.eval()

# 3. Perform the prediction
# Use a context manager to avoid tracking gradients during inference
with torch.no_grad():
    # Perform the forward pass of the model
    output = model(input_tensor)

# 4. Process the output
# Depending on the model's output format, process it to get the final prediction
# For example, if the output is a classification, you might take the argmax
# Replace the following line with your own output processing logic
prediction = output.argmax(dim=1)  # Example for classification

# Print or return the prediction
print("Prediction:", prediction)