# /usr/bin/env python

# TODO(John): Correct styling according to Google's Style Guide
# TODO(John): Make this script importable (add a main method)

from subprocess import call
import os  # for changing directory, etc
import time  # for printing current time to console
from helpers import cd # for safley changing directories
from argument_parser import parse_args

# parse and store arguments
arguments = parse_args()
print(arguments.download)

'''
# Variables that need to be changed on each run (START)
# first SRA accension number of the study
first_SRA = 3407206
# number of samples in the study
num_samples = 2
# study directory
study = 'study_1'
# fungal strain
strain = 'yeast'
# set of booleans to chose which part of workflow is ran
downloadSRA = False
trimSRA = True
mapSRA = False
# boolean, true if reads are pair-end
paired_end = True
# parent directory
parent_directory = '/Volumes/Storage/RNASeq_data/' + strain + '/'
# reference genome directory
reference_genome = '/Volumes/Storage/RNASeq_data/reference_genomes/' + strain + '_index'
# (END)

# SRA_files = ['1055985', '1055986', '1055987', '1055988', '1055989', '1055990', '1055991', '1055992', '1055993', '1055994']
'''
#######################################################################

for SRA in arguments.accession:
	# Create string variable SRA, points to SRA accension number
	SRA = "SRR" + str(SRA)
	# 1) download SRA file
	if arguments.download:
		# check if SRA diretory exists, if not create it
		if not os.path.exists(arguments.dir + '/SRA'):
			os.makedirs(arguments.dir + '/SRA')
		# move to newly created directory, download SRA files
		with cd(arguments.dir + '/SRA'):
			print(time.strftime("[%a, %I:%M]"), "Downloading SRA file: " + SRA + " to " + arguments.dir + '/SRA')
			# call fast-q dump using the SRA accension. Pass --split-files if these are pair-end
			if arguments.paired:
				call(["fastq-dump", "--split-files", SRA, "-gzip"])
			else:
				call(["fastq-dump", SRA, "-gzip"])

"""
	# 2) trim file
	if trimSRA:
		with cd(parent_directory+study+"/trimmed_fastq/"):
			# print conformation that moved occured sucsesfully
			print(time.strftime("[%a, %I:%M]"), "Moving to: ", os.getcwd())
			print(time.strftime("[%a, %I:%M]"), "Trimming " + SRA + ".fastq.gz ...")
			# call tim_galore  using the SRA accension. Pass flag if paired.
			if paired_end:
				file_1 = "../fastq/" + SRA + "_1.fastq.gz"
				file_2 = "../fastq/" + SRA + "_2.fastq.gz"
				call(["trim_galore", file_1, file_2, "--paired"])
			else:
				call(["trim_galore", "../fastq/" + SRA + ".fastq.gz"])
			# print DONE message along with current time
			print(time.strftime("[%a, %I:%M]"), "DONE.", SRA + ".fastq.gz", "trimmed")

	# 3) map back to reference genome
	if mapSRA:
		with cd("/Users/johngiorgi/Documents/Google Drive/honours/workflows/tmp/"):
			# print conformation that moved occured sucsesfully
			print(time.strftime("[%a, %I:%M]"), "Moving to: ", os.getcwd())
			print(time.strftime("[%a, %I:%M]"), "Begin mapping " + SRA +
				"_trimmed.fq.gz to reference genome...")
			# map trimmed fast-q back to reference genome
			# IF there is a buffer size error, add:
			# "--limitOutSJcollapsed", "5000000", to this call

			call(["STAR", "--quantMode", "GeneCounts", "--runThreadN", "2", "--genomeDir",
				reference_genome, "--readFilesIn", parent_directory + study + "/trimmed_fastq/" +
				SRA + "_trimmed.fq.gz", "--readFilesCommand", "gunzip", "-c", "--runMode", "alignReads"])

			# rename and move file to correct directory
			call(["mv", "ReadsPerGene.out.tab", "ReadsPerGene_" + SRA + "_trimmed.out.tab"])
			print(time.strftime("[%a, %I:%M]"),
				"Renamed output file 'ReadsPerGene.out.tab' to 'ReadsPerGene_" +
				 SRA + "_trimmed.out.tab'")
			call(["mv", "ReadsPerGene_" + SRA + "_trimmed.out.tab", parent_directory + study + "/RNA_raw_counts/"])
			print(time.strftime("[%a, %I:%M]"), "Moved 'ReadsPerGene_" + SRA +
				"_trimmed.out.tab' to " + parent_directory + study + "/RNA_raw_counts")
			# empty tmp directory
			call(["rm", "-r", "/Users/johngiorgi/Documents/Google Drive/honours/workflows/tmp/"])
			call(["mkdir", "/Users/johngiorgi/Documents/Google Drive/honours/workflows/tmp/"])

# empty ncbi > public > sra directory
print(time.strftime("[%a, %I:%M]"), "Emptying /Users/johngiorgi/ncbi/public/sra")
call(["rm", "-r", "/Users/johngiorgi/ncbi/public/sra"])
call(["mkdir", "/Users/johngiorgi/ncbi/public/sra"])
"""
