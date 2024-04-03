# 1.1
a) X i Y są bratami lub siostrami <br>
b) X i Y są kuzynami <br>
c) X i Y są swatami <br>
d) Y jest pradziadkiem X <br>
e) X i Y są bratami przyrodnimi <br>
f) Y jest prapradziadkiem X <br>
g) X jest dziadkiem lub pradziadkiem Y ?

# 1.2 
nieprzyjazn(X,Y) :- \+lubi(X,Y) , \+lubi(Y,X).<br>
niby_przyjazn(X,Y) :- lubi(X,Y) ; lubi(Y,X).<br>
loves(X,Y) :- lubi(X,Y) , (   (mezczyzna(X) , \+mezczyzna(Y)) ; (mezczyzna(Y) , \+mezczyzna(X))).<br>
true_love(X,Y) :- loves(X,Y) , loves(Y,X).
