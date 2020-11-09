set Blanco := {<0,2>,< 4,2>} ;
set Negro := {<1,1>,<3,2>};
var a real ;
var b real ;
var c real ;
var o real ;
subto restricB: forall <i,j> in Blanco: j >= a*(i*i) + b*i + c  + o;
subto restricA: forall <i,j> in Negro: j <= a*(i*i) + b*i + c - o;
maximize objetivo: o;

