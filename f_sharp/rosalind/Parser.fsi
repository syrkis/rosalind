module Parser

type DNA        = A | C | G | T
type RNA        = A | C | G | U

type Protein    = A | B | C | D | E | F | G | H | I | K | L | M | N | P | Q | R | S | T | V | Y

type FASTA      =
    | RNA         of RNA
    | DNA         of DNA
    | Identifier  of string
    | Description of string
    
type FASTResult =
    { Identifier  : string
      Description : string
      DNA         : seq<DNA>
      RNA         : seq<RNA>
      Protein     : seq<Protein>} 
