open Parser
open System.IO

// For more information see https://aka.ms/fsharp-console-apps
[<EntryPoint>]

let main _ =
    
    // let task = arg.[0] // from command line argument
    
    // let funcs = Map [("dna", dna); ("rna", rna); ("revc", revc)] // dictionary of functions
    
    let readLines (filePath: string) = seq {
        use sr = new StreamReader ("../../../../../data/rosalind_" + filePath + ".txt")
        while not sr.EndOfStream do
            yield sr.ReadLine ()
    }
    // let data = Seq.toList (readLines (task))
    let data = (readLines "lcsm" |> String.concat "\n")
    
    printfn "%A" (lcsm data)
    
    0