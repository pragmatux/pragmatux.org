#!/usr/bin/env python
# usage: splice TEMPLATE
#
# Read TEMPLATE, replace lines with {{ scheme:filepath }}. See _README.

import sys, re, os, subprocess

def normalize_path(path):
	if path[0] == '/':
		path = path[1:]
	else:
		base = os.path.dirname(template_name)
		path = os.path.join(base, path)
	return path

def scheme_asciidoc(path):
	cmd = ["asciidoc", "--backend=xhtml11", "--conf-file=_asciidoc.conf",
	       "--out-file=-", normalize_path(path)]
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = p.communicate()
	return out.replace("\r\n", "\n")

def scheme_include(path):
	return file(normalize_path(path)).read()

def expand(scheme, path):
	if scheme == "include":
		return scheme_include(path)
	if scheme == "asciidoc":
		return scheme_asciidoc(path)
	else:
		raise Exception("Unknown scheme " + scheme)

def main(text):
	ex = re.compile(r"\{\{ (\w+):([/\w\-\.]+) \}\}")
	for line in text:
		match = ex.search(line)
		if match is not None:
			print expand(match.group(1), match.group(2)),
		else:
			print line,

if __name__ == "__main__":
	template_name = sys.argv[1]
	main(open(template_name).readlines())
