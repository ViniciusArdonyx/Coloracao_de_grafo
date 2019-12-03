#!/bin/bash
a=1
b=1
# a heuristicas
for i in $(seq $a);
do
	#echo $i
	# Executa as a heuristicas b vezes
	for j in $(seq $b);
	do
		#echo "\t" $j
		#python3 main.py ./Instâncias/myciel5.col 9 $i
		python3 ./../Codigo/main.py ./../Instâncias/myciel6.col 95 3 -m
	done
done