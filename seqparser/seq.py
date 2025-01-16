# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """

    # Generate RNA sequence by replacing each base using the mapping
    rna_seq = "".join(TRANSCRIPTION_MAPPING.get(base, base) for base in seq)
    return rna_seq


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!

    # Transcribe the sequence and reverse the result
    rev_seq = transcribe(seq)[::-1]
    return rev_seq
    


