#!/bin/bash -xe

sed -e "s~  ~ ~g" $1 > $1.tmp && mv $1.tmp $1
sed -e "s~ ;~?;~g" $1 > $1.tmp && mv $1.tmp $1
sed -e "s~, ~,~g" $1 > $1.tmp && mv $1.tmp $1
