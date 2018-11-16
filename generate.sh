#!/usr/bin/env bash

function usage() {
    die "Generate an HTML page of differences between two folded stacks (rendered as flame graphs)

    Usage: $0 <left_stacks> <right_stacks> <output_dir>

       eg: $0 demos/rsync/rsync_v1.txt demos/rsync/rsync_v2.txt demos/rsync"
}

function die() {
    local exit_status="$?"
    set +x
    [ "$exit_status" -eq "0" ] && exit_status=1
    local msg="$1"
    >&2 echo -e "$msg"
    exit "${exit_status}"
}

trap 'die "Unhandled error on or near line ${LINENO}"' ERR

left=$1
right=$2
output_dir=$3

[ -z "$left" ] || [ -z "$right" ] || [ -z "$output_dir" ] && usage

set -x

FlameGraph/difffolded.pl $2 $1 | FlameGraph/flamegraph.pl > $3/dfg1.svg
FlameGraph/difffolded.pl $1 $2 | FlameGraph/flamegraph.pl > $3/dfg2.svg
FlameGraph/difffolded.pl -d $1 $2 | FlameGraph/flamegraph.pl > $3/dfg_diff.svg

graphs/generate_dfg_report.sh dfg1.svg dfg2.svg $3/dfg_diff.svg $3
