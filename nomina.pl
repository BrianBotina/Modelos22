extra('tco',0.25).
extra('mto',0.10).
extra('hc',0).
extra('honorarios',0).
semestre(4).
valor_hora('tco','titular',200000).
valor_hora('tco','auxiliar',150000).
valor_hora('tco','asistente',100000).
valor_hora('mto','titular',200000).
valor_hora('mto','auxiliar',150000).
valor_hora('mto','asistente',100000).
valor_hora('hc','titular',200000).
valor_hora('hc','auxiliar',150000).
valor_hora('hc','asistente',100000).
valor_hora('honorarios','titular',200000).
valor_hora('honorarios','auxiliar',150000).
valor_hora('honorarios','asistente',100000).
vinculacion('juan','titular','tco',40).
vinculacion('maria','auxiliar','hc',30).
vinculacion('pablo','asistente','tco',15).
vinculacion('mario','asistente','mto',45).
vinculacion('pedro','auxiliar','honorarios',10).
vinculacion('alexandra','titular','tco',5).
vinculacion('alex','titular','mto',20).
vinculacion('brian','auxiliar','mto',35).
vinculacion('camilo','auxiliar','hc',8).
vinculacion('jairo','asistente','honorarios',50).

valor_contrato(N,V) :- vinculacion(N,C,T,H),valor_hora(T,C,VH),semestre(S),extra(T,E),VT is H*VH*S,A is VT*E,V is VT+A.