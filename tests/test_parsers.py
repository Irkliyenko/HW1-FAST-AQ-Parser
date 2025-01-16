# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest 


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements 


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa.
    """
    # Edge cases like bad.fa and blank.fa are handled by class code itself by raising the ValueError File (file.fa) had 0 lines.

    # Test using a valid FASTA file

    test_f = "data/test.fa"

    parser_t = FastaParser(test_f)
    
    
    # Test that the parser correctly reads the valid FASTA file

    seqs = [record for record in parser_t]
    seq0 = 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    assert seqs[0][1] == seq0, "FastaParser doesn't work on valid file"
     
 

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    test_fa = "data/test.fa"
    parser = FastaParser(test_fa)

    # Check if each record in the FASTA file is valid

    for record in parser:
        assert record[0][1] is not None, "Not a valid FASTA file"
        assert len(record) == 2, "Not a valid FASTAQ file"


    

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    test_fq = "data/test.fq"
    parser = FastqParser(test_fq )
    
    # Test on correct FASTQ file

    seqs = [record for record in parser]
    seq0 = 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    assert seqs[0][1] == seq0, "FastqParser doesn't work on valid file"


def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Test using a valid FASTQ file

    test_f = "data/test.fa"
    parser = FastqParser(test_f)

    # Test that the parser correctly reads the valid FASTQ file

    for record in parser:
        assert len(record) == 3, "Not a valid FASTAQ file"