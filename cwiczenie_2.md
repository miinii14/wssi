kobieta(X) :- osoba(X) , \+mezczyzna(X).<br>
ojciec(X,Y) :- osoba(X) , osoba(Y) , rodzic(X,Y) , mezczyzna(X).<br>
matka(X,Y) :- osoba(X) , osoba(Y) , rodzic(X,Y) , kobieta(X).<br>
corka(X,Y) :- osoba(X) , osoba(Y) , rodzic(Y,X) , kobieta(X).<br>
brat_rodzony(X,Y) :- osoba(X) , osoba(Y) , ojciec(O,X) , ojciec(O,Y) , matka(M,X) , matka(M,Y) , mezczyzna(X).<br>
brat_przyrodni(X,Y) :- osoba(X) , osoba(Y) , (ojciec(O1,X) , ojciec(O2,Y) , matka(M1,X) , matka(M2,Y)) , ((O1=O2 , M1\=M2) ; ( O1\=O2 , M1=M2 )) , mezczyzna(X).<br>
kuzyn(X,Y) :- osoba(X) , osoba(Y) , mezczyzna(X) , ( rodzic(R1,X) , rodzic(R2,Y), rodzic(D1,R1), rodzic(D2,R2) , D1=D2 ).<br>
dziadek_od_strony_ojca(X,Y) :- osoba(X) , osoba(Y) , ojciec(R,Y) , ojciec(D,R) , X=D.<br>
dziadek_od_strony_matki(X,Y) :- osoba(X) , osoba(Y) , matka(R,Y) , ojciec(D,R) , X=D.<br>
dziadek(X,Y) :- osoba(X) , osoba(Y) , mezczyzna(X) , rodzic(R,Y) , rodzic(D,R) , D=X.<br>
babcia(X,Y) :- osoba(X) , osoba(Y) , kobieta(X) , rodzic(R,Y) , rodzic(D,R) , D=X.<br>
wnuczka(X,Y) :- osoba(X) , osoba(Y) , kobieta(Y) , rodzic(R,Y) , rodzic(D,R) , D=X.<br>
przodek_do2pokolenia_wstecz(X,Y) :- osoba(X) , osoba(Y) , (rodzic(R,X) , R=Y) ; (rodzic(R,X) , rodzic(D,R) , D=Y).<br>
przodek_do3pokolenia_wstecz(X,Y) :- osoba(X) , osoba(Y) , (rodzic(R,X) , R=Y) ; (rodzic(R,X) , rodzic(D,R) , D=Y) ; (rodzic(R,X) , rodzic(D,R) , rodzic(P,D) , P=Y) .<br>
