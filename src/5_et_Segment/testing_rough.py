
def dice_loss(inputs, targets, smooth=1e-6):
    # Apply softmax to the inputs
    inputs = torch.softmax(inputs, dim=1)

    # Create the one-hot encoding for targets
    targets_one_hot = F.one_hot(targets, num_classes=inputs.shape[1])
    targets_one_hot = targets_one_hot.permute(0, 3, 1, 2).float()

    # Calculate Dice coefficient for each class
    intersection = torch.sum(inputs * targets_one_hot, dim=(2, 3))
    union = torch.sum(inputs, dim=(2, 3)) + torch.sum(targets_one_hot, dim=(2, 3))

    dice_score = (2. * intersection + smooth) / (union + smooth)
    dice_loss = 1 - dice_score.mean()

    return dice_loss

def combined_seg_loss(inputs, targets):
    ce_loss = torch.nn.CrossEntropyLoss()
    ce = ce_loss(inputs, targets)
    dice = dice_loss(inputs, targets)
    return ce + dice


# Function to generate synthetic data
def generate_synthetic_data(batch_size, num_classes, height, width):
    # Generate random predictions
    inputs = torch.rand(batch_size, num_classes, height, width)
    # Generate random target labels
    targets = torch.randint(0, num_classes, (batch_size, height, width))
    return inputs, targets

# Testing the functions
def test_loss_functions():
    # Parameters for synthetic data
    batch_size = 10
    num_classes = 5
    height = 256
    width = 256

    # Generate synthetic data
    inputs, targets = generate_synthetic_data(batch_size, num_classes, height, width)

    # Compute losses
    dice_loss_value = dice_loss(inputs, targets)
    combined_loss_value = combined_seg_loss(inputs, targets)

    print(f"Dice Loss: {dice_loss_value.item()}")
    print(f"Combined Segmentation Loss: {combined_loss_value.item()}")

# Run the test
test_loss_functions()