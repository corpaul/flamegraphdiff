#!/bin/bash -xe

# preprocess stuff
python graphs/preprocess.py test/reportOld IO
python graphs/preprocess.py test/reportNew IO

# generate diff
python graphs/diff_flame_graphs.py test/reportOld_rewr test/reportNew_rewr output/reports_diff.txt

# generate svgs
graphs/flamegraph/flamegraph.pl test/reportOld_rewr --cp > output/reportsOld.svg
graphs/flamegraph/flamegraph.pl test/reportNew_rewr --cp > output/reportsNew.svg
graphs/flamegraph/flamegraph.pl output/reports_diff.txt --cp > output/reports_diff.svg