"""
Main training pipeline.

Flow:
Load → Preprocess → Train → Validate → Log
"""

from data_loader.loader import DataLoader
from preprocessing.preprocess import preprocess
from training_jobs.train_supervised import train_supervised
from training_jobs.train_anomaly import train_anomaly
from validation.validate import validate_model
from experiment_runner.runner import ExperimentRunner


def run_training_pipeline():
    loader = DataLoader()
    runner = ExperimentRunner()

    # Load data
    df = loader.load_data()

    # Preprocess
    X, y = preprocess(df)

    # Train supervised model
    sup_model = train_supervised(X, y)

    # Validate
    metrics = validate_model(sup_model, X, y)
    runner.log("SupervisedModel", metrics)

    # Train anomaly model
    anomaly_model = train_anomaly(X)
    print("Anomaly model trained")

    print("Training pipeline completed successfully")


if __name__ == "__main__":
    run_training_pipeline()


# after graph and seq

from training_jobs.train_sequence import train_sequence_model
from training_jobs.train_graph import train_graph_model

def run_training_pipeline():
    loader = DataLoader()
    runner = ExperimentRunner()

    df = loader.load_data()

    X, y = preprocess(df)

    # Supervised
    sup_model = train_supervised(X, y)
    metrics = validate_model(sup_model, X, y)
    runner.log("SupervisedModel", metrics)

    # Anomaly
    anomaly_model = train_anomaly(X)
    print("Anomaly model trained")

    # Sequence
    seq_model = train_sequence_model(X)
    print("Sequence model trained")

    # Graph
    graph_model = train_graph_model(df)
    print("Graph model ready")

    print("Training pipeline completed")


# for model Registry


from model_registry.model_registry_manager import ModelRegistryManager

registry = ModelRegistryManager()

# After training supervised model
version, path = registry.register_model(
    "supervised_model",
    sup_model,
    metrics
)

# Register anomaly model
registry.register_model("anomaly_model", anomaly_model)

# Sequence model
registry.register_model("sequence_model", seq_model)

# Graph model (dict-based)
registry.register_model("graph_model", graph_model)