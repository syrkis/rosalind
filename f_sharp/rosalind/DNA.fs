module DNA

type DNA = A | T | C | G

let parseNucleotide c =
    match c with
    | 'T' -> T
    | 'A' -> A
    | 'C' -> C
    | 'G' -> G
    | _   -> raise (System.ArgumentException "Invalid character")
    
let countNucleotides s = List.map (fun N -> List.length (List.filter (fun n -> n = N) s)) [A; T; C; G]
    
let dna (s: string list) = List.map (fun c -> parseNucleotide c) (Seq.toList s[0])
                           |> countNucleotides
                           |> List.map (fun i -> i.ToString())
                           |> String.concat " "
