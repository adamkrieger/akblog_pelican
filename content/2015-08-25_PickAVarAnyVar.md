Date: 2015-08-25 20:54:53-05:00
Title: Pick a Variable, Any Variable
Category: Programming Practice
Tags: referential transparency, clarity
Summary: Those times when code looks like magic because it doesn't properly track inputs and outputs.

The magician's mastery of sleight of hand can be enthralling. A magician can take what you know (input), combine it with flourish and props (externals), and give you a result you may not have expected (output). If you're my target audience though, you're more likely to be reading code. Sleight of hand in source code is simply frustrating. Removing the external dependencies until functions operate solely on input is called **Referential Transparency**. It can reduce surprise, and less surprise leads to more productivity.

<!--more-->

Things that fool us while we're trying to do a job are generally unwelcome. _Sleight of variable_, intentional or not, wastes a programmer's time.

Referential Transparency, one of the principles of functional programming, is here to help. **A function is referentially transparent if it can be replaced with the value it would result in for a given input.**

Tell a computer 'Give me five', and the computer will give you five.

```cs
public int GiveMeFive(){
  return 5;
}
```

Use this same approach on a human, and you'll get varying response depending on state or environment.

```cs
// Human brain grossly oversimplified
public int GiveMeFive(Person dude){
  Recognize(dude);
  if((_iKnowThisGuy && _hesNotAJokester) || SomethingGreatJustHappened()){
    return 5;
  }

  return 0;
}
```

You may or may not be left hanging. The variable *iKnowThisGuy* is an example of some data that GiveMeFive uses, **but does not take as input**. This means that humans are generally **referentially opaque**, which is to say that their responses are influenced by factors out of your control. Don't run off an try to control them, though. Let's get back on task.

GiveMeFive(), in the first example, could be replaced by the literal 5 wherever it was called. That's the concept, but it's not particularly useful on its own. What if the function had a wide array of outputs based on a wide array of inputs?

### Optimization via Memoization

Consider a Caesar Cipher, where each letter is cycled a certain number of characters to form a coded alphabet.

```cs
public char Encode(char original, int codeKey){
  //Shift and return encoded letter
}
```

Anything that calls this function with *'a'* and *4* could be replaced with *'e'*, *'m'* and *2* replaced with *'o'*, and *'z'* and *2602* with *'b'*. The function is the vehicle that drives from the input to the output.

The beauty of this is that we're probably going to encode the same letter-key combination many times in a message, and we're going to use the same code key for every letter in the same message. If the encoding process is referentially transparent, we can **memoize** it. This is a technique used in **dynamic programming** to shorten the overall compute time by reusing computed results. Memoization is a specialized form of caching.

Suspend your disbelief and assume that it takes a really long time (RLT) to encode a letter. Encoding a one thousand character string would take 1000 * RLT. If you stored each output in a map, the encoding now takes a maximum of 26 * RLT + MASO *(Map Access and Storage Overhead)*. A map data structure would be used to store the precomputed outputs, and could be checked to see if the **input has already been solved for** on successive iterations. In practice, compute time is better than linear in the average case.

Given a referentially transparent function that has a maximum number of inputs, or one with a strong weighting towards a set of inputs, memoization can help.

### Assisting with Comprehension

It's easier to read referentially transparent functions. The following assumptions reduce the amount of time it takes to comprehend the journey from input to output.

- All variable dependencies must be inputted
- Nothing except input and constants can be used

Magic tricks are more compelling when the magician simplifies the environment. "Nothing up my sleeve!" they say, as cuffs are rolled up. It's a ruse, obviously, as the viewer's focus is still being manipulated. It's a skilled magician that fools you with fewer factors. Code, though, legitimately shouldn't have anything *up its sleeve*. Reduce the number of places you have to look for meaning, and the meaning will be understood faster.

### Not Always Appropriate

```cs
public bool IsItTimeToEatBreakfast(){
  var min = _breakfastDb.ReadMin();
  var max = _breakfastDb.ReadMax();
  var thisHour = DateTime.Now.Hour;
  if(min <= thisHour && thisHour <= max){
    return true;
  }

  return false;
}
```

Time, accumulators, databases, and other functions are often accessed using module or global scope. They're regularly used and even mutated without providing transparency to the caller. The caller has no way of knowing what kind of environment is necessary to make the decision. The calls cannot be replaced with values.

```cs
public bool DoesFileContain(string filename, string word){
  //The magic happens
}

public bool IsItTheAfternoon(Func<DateTime> timeGetter){
  //Abra-kadabra
}

public IEnumerable<Record> RecordSearch(DatabaseConnection db, string searchString){
  //Assorted pyrotechnics
}
```

These functions may look referentially transparent, but they're not. DoesFileContain probably accesses a file system that isn't input, IsItTheAfternoon would talk to the operating system, and RecordSearch would reach through the database connection interface to get dependent data.

Sometimes it's best to hold state and take requests, or mask an environment that the caller doesn't know about, but the intent must be clear. It should be obvious to the reader that the code makes use of inputs, external resources, or both. With scope-dependant naming and some refactoring, you can uphold a standard of readability even when referential transparency isn't the goal.

### Tips

1. When functions really only make use of objects and literals, attempting referential transparency can improve readability.
2. Given referential transparency, memoization may drastically reduce processing time.
3. Functions using external resources should be obvious about that use, and are not referentially transparent.

Thanks much for reading. Have you used memoization successfully for referentially transparent processes? Have I given you something new to think about? Please leave a comment.
