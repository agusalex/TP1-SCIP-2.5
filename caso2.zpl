set Blanco := { read "input_B.txt" as "<1n,2n>" };
set Negro := { read "input_N.txt" as "<1n,2n>" };
var a real ;
var b real ;
var o real ;
maximize objetivo: o ;
subto restricB: forall <i,j> in Blanco: j >= a*i +b + o;
subto restricN: forall <i,j> in Negro: j <= a*i + b - o;


