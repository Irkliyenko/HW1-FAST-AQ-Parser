from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    fasta_f = "data/test.fa"
    fastq_f = "data/test.fq"

    # Create instance of FastaParser

    fasta = FastaParser(fasta_f)

    # Create instance of FastqParser

    fastq = FastqParser(fastq_f)   

    # Iterate through each record in the FASTA file
    # Transcribe and reverse transcribe the sequence, then print the results

    for record in fasta:
        print(f"Transcribed FASTA: {transcribe(record[1])}")
        print(f"Reverse transcribed FASTA: {reverse_transcribe(record[1])}")
       
    # Iterate through each record in the FASTQ file
    # Transcribe and reverse transcribe the sequence, then print the results
    
    for record in fastq:
        print(f"Transcribed FASTQ: {transcribe(record[1])}")
        print(f"Reverse transcribed FASTQ: {reverse_transcribe(record[1])}")


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
