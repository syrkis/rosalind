module Transcriptomics

type Nucleotide = A | C | G | T | U

let parseChar c =
    match c with
    | 'A' -> A
    | 'C' -> C
    | 'G' -> G
    | 'T' -> T
    | 'U' -> U
    |  _  -> raise (System.ArgumentException "Invalid character")
    
let parseNucleotide N =
    match N with
    | A -> 'A'
    | C -> 'C'
    | G -> 'G'
    | T -> 'T'
    | U -> 'U'

let transcribe N =
    match N with
    | T -> U
    | N -> N
    
let complement N =
    match N with
    | A -> T
    | T -> A
    | C -> G
    | G -> C
    | _ -> raise (System.ArgumentException "Invalid nucleotide")

let dna (s: string list) =
    let rec aux s a c g t =
        match s with
        | []      -> String.concat " " (List.map string [a; c; g; t]) 
        | x :: xs ->
            if x   = A then aux xs (a + 1) c g t
            elif x = C then aux xs a (c + 1) g t
            elif x = G then aux xs a c (g + 1) t
            elif x = T then aux xs a c g (t + 1)
            else raise (System.ArgumentException "Invalid nucleotide")
    aux (List.map parseChar (Seq.toList s[0])) 0 0 0 0
    
let rna (s: string list) =
    String.concat "" (List.map (fun c -> parseChar c |> transcribe |> string) (Seq.toList s[0]))
    
let revc (s: string list) =
    let rec aux s acc =
        match s with
        | x :: xs -> aux xs (acc @ [x])
        | []      -> acc
    List.map string (aux (Seq.toList s[0]) []) |> String.concat ""
 