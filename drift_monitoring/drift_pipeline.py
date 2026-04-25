"""
End-to-end drift monitoring pipeline.
"""

from data_drift.data_drift import DataDriftDetector
from concept_drift.concept_drift import ConceptDriftDetector
from prediction_drift.prediction_drift import PredictionDriftDetector
from reporting.report_generator import DriftReportGenerator


class DriftPipeline:
    def __init__(self):
        self.data_detector = DataDriftDetector()
        self.concept_detector = ConceptDriftDetector()
        self.pred_detector = PredictionDriftDetector()
        self.reporter = DriftReportGenerator()

    def run(self, ref_data, curr_data, old_metrics, new_metrics, old_preds, new_preds):
        data_drift = self.data_detector.detect(ref_data, curr_data)
        concept_drift = self.concept_detector.detect(old_metrics, new_metrics)
        pred_drift = self.pred_detector.detect(old_preds, new_preds)

        report = self.reporter.generate(
            data_drift,
            concept_drift,
            pred_drift
        )

        return report