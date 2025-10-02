import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    text = "My name is Bond."
    start = 11
    end = 15

    result = sample_run_anonymizer(text, start, end)

    assert result["start"] == start
    assert result["end"] == end
    assert result["original_length"] == len(text)
    assert result["anonymized"] == "My name is ****."
    pass