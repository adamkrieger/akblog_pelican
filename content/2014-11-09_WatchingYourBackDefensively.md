Title: Watching Your Back with Defensive Programming
Category: Programming Practice
Tags: safe code
Summary: That time Murphy and Ockham fought about programming.

Defensive Programming is a design principle which indicates that code be written with the understanding that it is not in control of its inputs or environment. It mandates that you validate thoroughly.

<!--more-->

Let’s jump straight into a contrived code snippet (C# in these examples). If you pass very large positive or negative integers into this function, you may quietly get an overflowed return value.


```cs
public int AddAtoB(int a, int b)
{
     return a + b;
}
```

Compare the above with the following, which checks for two known situations:
* When values added together would cause a maximum value overflow
* When values added together would cause a minimum value overflow

```cs
public static AddResult AddAtoB_Defensively(int a, int b)
{
  if (
	  (
		  (a > 0)
		  && (b > 0)
		  && (b > (int.MaxValue - a))
	  )
	  ||
	  (
		  (a < 0)
		  && (b < 0)
		  && (b < (int.MinValue - a))
	  )
  )
  {
    return new AddResult(
         success: false,
         result: -1,
         errorMessage:"Addition would have caused overflow.");
  }

  return new AddResult(
        success: true,
        result: a + b,
        errorMessage: string.Empty);
}
```

The defensive example has a lot going for it:
* It's more resilient
* It has a strong return type
* There’s a little self-documentation going on
* It's name rhymes

Defensive code reduces debugging time because it makes clear to the reader that certain circumstances are considered invalid. Following the ‘Pragmatic Programmer’ tip ‘Exceptions are Exceptional', it implements a user-defined type instead of just throwing an exception. I prefer this design choice because of its self-documentative nature, and because it’s easier to avoid spaghetti code in construction. Defensive code is not just about making decisions, but also about making the consequences clear. The caller must now know that a success flag is returned with the result, and they are more likely to deal with it before trusting the result.

### Beware of Shortcuts

Proper use of TDD will reveal the flaws in AddAtoB and push the outcome in the direction of AddAtoB_Recursively, but it should happen incrementally. Testing for upper and lower bounds, hunches, and what-ifs, will all force code to be more defensive. Iterative improvements allow the procedure to fail gracefully, but also consciously. This is the beauty of test-first. Just as the original example made too many assumptions about the input, it’s possible to mutate those assumptions into something that doesn’t work like you may expect.


```cs
public static AddResult AddAtoB(int a, int b)
{
   var result = a + b;

   if(
        (result < a)
        ||
        (result < b)
   )
   {
        throw new Exception("Addition would have caused overflow.");
   }

   return new AddResult(
        success: true,
        result: a + b,
        errorMessage: string.Empty);
}
```

This time, the case throws an exception instead of providing the intended outcome. As you also may notice, the case is written incorrectly. The programmer only considered high end overflow, and missed negative addition. Poorly written cases, and the lack of clear result, often go hand in hand. They are both a symptom of incomplete analysis.

Test-last construction can reinforce incomplete analysis if we don’t train ourselves to be skeptical of our own product.  Tests which don’t take the whole method into account can end up defending poor code, and the way forward may no longer be clear. Overturning production code when a missed case is found is a touchy subject. The likeliness of the case being hit, and the severity of the output, should be examined. Research, documentation, and discussion, are your best outlets. Changes made without thought are reckless, but prevention of emergency can be very valuable.

### Philosophically Speaking

It’s worth considering both Murphy's Law and Ockham's Razor when discussing Defensive Programming.

Murphy's Law: Anything that can go wrong, will.

Ockham's Razor: Of competing hypotheses, the one with the fewest assumptions should be selected.

Ockham's Razor is often quoted as "The simplest solution is the best.” This is subtly, but importantly, different from the above. Simple code has storied advantages, but I want to set that topic aside for now. The act of making fewer assumptions can lead to fewer defects, but it can also lead to code that is not simple, per se. The Wikipedia article contrasts simple hypothesis versus simple description, and interpretation is polarizing. My interpretation in this article sides with ‘fewer assumptions’, at least from a software construction perspective, because it aligns with Defensive Programming.

### Murphy’s Law

Earlier, I mentioned that the likeliness of a bad case should be taken into account when deciding whether or not to overturn working production code. Murphy’s Law doesn’t indicate what to do in this situation, but believing in it leads us to more simplified analysis. If everything that can go wrong, will, then likeliness cannot be used as a metric. Every case has a one hundred percent chance of occurring. Knowing that, severity of outcome rules.

### Conclusion

Defensive programming is the use of Ockham's Razor to mitigate the effects of Murphy's Law. We must assume that we will get bad inputs. We must assume that our environment is mutable unless we have control of it. We must deal with all outcomes which are considered unacceptable, and we must do it with conscious intent. These understandings protect the products we make, as well as the people and systems which use them.

Thanks for reading,

Adam Krieger
