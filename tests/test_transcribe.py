# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    test_seq = {"ATGC":"UACG",
                "GCGA":"CGCU",
                "AAAA":"UUUU"}
    
    for dna,rna in test_seq.items():

        rna_seq = transcribe(dna)
        assert rna_seq == rna, f"transcribe func doesn't work"
    


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    test_seq = {"ATGC":"GCAU",
                "GCGA":"UCGC",
                "AAAA":"UUUU"}
    
    for dna,rna in test_seq.items():

        rna_seq = reverse_transcribe(dna)
        assert rna_seq == rna, f"reverse_transcribe func doesn't work"
        