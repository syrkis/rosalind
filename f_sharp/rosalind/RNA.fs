module RNA

type RNA = A | U | C | G

let transcribeChar c =
    match c with
    | 'A' | 'C' | 'G' -> c
    | 'T'             -> 'U'
    | _               -> raise (System.ArgumentException "Invalid character")

let rna (s: string list) = List.map (fun c -> transcribeChar c) (List.ofSeq s[0])
                           |> System.String.Concat