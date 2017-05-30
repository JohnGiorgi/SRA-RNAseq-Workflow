# /usr/bin/env python
import argparse

# TODO(John): Go over argparse doc, ensure I am using it to its full potential

def parse_args():
    '''
    This method creates an ArgumentParser object, creates and defines all
    arguments to be used by SRA_rnaseq_workflow.py, and returns all captured
    arguments as an argparse object.
    '''

    ## create parser
    parser = argparse.ArgumentParser(description='''Run a workflow which includes
    downloading multiple SRA files, trimming them, and mapping them to a reference
    genome. Example usage: FINISH''')

    ## add arguments
    # accession
    parser.add_argument('--accession', metavar = '<accession number>', type = int, \
    nargs='+', help = '''Enter a single accesion number or a list of accession
    numbers''')
    # paired- or single-end reads
    parser.add_argument('--paired', action = 'store_true', help = '''Changes
    workflow for paired end reads. Default value is False''', default = False)
    # download or local
    parser.add_argument('--download', action = 'store_true', help = '''Downloads
    all SRA files passed by the --accession argument. Default action is to look
    for them in a folder called "SRA" in --dir''', default = False)
    # to trim or not to trim...
    parser.add_argument('--trim', action = 'store_true', help = '''Calls
    trim_galore to preform adaptor timming and quality assurance of all SRA
    files passed by the --accession argument''', default = False)
    # directory
    parser.add_argument('--dir', metavar = '<directory>', type = str, \
    help = '''The directory where SRA files are downloaded or where they are
    looked for (this depends on whether or not you pass the --download flag).
    Other directories are also created here''')
    # reference genome
    parser.add_argument('--genome', metavar = '<reference genome>', type = str,\
    help = '''Directory to the reference genome''')

    ## parse arguments
    arguments = parser.parse_args()

    return arguments
