#!/bin/bash -xe

EXPECTED_ARGS=3
if [ $# -ne $EXPECTED_ARGS ]
then
	echo "Usage: `basename $0` v1.svg v2.svg diff.svg"
	exit 65
fi

cp graphs/dfg_template.html output/dfg.html
sed -i "s/%V1FILE%/$1/g" output/dfg.html 
sed -i "s/%V2FILE%/$2/g" output/dfg.html 
sed -i "s/%DIFFFILE%/$3/g" output/dfg.html 
