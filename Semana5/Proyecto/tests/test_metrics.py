import numpy as np

from src.metrics import compute_similarity_matrix, summarize_multi_target_ranking, confusion_from_predictions

def test_compute_similarity_matrix_shape_and_values():
    a = np.array([[1.0, 0.0], [0.0, 1.0]], dtype=np.float32)
    b = np.array([[1.0, 0.0], [1.0, 1.0]], dtype=np.float32)
    sim = compute_similarity_matrix(a, b)
    assert sim.shape == (2, 2)
    assert np.allclose(sim, np.array([[1.0, 1.0], [0.0, 1.0]], dtype=np.float32))

def test_summarize_multi_target_ranking_perfect_recall():
    sim = np.array([[0.9, 0.1, 0.2], [0.1, 0.8, 0.2], [0.1, 0.2, 0.7]], dtype=np.float32)
    positives = {0: [0], 1: [1], 2: [2]}
    metrics = summarize_multi_target_ranking(sim, positives)
    assert metrics["R@1"] == 1.0
    assert metrics["MRR"] == 1.0
    assert metrics["MedianRank"] == 1.0

def test_summarize_multi_target_ranking_multiple_positives():
    sim = np.array([[0.2, 0.8, 0.7]], dtype=np.float32)
    positives = {0: [0, 2]}
    metrics = summarize_multi_target_ranking(sim, positives)
    assert metrics["Ranks"] == [2]
    assert metrics["R@1"] == 0.0
    assert metrics["R@5"] == 1.0

def test_confusion_from_predictions_counts():
    conf = confusion_from_predictions(["cat", "cat", "dog"], ["cat", "dog", "dog"])
    assert conf.loc["cat", "cat"] == 1
    assert conf.loc["cat", "dog"] == 1
    assert conf.loc["dog", "dog"] == 1
