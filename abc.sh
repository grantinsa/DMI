#!/bin/bash
if [ $# -eq 0 ]
then
    echo "Ievadi skaitļus"
    exit
fi
> temp
for i in $*
do
echo "$i" >> temp
done
echo "Sakārtotie skaitļi:"
sort -n temp




: <<'END'
a=$1
b=$2
c=$3
echo "$a $b $c"
echo "$a $c $b"
echo "$b $a $c"
echo "$c $a $b"
echo "$c $b $a"
END
