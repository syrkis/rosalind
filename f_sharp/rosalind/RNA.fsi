module RNA

type RNA = A | U | C | G

val transcribeChar : char -> char

val rna : string list -> string