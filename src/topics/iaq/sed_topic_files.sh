#!/bin/sh

for f in 'gases.csv particulates.csv status.csv climate.csv'; do
    sed -i 's/birmingham-ac/oxford-ac/g' $f
done
