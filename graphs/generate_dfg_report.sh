#!/bin/bash -xe

EXPECTED_ARGS=4
if [ $# -ne $EXPECTED_ARGS ]
then
	echo "Usage: `basename $0` v1.svg v2.svg diff.svg outputdir"
	echo "Note: the svg files should be in the same directory as the generated dfg-set.html file."
	exit 65
fi

OUTPUTDIR=$4

IFLAG="-i" && [[ "$(uname)" == "Darwin" ]] && IFLAG="-i ''"

cp graphs/dfg_template.html $OUTPUTDIR/dfg-set.html
sed ${IFLAG} "s|%V1FILE%|$1|g" $OUTPUTDIR/dfg-set.html
sed ${IFLAG} "s|%V2FILE%|$2|g" $OUTPUTDIR/dfg-set.html
sed ${IFLAG} "s|%DIFFFILE%|$3|g" $OUTPUTDIR/dfg-set.html
