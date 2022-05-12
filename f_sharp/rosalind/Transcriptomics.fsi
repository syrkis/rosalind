module Transcriptomics

type Nucleotide = A | C | G | T | U

val parseChar  : char        -> Nucleotide
val transcribe : Nucleotide  -> Nucleotide
val complement : Nucleotide  -> Nucleotide

val dna        : string list -> string
val rna        : string list -> string
val revc       : string list -> string
