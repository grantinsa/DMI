#!/bin/bash
#9.piemērs - operācijas ar mainīgajiem
a=56
b=32
val31=`expr $a + $b`
echo "$a + $b = "$val31

val32=`expr $a - $b`
echo "$a - $b = "$val32

val33=`expr $a \* $b`
echo "$a * $b = "$val33

val34=`expr $a / $b`
echo "$a / $b = "$val34

val35=`expr $a % $b`
echo "$a % $b = "$val35



#8.piemērs - operācijas ar konstantēm
: <<'END'
val21=`expr 2 + 3`
echo "2 + 3 = "$val21

val22=`expr 2 - 3`
echo "2 - 3 = "$val22

val23=`expr 2 \* 3`
echo "2 * 3 = "$val23

val24=`expr 2 / 3`
echo "2 / 3 = "$val24

val25=`expr 2 % 3`
echo "2 % 3 = "$val25
END


: <<'END'# komentāra bloka sākums
#7.piemeers
skaitliskaa_vertiba='expr 2 + 2'
echo "Summas vertiba: "$skaitliskaa_vertiba
echo "Summas vertiba: $skaitliskaa_vertiba"
skaitliskaa_vertiba=`expr 2 + 2`
echo "Summas vertiba: $skaitliskaa_vertiba"
echo "Summas vertiba: "$skaitliskaa_vertiba
skaitliskaa_vertiba=exrp 2 + 2
echo "Summas vertiba: $skaitliskaa_vertiba
echo "Summas vertiba: $skaitliskaa_vertiba"
END # komentāra bloka beigas

#6.piemeers
#echo $*
#echo "-------------"
#kartas_numurs=1
#for arguments in $*
#do
#    echo $kartas_numurs". arguments - "$arguments
#    kartas_numurs=$kartas_numurs+1
#done

#5.piemeers
#echo "Skriptam nodoto argumentu skaits: " $#
#echo "Argumentu saraksts (attelosanas veids 1): "$*
#echo "Argumentu saraksts (attelosanas veids 2): "$@
#echo "Pirma argumenta vertiba: "$1
#echo "Otra argumenta vertiba: "$2
#echo $1$2

#4.piemeers
#echo "Izpildama skripta faila nosaukums" $0
##echo $n
#echo "Skriptam nodoto argumentu skaits: " $#
#echo "Argumentu saraksts (attelosanas veids 1): "$*
#echo "Argumentu saraksts (attelosanas veids 2): "$@
#ech "Ieprieksejas komandas izpildes rezultats: "$?
#echo "Ieprieksejas komandas izpildes rezultats: "$?
#echo "Skripta izpildei pieskirtais procesa numurs: "$$
##echo ""$!

#3. piemeers
#NAME="Vards Uzvards"
#echo $NAME
#unset NAME
#echo $NAME

#2. piemeers
#NAME="Vards Uzvards"
#readonly NAME
#echo $NAME
#NAME="Uzvards Vards"
#echo $NAME

#1. piemeers
#NAME="Vards Uzvards"
#echo $NAME

#0. piemeers
#history > history_20170927.txt

