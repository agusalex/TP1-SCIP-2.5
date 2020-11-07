set I := 1..10 ;
do print I;
do print " Cardinality of I:", card(I);
do forall <i> in I with i > 5 do print sqrt(i);
