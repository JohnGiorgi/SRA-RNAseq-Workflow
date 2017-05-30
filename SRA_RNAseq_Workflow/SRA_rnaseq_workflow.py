# /usr/bin/env python

# TODO(John): Correct styling according to Google's Style Guide
# TODO(John): Make this script importable (add a main method)
# TODO(John): Figure out how to end script the correct way

from subprocess import call
import os
import time
from helpers import cd
from argument_parser import parse_args

# parse and store arguments
arguments = parse_args()

def download_sra():
	# check if SRA directory exists, if not create it
	if not os.path.exists(arguments.dir + '/SRA'):
		print(time.strftime('[%a, %I:%M]'), 'Creating directory /SRA..')
		os.makedirs(arguments.dir + '/SRA')
	# move to newly created directory, download SRA files
	with cd(arguments.dir + '/SRA'):
		print(time.strftime("[%a, %I:%M]"), "Downloading SRA file: " + SRA\
		 + " to " + arguments.dir + '/SRA')
		# call fastq-dump using the SRA accension.
		if arguments.paired:
			call(["fastq-dump", "--split-files", SRA, "-gzip", ">",\
			"../log/fastq_dump_log_{}.txt".\
			format(time.strftime("[%a:%I:%M]"))])
		else:
			call(["fastq-dump", SRA, "-gzip", ">",\
			"../log/fastq_dump_log_{}.txt".\
			format(time.strftime("[%a:%I:%M]"))])
def trim_sra():
	# check for SRA folder and file existance
	if not os.path.exists(arguments.dir + '/SRA'):
		print('''There is no directory /SRA in {dir}. Either create this
		directory in {dir} or use the --download flag to create the directory
		and download SRA files to it'''.format(dir = arguments.dir))
	if not os.path.exists(os.path.exists(arguments.dir + '/SRA/' + SRA)):
		print("There is no file {file} in {dir}".\
		format(file = SRA, dir = arguments.dir))ß
	# check if SRA_trimmed directory exists, if not create it
	if not os.path.exists(arguments.dir + '/SRA_trimmed'):
		print(time.strftime('[%a, %I:%M]'), 'Creating directory /SRA_trimmed..')
		os.makedirs(arguments.dir + '/SRA_trimmed')

	with cd(arguments.dir + '/SRA_trimmed/'):
		print(time.strftime("[%a, %I:%M]"), "Trimming " + SRA + ".fastq.gz ...")
		# call tim_galore  using the SRA accension. Pass flag if paired.
		if arguments.paired:
			file_1 = arguments.dir + '/SRA/' + SRA + "_1.fastq.gz"
			file_1 = arguments.dir + '/SRA/' + SRA + "_2.fastq.gz"
			call(["trim_galore", file_1, file_2, "--paired", ">",\
			"../log/trim_galore_output_{}.txt".\
				format(time.strftime("[%a:%I:%M]"))])
		else:
			call(["trim_galore", arguments.dir + '/SRA/' + SRA + \
			".fastq.gz", ">", "../log/trim_galore_output_{}.txt".\
			format(time.strftime("[%a:%I:%M]"))])
def map_sra():
	pass

for SRA in arguments.accession:
	# Create string variable SRA, points to SRA accension number
	SRA = "SRR" + str(SRA)
	# 1) download SRA file
	if arguments.download: download_sra()
	# 2) trim file
	if arguments.trim: trim_sra()
	# 3) map sra file to reference genome

	"""
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
