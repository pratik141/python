#!/usr/bin/python

from jinja2 import Template
import getopt
import yaml
import sys

def Merge(dict1, dict2):
    return {**dict1, **dict2}


def render_data(filename,datafile, outputfile,vardict,separator):

	t = open(filename,"r")
	template_data = t.read()
	t.close()
	tdata = Template(template_data)

	d = open(datafile,"r")
	data = d.read()
	d.close()
	
	data = yaml.load(data, yaml.SafeLoader)
	odata = tdata.render(Merge(data, vardict))

	if outputfile != "":
		f = open(outputfile, "w")
		f.write(odata)
		f.close()

	else:
		print("\n******************OUTPUT******************\n")
		print(odata)

def main():

	argv       = sys.argv[1:]
	filename   = ""
	datafile   = ""
	outputfile = ""
	vardata    = ""
	separator  = ":"
	opts, args = getopt.getopt(argv,"i:d:o:v:s:h",["ifile=", "dfile=", "ofile=","var=", "separator="])
	
	if opts == []:
		print ('file_render -i <template file name> -d <data file name> -o <output file name>')
		sys.exit(2)

	for opt, arg in opts:
	  if opt == '-h':
	    print ('[HELP] file_render  -i <template file name> -d <data file name> -o <output file name>')
	    sys.exit()

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
	render_data(filename, datafile, outputfile,vardict,separator)

if __name__ == "__main__":
   main()
