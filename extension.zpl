set Blanco := { read "input_B.txt" as "<1n,2n>" };
set Negro := { read "input_N.txt" as "<1n,2n>" };
var a real ;
var b real ;
var c real ;
var o real ;
maximize objetivo: o;
subto restricB: forall <i,j> in Blanco: j >= a*(i*i) + b*i + c  + o;
subto restricA: forall <i,j> in Negro: j <= a*(i*i) + b*i + c - o;


