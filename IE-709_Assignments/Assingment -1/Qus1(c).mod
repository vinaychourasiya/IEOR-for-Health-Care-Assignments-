
param T{1..85,1..40}; # Travelling time Matrix
param P{1..85};

var x{j in 1..40 } binary >=0;
var u{i in 1..85} binary >=0;
var y{i in 1..85} binary >=0;

#---------------------------------------model objective

maximize z:sum{j in 1..85} P[j]*u[j];

#---------------------------------------model constraints	

subject to  con1{i in 1..85}:sum{j in 1..40} (T[i,j]*x[j])-u[i] >=1;

subject to con2: sum{k in 1..40} x[k]==3;
 

