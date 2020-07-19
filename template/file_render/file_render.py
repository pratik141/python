#!/usr/bin/python

from jinja2 import Template
import getopt
import yaml
import sys

def render_data(filename,datafile, outputfile):
	
	t = open(filename,"r")
	template_data = t.read()
	t.close()
	tdata = Template(template_data)
	
	d = open(datafile,"r")
	data = d.read()
	d.close()
	
	data = yaml.load(data, yaml.SafeLoader)
	odata = tdata.render(data)

	f = open(outputfile, "w")
	f.write(odata)
	f.close()


def main():

	argv     = sys.argv[1:]
	filename = ""
	datafile = ""
	outputfile = ""
	opts, args = getopt.getopt(argv,"h:t:d:o:",["tfile=", "dfile=", "ofile="])
	
	if opts == []:
		print ('file_render -t <template file name> -d <data file name> -o <output file name>')
		sys.exit(2)

	for opt, arg in opts:

	  if opt == '-h':
	     print ('[HELP] file_render  -t <template file name> -d <data file name> -o <output file name>')
	     sys.exit()

	  elif opt in ("-t", "--tfile"):
	     filename = arg

	  elif opt in ("-d", "--dfile"):
	     datafile = arg

	  elif opt in ("-o", "--ofile"):
	     outputfile = arg


	print ('template file is :', filename)
	print ('data file is     :', datafile)
	print ('output file is   :', outputfile)
	render_data(filename, datafile, outputfile)


if __name__ == "__main__":
   main()
