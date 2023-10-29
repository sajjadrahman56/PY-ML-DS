import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import jsonlines
import os

# Define your custom dataset
class MammogramDataset(Dataset):
    def __init__(self, jsonl_file, img_dir, transform=None):
        self.metadata = [data for data in jsonlines.open(jsonl_file)]
        self.img_dir = img_dir
        self.transform = transform

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, idx):
        img_name = os.path.join(self.img_dir, self.metadata[idx]['image_name'])
        image = Image.open(img_name)
        label = self.metadata[idx]['masking_level']
        if self.transform:
            image = self.transform(image)
        return image, label

# Define your model architecture
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 3) # Assuming 3 classes: low, medium and high

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Define transformations
transformations = transforms.Compose([
    transforms.Resize((32,32)),
    transforms.ToTensor(),
])

# Initialize dataset and dataloader
dataset = MammogramDataset('metadata.jsonl', 'images/', transformations)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

# Initialize model, loss function and optimizer
model = SimpleCNN()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

# Training loop
for epoch in range(10): 
    for i, data in enumerate(dataloader):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = model(inputs)
        
        # Calculate loss
        loss = criterion(outputs, labels)
        
        # Backpropagation and optimization
        loss.backward()
        optimizer.step()

# Function to calculate accuracy
def calculate_accuracy(dataloader):
    correct_predictions = 0
    total_predictions = 0

    # Set model to evaluation mode
    model.eval()

    with torch.no_grad():
        for data in dataloader:
            images, labels = data
            
            # Forward pass
            outputs = model(images)
            
            # Get predictions from the maximum value
            _, predicted = torch.max(outputs.data, 1)

            total_predictions += labels.size(0)
            
            # Total correct predictions
            correct_predictions += (predicted == labels).sum().item()

    return (correct_predictions / total_predictions) * 100

accuracy = calculate_accuracy(dataloader)
print(f'Accuracy of the model: {accuracy}%')
