import torch
import torch.nn as nn
from models.sequence.lstm_model import LSTMModel
from models.utils import dict_to_vector


def build_sequences(X, sequence_length=5):
    sequences = []
    labels = []

    data = X.values

    for i in range(len(data) - sequence_length):
        seq = data[i:i+sequence_length]
        label = 0  # dummy label (can improve later)

        sequences.append(seq)
        labels.append(label)

    return torch.tensor(sequences, dtype=torch.float32), torch.tensor(labels, dtype=torch.float32)


def train_sequence_model(X):
    model = LSTMModel(input_size=X.shape[1])

    sequences, labels = build_sequences(X)

    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    model.train()

    for epoch in range(3):  # keep small
        optimizer.zero_grad()

        outputs = model(sequences)
        loss = criterion(outputs.squeeze(), labels)

        loss.backward()
        optimizer.step()

        print(f"Epoch {epoch+1}, Loss: {loss.item()}")

    return model