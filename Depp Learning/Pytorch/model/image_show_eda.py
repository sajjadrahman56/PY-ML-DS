import json
import matplotlib.pyplot as plt
import os
from PIL import Image

# Load the metadata
metadata = []
with open('/content/data/metadata.jsonl', 'r') as f:
    for line in f:
        metadata.append(json.loads(line))

# Count the number of each masking level
masking_counts = {'Low masking level': 0, 'Medium masking level': 0, 'High masking level': 0}
for data in metadata:
    masking_counts[data['text_prompt']] += 1

# Plot the counts
plt.bar(masking_counts.keys(), masking_counts.values())
plt.title('Masking Level Counts')
plt.xlabel('Masking Level')
plt.ylabel('Count')
plt.show()


# Display some images from each masking level
for level in ['Low masking level', 'Medium masking level', 'High masking level']:
    img_name = next(data['file_name'] for data in metadata if data['text_prompt'] == level)
    img_path = os.path.join('/content/data/', img_name)
    img = Image.open(img_path).convert('L')  # Convert image to grayscale
    plt.imshow(img, cmap='gray')  # Display image in grayscale
    plt.title(f'Example of {level}')
    plt.show()

