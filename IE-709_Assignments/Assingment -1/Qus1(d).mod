
param T{1..85,1..40}; # Travelling time Matrix
param P{1..85};

var x{j in 1..40 } binary >=0; 
var y{i in 1..85} integer >=0;

#---------------------------------------model objective

maximize z:sum{i in 1..85} P[i]*y[i];

#---------------------------------------model constraints	


subject to  con1{i in 1..85}:sum{j in 1..40} (T[i,j]*x[j]) >=y[i];

# Bound of max No. of ambulance availble
subject to con2: sum{k in 1..40} x[k]==8;

# for satisfy each node demand 
subject to con3{n in 1..85}: y[n]>=1


 

