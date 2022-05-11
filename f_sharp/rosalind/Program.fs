open DNA
open RNA
open System.IO

// For more information see https://aka.ms/fsharp-console-apps
[<EntryPoint>]

let main arg =
    
    let task = arg.[0] // from command line argument
    
    let funcs = dict [("dna", dna); ("rna", rna)] // dictionary of functions
    
    let readLines (filePath: string) = seq {
        use sr = new StreamReader ("../data/rosalind_" + filePath + ".txt")
        while not sr.EndOfStream do
            yield sr.ReadLine ()
    }
    let data = Seq.toList (readLines (task))
    
    printfn "%s" (funcs.[task] data)
    
    0