pared1(E) :- E = [1,1,1,1,1].
camino1(A) :-  A = [1,0,fin,0,1].
camino2(B) :- B = [1,0,inicio,0,1].
camino3(C) :- C = [1,0,1,1,1].
camino4(D) :- D = [1,0,0,1,1].
pared2(F) :- F = [1,1,1,1,1].

empieza(X) :- camino1(A), member(inicio,A),
              X = A,!.
empieza(X) :- camino2(B), member(inicio,B),
              X = B,!.
empieza(X) :- camino3(C), member(inicio,C),
              X = C,!.
empieza(X) :- camino4(D), member(inicio,D),
              X = D,!.

termina(Y) :- camino1(A), member(fin,A),
              Y = A,!.
termina(Y) :- camino2(B), member(fin,B),
              Y = B,!.
termina(Y) :- camino3(C), member(fin,C),
              Y = C,!.
termina(Y) :- camino4(D), member(fin,D),
              Y = D,!.

conecta(Y) :- empieza(X), camino1(A), member(0,A), X \= A, remove(1,X,Zs),
              remove(1,A,Ys), append(Zs,Ys,Y), true.
conecta(Y) :- empieza(X), camino2(B), member(0,B), X \= B, remove(1,X,Zs),
              remove(1,B,Ys), append(Zs,Ys,Y), true.
conecta(Y) :- empieza(X), camino3(C), member(0,C), X \= C, remove(1,X,Zs),
              remove(1,C,Ys), append(Zs,Ys,Y), true.
conecta(Y) :- empieza(X), camino4(D), member(0,D), X \= D, remove(1,X,Zs),
              remove(1,D,Ys), append(Zs,Ys,Y), true.

remove(_, [], []).
remove(Y, [Y|Xs], Zs):- remove(Y, Xs, Zs),!.
remove(X, [Y|Xs], [Y|Zs]):- remove(X, Xs, Zs).
