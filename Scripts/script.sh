#!/bin/bash
a=100
for i in $(seq $a);
do
	python3 ./../Codigo/main.py ./../Instâncias/fpsol2.i.1/fpsol2.i.1.col 496 2 -m
	python3 ./../Codigo/main.py ./../Instâncias/inithx.i.3/inithx.i.3.col 621 2 -m
	python3 ./../Codigo/main.py ./../Instâncias/le450_5a/le450_5a.col 450 2 -m
	python3 ./../Codigo/main.py ./../Instâncias/le450_25d/le450_25d.col 450 2 -m
	python3 ./../Codigo/main.py ./../Instâncias/miles250/miles250.col 128 2 -m
	python3 ./../Codigo/main.py ./../Instâncias/miles1500/miles1500.col 128 2 -m
	python3 ./../Codigo/main.py ./../Instâncias/myciel3/myciel3.col 11 2 -m
	python3 ./../Codigo/main.py ./../Instâncias/queen5_5/queen5_5.col 25 2 -m
done

b=10
for i in $(seq $b);
do
	python3 ./../Codigo/main.py ./../Instâncias/inithx.i.1/inithx.i.1.col 864 2 -m
	python3 ./../Codigo/main.py ./../Instâncias/qg.order60/qg.order60.col 3600 2 -m
done