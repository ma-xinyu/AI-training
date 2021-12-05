import torch
from torchvision.datasets import MNIST
from torchvision.transforms import Compose, ToTensor
from torch.utils.data import DataLoader

def load_mnist(batch_size=1000):
    train_data = MNIST(root="data", train=True, transform=Compose([ToTensor()]))
    valid_data = MNIST(root="data", train=False, transform=Compose([ToTensor()]))

    train_loader = DataLoader(train_data, shuffle=True, batch_size=batch_size)
    valid_loader = DataLoader(valid_data, shuffle=True, batch_size=batch_size)
    return train_loader, valid_loader

