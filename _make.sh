#!/bin/sh -e
# Build the website in _site/, filling templates.

# Recreate the _site directory with no warning.
mkdir -p _site
rm -rf _site/*

# Copy all files into _site except hidden files and directories and those files
# and directories with leading or trailing underscores.
rsync -a --exclude=/_* --exclude=/.* --exclude=*_ --exclude=_* * _site

# Process all templates (files named with trailing underscores). The real name
# of the generated file is the template name without the trailing underscore.
for file in $(find . -name '*_' -type f); do
	mkdir -p _site/${file%/*}
	output=_site/${file%_}
	if test -x $file; then
		$file $output
	else
		./_splice.py $file >$output
	fi
done
