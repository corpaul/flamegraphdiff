#!/bin/bash -xe

FlameGraph/difffolded.pl demos/rsync/rsync_v2.txt demos/rsync/rsync_v1.txt | FlameGraph/flamegraph.pl > demos/rsync/rsync_dfg1.svg 
FlameGraph/difffolded.pl demos/rsync/rsync_v1.txt demos/rsync/rsync_v2.txt | FlameGraph/flamegraph.pl > demos/rsync/rsync_dfg2.svg 
FlameGraph/difffolded.pl -d demos/rsync/rsync_v1.txt demos/rsync/rsync_v2.txt | FlameGraph/flamegraph.pl > demos/rsync/rsync_dfg_diff.svg 

graphs/generate_dfg_report.sh rsync_dfg1.svg rsync_dfg2.svg rsync_dfg_diff.svg demos/rsync/
