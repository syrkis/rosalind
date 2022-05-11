module DNA

type DNA = A | T | C | G

val parseNucleotide: char -> DNA

val dna : string list -> string