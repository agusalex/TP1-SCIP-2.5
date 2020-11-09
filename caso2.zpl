set Blanco := {<2,4>,< 3,5>} ;
set Negro := {<3,1>};
var a real ;
var b real ;
var o real ;
maximize objetivo: o;
do forall <i,j> in Blanco do print i ;
subto restricB: forall <i,j> in Blanco: j >= a*i + b + o;
subto restricA: forall <x,y> in Negro: y <= a*x + b - o;


#do print Blanco ;