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
    
    # Test cases: DNA sequence as key, expected RNA sequence as value

    test_seq = {"ATGC":"UACG",
                "GCGA":"CGCU",
                "AAAA":"UUUU"}
    
    # Iterate over each test case and validate the transcription

    for dna,rna in test_seq.items():
        rna_seq = transcribe(dna)
        assert rna_seq == rna, f"transcribe function doesn't work"
    


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # Test cases: DNA sequence as key, expected reversed RNA sequence as value

    test_seq = {"ATGC":"GCAU",
                "GCGA":"UCGC",
                "AAAA":"UUUU"}
    
    # Iterate over each test case and validate the reverse transcription

    for dna,rna in test_seq.items():
        rna_seq = reverse_transcribe(dna)
        assert rna_seq == rna, f"reverse_transcribe function doesn't work"
        