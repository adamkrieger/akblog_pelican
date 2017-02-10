Date: 2015-09-08 20:54:53-05:00
Title: Know When to Fold'em
Category: Functional Programming
Tags: fsharp, functional
Summary: That time I discussed when to use F#'s fold over reduce.

'The Gambler' is one catchy song. I used to work with a guy who felt compelled to finish the chorus if you prompted him with the first line. This post is not about that song, nor is it about him. This post is about trying to solve an algorithm in a purely functional way, and it's about the subtle differences between __reduce__ and __fold__.

<!--more-->

Functional programming fundamentally changes the way you approach algorithm design. Most imperative approaches lead to non-atomic solutions. Examples of what I see in typical solutions:

- Multiple uses of pointers or references
- References that float around at module-level scope
- Intermingled control flow, or loops within ifs within loops.

### The Challenge

Consider the lonely integer problem. Given an odd-length array of *n* integers, guaranteed to have only one value which doesn't have a pair, find the lonely value. Full problem listed on [HackerRank](https://www.hackerrank.com/challenges/lonely-integer).

One solution is to maintain a set of values with no pairs. As you iterate through the array, check to see if the value exists in the set. If it does, remove it from the set, and if not, add it to the set. After iterating through all of the items, the only value which wasn't removed from the set is the lonely integer.

Rather than telling the computer exactly what to do, let's declare the outcome by...

### Solving it Functionally

Given the big three functional operations: Map, Filter, and Reduce, what can we do?

- __Map__ probably won't help on its own. Each value needs to know about the others in the array to determine if it has a pair. We could give the map function reference to the array, but that raises the compute time to n-squared.
- __Filter__ sounds right, since we want to filter out the pairs. Like map, though, the filter function would need knowledge of the whole array.
- __Reduce__ will collapse each pair in the array, keeping track of what we know of so far. After reducing the collection and pairing-off whenever possible, we should know which element is the odd one out.

Reduce is the best match so far. Given `[|"a"; "b"; "a"|]`, here is the step-by-step resolution. I used letters instead of integers for this example because it provides clarity while not changing the problem. `[| |]` is array syntax in F#.

*Spoiler: Reduce is going to produce a bit of a messy solution, but going through the process is important.*

1. Wrap each element in an array, converting `[|"a"; "b"; "a"|]` to `[| [|"a"|]; [|"b"|]; [|"a"|] |]`.
2. Reduce `[|"a"|]` and `[|"b"|]` to `[|"a"; "b"|]`. The only element of `[|"b"|]` does not exist in `[|"a"|]`, so the value is appended to the initial state.
3. Reduce `[|"a"; "b"|]` and `[|"a"|]` to `[|"b"|]`. The only element of `[|"a"|]` does exist in `[|"a"; "b"|]`, so the value is filtered out of the reduction.
4. Solution found to be the only element after performing the reduction across the input: `"b"`.

Here's the F# code

```fsharp
let toArr x = [| x |]

let valFilter (value:string[]) arr =
    Array.filter (fun x -> x <> value.[0]) arr

let valExists (value:string[]) arr =
    Array.exists (fun x -> x = value.[0]) arr

// If the value exists in the accumulator, filter it out
//  And if not, append it
let pairOff (accum:string[]) (value:string[]) =
    match (accum,value) with
    | (accum, value) when valExists value accum -> valFilter value accum
    | _ -> Array.append accum value

let size = Console.ReadLine()

let array =
    Console.ReadLine().Split ' '
    |> Array.map toArr
    |> Array.reduce pairOff

do Console.WriteLine array.[0]
```

As mentioned in the spoiler, I had a couple of problems with this approach.

- Each item has to be pre-wrapped in an array so that it can be reduced into the accumulator
- valFilter and valExists need to specify type because the element gets accessed during reduction

### Turning Point

When using **reduce**, the accumulator needs to be the same type as the elements in the collection. **Fold**, however, lets us use any type as the accumulator. It could be a string, a collection, or something completely different.

Same algorithm using fold instead of reduce.

```fsharp
let valFilter value arr =
    Array.filter (fun x -> x <> value) arr

let valExists value arr =
    Array.exists (fun x -> x = value) arr

let pairOff accum value =
    match (accum,value) with
    | (accum, value) when valExists value accum -> valFilter value accum
    | _ -> Array.append accum [| value |]

let size = Console.ReadLine()

let array =
    Console.ReadLine().Split ' '
    |> Array.fold pairOff [||]

do Console.WriteLine array.[0]
```

- Type annotations are gone, which permits greater reuse and better readability.
- Element pre-mapping is gone, which improves performance.

What **Reduce** and **Fold** accomplish are very similar. In this case, it turned out that Fold was better than Reduce, but don't ignore the power of reduce either. Reduce uses the first element as the initial state, but all results must be of that type. Fold allows the result to be of any type, but requires that you provide an initial state.

Reduce is more suited for

- Summation, and many other number problems
- String concatenation
- Resolving multiple states of an entity, such as when an object changes over time

Fold is more suited for

- Division or combination of elements, or when the collection should get larger or smaller
- Keeping track of more than one value while iterating, such as in the lonely integer
- Processing events against against an initial state, as in an Event Store

Have you found a solution that was better solved with one or the other? Do you have a great example of a category of problem that I didn't list? Please let me know in the comments.
