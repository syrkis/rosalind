module Parser

type DNA        = A | C | G | T
type RNA        = A | C | G | U

type Protein    = A | B | C | D | E | F | G | H | I | K | L | M | N | P | Q | R | S | T | V | Y

type FASTA      =
    | RNA         of RNA
    | DNA         of DNA
    | Identifier  of string
    | Description of string
    
type FASTAResult =
    { Identifier  : string
      Description : string
      DNA         : DNA list 
      RNA         : RNA list
      Protein     : Protein list }

let charToDNA c =
    match c with
    | 'A' -> DNA.A
    | 'T' -> DNA.T
    | 'C' -> DNA.C
    | 'G' -> DNA.G
    | _   -> failwith "Character not DNA nucleotide"
let charToRNA c =
    match c with
    | 'A' -> RNA.A
    | 'U' -> RNA.U
    | 'C' -> RNA.C
    | 'G' -> RNA.G
    | _   -> failwith "Character not RNA nucleotide"
    
let (|Empty|Header|Data|) (line : string) =
    if   line = ""           then Empty
    elif line.StartsWith ">" then Header
    else                          Data
    
let parseDNA s    = List.map charToDNA (Seq.toList s)
let parseHeader s = List.map charToDNA (Seq.toList s)

let parseAny line =
    match line with
    | Data           -> parseDNA line
    | Header | Empty -> []

let parse (source: string) = Seq.map parseAny (source.Split("\n"))

let lcsm s = s |> parse
