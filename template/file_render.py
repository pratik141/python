#!/usr/bin/python

from jinja2 import Template
import getopt
import yaml
import sys

def dict_merge(dict1, dict2):

	""" merge two dict"""

	return {**dict1, **dict2}


def sanitize(inputstr): 

	""" remove bad strings """
	badstrings = [
	    ';',
	    '$',
	    '&&',
	    '&',
	    '../',
	    '<',
	    '>',
	    '%3C',
	    '%3E',
	    '\'',
	    '--',
	    '1,2',
	    '\x00',
	    '`',
	    '(',
	    ')',
	    'file://',
	    'input://'
	]
	for badstr in badstrings:
	    if badstr in inputstr:
	        inputstr = inputstr.replace(badstr, '')
	return inputstr

def render_data(filename, datafile, outputfile, vardict, separator):

	""" 
		render data to output file 
		inp:
			filename:   input file name (type: str)
			datafile:   data file name (type: str)
			outputfile: output file name (type: str) (optional)
			vardict:    command line vars (type: dict) (optional)
			separator:  separator for command line vars (type: str) (optional)
	"""

	t = open(filename,"r")
	template_data = t.read()
	t.close()
	tdata = Template(template_data)
	if datafile != "":
		d = open(datafile,"r")
		data = d.read()
		d.close()
		data = yaml.load(data, yaml.SafeLoader)
	else:
		data = {}

	odata = tdata.render(dict_merge(data, vardict))

	if outputfile != "":
		f = open(outputfile, "w")
		f.write(odata)
		f.close()
		return "output written in {}".format(outputfile)

	else:
		print("\n******************OUTPUT******************\n")
		return odata

def main():
	"""
		main function to execute

	"""

	argv       = sanitize(sys.argv[1:8])
	filename   = ""
	datafile   = ""
	outputfile = ""
	vardata    = ""
	separator  = ":"
	opts, args = getopt.getopt(argv,"i:d:o:v:s:h",["ifile=", "dfile=", "ofile=","var=", "separator="])
	
	if opts == []:
		print ('[EMPTY ARG] file_render -i <input file name> -d <data file name> -o <output file name>')
		sys.exit(1)

	for opt, arg in opts:
		arg = sanitize(arg)
		if opt == '-h':
			print ('[HELP] file_render -i <input file name> -d <data file name> -o <output file name>')
			sys.exit(1)

		elif opt in ("-i", "--ifile"):
			filename = arg

		elif opt in ("-d", "--dfile"):
			datafile = arg

		elif opt in ("-o", "--ofile"):
			outputfile = arg

		elif opt in ("-v", "--var"):
			vardata = arg

		elif opt in ("-s", "--separator"):
			separator = arg


	print (' input file :', filename)
	print ('  data file :', datafile)
	print ('output file :', outputfile)

	if vardata != "":
		vardict = dict((x.strip(), y.strip())
			for x, y in (element.split(separator)
			for element in vardata.split(',')))
	else:
		vardict = {}
	print(render_data(filename, datafile, outputfile,vardict,separator))

if __name__ == "__main__":
   main()
