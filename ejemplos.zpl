set Blanco := {<1,2>,< 2,2>} ;
set Negro := {<2,1>,<1,1>};
var a integer ;
var o integer ;
var b integer ;
maximize objetivo: o + b ;
do forall <i,j> in Blanco do print i ;
subto restricB: forall <i,j> in Blanco: j >= a*i + b + o;
subto restricA: forall <i,j> in Negro: j <= a*i + b - o;

#do print Blanco ;