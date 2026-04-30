import torch
from models.utils import dict_to_vector
from .lstm_model import LSTMModel

class SequenceModel:
    def __init__(self):
        self.model = LSTMModel()
        self.model.eval()

    def predict(self, sequence: list):
        """
        sequence: list of feature dicts
        """

        vectors = [dict_to_vector(f) for f in sequence]

        tensor = torch.tensor(vectors, dtype=torch.float32).unsqueeze(0)

        with torch.no_grad():
            output = self.model(tensor)

        return float(output.item())