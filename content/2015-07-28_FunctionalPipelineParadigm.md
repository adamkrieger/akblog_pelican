Title: The Functional Pipeline Paradigm
Category: Functional Programming
Tags: fsharp, functional, syntax
Summary: That time I learned F# and realized how much more I like functional programming techniques, especially piping output to input.

Over a year ago, a colleague recommended that I try learning F#. A few tools and algorithms later, and I was hooked on functional programming. The first key concept is in the name. Functions build relationships between inputs and outputs. The benefits are unlocked when the software development paradigm shifts from programming a sequence of instructions to designing a programmatic workflow.

Purely functional languages eliminate imperative code in favour of declarative code. Imperative thinking is roughly equivalent to a dated manager-employee relationship. The manager tells the employee what to do, or directly asks for a result. The *if* statement is the poster child of imperative control flow. Here's an example of intentionally over-imperative code.

```cs
//Is there a cover on this TPS report?
if(tpsReport.hasCover()){
  //Good, then this report is considered final, by me, the manager
  var finalReport = tpsReport.finalize("Bob Bobberson");
  //Janet, please file this TPS report
  janet.fileThis(finalReport);
}
else{
  //Hmm, did you get the memo?
  if(yourMemos.contains(tpsCoverSheetMemo)){
    //You know we need to put cover sheets on all of our TPS reports now
    remind(tpsCoverSheetMemo);
  }
  else{
    //You know we need to put cover sheets on all of our TPS reports now
    remind(tpsCoverSheetMemo);
  }
}
```

In the above code, we've told the computer what to do at every step, or we've skipped over a section of code as the result of a check. This can be hard to keep straight. Additionally, *if* blocks tend to encourage the reference of entities that are out of context (janet, yourMemos). The nested *if* is only partly there for comedic value. I've seen my share of if/else blocks that, over years of refactoring, end up doing the same thing regardless of the condition's result.

Functional programming is often lauded for its natural application to math concepts. I think there's more. Consider the above problem as a workflow or pipeline. There is no controller or manager, and the evaluation or processing of an entity is only concerned with the necessary dependencies. Entities stream through the pipe, get transformed, diverted, and processed. Here's a possible example written in Elixir, one of the functional languages I've picked up over the last year. The **|>** operator is called a pipe. I've only seen this guy in F# and Elixir, and it really nails the metaphor, because, you know, it's a pipe. Its function is to pass the result from the left into the function on the right.

```elixir
# Reports are submitted to the system. For each report, if the report has a cover sheet, the report must be filed. The system must send an alert for all reports that don't have cover sheets.
def process(tpsReports) do
  # tpsReports are passed into a sorter, and the sorted reports are split into two lists depending on presence of a cover sheet
  # The result is a tuple of two lists: with covers, and without covers
  covered_uncovered = tpsReports
  |> Enum.sort(&(_sort_covered_reports(&1, &2)))
  |> Enum.split_while(&(&1.hasCover))

  # Send the covered reports to the filer
  elem(covered_uncovered, 0)
  |> Enum.each(&(_tps_report_filer(&1)))

  # Send the uncovered reports to the notifier
  elem(covered_uncovered, 1)
  |> Enum.each(&(_cover_sheet_reminder(&1)))
end
```

[This Example on GitHub](https://github.com/adamkrieger/learn_elixir/blob/master/tps_processor.exs)

### Benefits
1. The program flow doesn't appear to skip large sections of code as is so with **if** statements. The flow is easier to follow.
2. Each stage of the workflow only has reference to inputs and outputs. This reduces the number of places you have to look for dependencies and makes the code easier to maintain.
3. Piping flow reads left to right, top to bottom. At least for most people, this is more natural than process(split(sort(reports, sorter), splitter)), which you would have to read from the inside-out.

You need not do your daily work in Elixir, F#, Clojure, or Haskell, to appreciate and benefit from functional programming. C#, Java, and many other more imperative-rooted languages support at least this style of programming. The syntax may not be as clean. You may malign the lack of something like pattern matching, which I used while implementing the sort in the above example. Being knowledgeable of these concepts, though, and using them where appropriate, will increase speed of development and reduce cost of maintenance. There is also the possible side effect of feeling like a badass when you commit your code.

What do you think? Have you learned functional programming and changed your style? What has shifted your paradigm?

### Resources:
* [F# for Fun and Profit](http://fsharpforfunandprofit.com/) - A great site for learning F#.
* [Programming Elixir by Dave Thomas](https://pragprog.com/book/elixir/programming-elixir) - A great book for learning Elixir.

Thanks much!
