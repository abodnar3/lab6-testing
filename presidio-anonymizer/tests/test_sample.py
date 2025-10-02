import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    text = "My name is Bond."
    start = 11
    end = 15

    result = sample_run_anonymizer(text, start, end)

    assert start in result
    assert end in result
    assert text in result
    pass