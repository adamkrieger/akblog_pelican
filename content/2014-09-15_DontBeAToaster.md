Title: Don't be a Toaster
Category: Software Design
Tags: patterns
Summary: That time a comedy podcast got me thinking about the intent of software design, and our ability to forget it.

Lately, I've started listening to Dan Harmon's podcast: Harmontown. The format is far more exploratory than a television series, but it retains some of the structure of a late night talk show. I got in relatively late, but it's already on my recommended list. Full disclosure: contains profanity and discussion of some edgy topics.

<!--more-->

More towards the point, one of the opening dialog topics in Episode 111: "Fluid Levitation" centers around Shark Week. Dan and Jeff discuss recent integrity problems, such as fake documentaries and dramatic commercials, but then question why we should be surprised at all. Media's focus has distilled to an initiative intended only to guide the consumer to consume more media. The whole two minute bit comes to a head when Dan says “If you ask a Toaster its opinion of bread, it’s going to say ‘I don't think it's toasted enough’.”

The television is just an appliance, and it has the body of psychological knowledge powering its feedback loop. If toasters could do the same, there’d be an awful lot of people that preferred their toast burnt to a puck. My point rises out of those charred ashes: don’t be a single-purpose appliance.

### The Problem with Wanting to Toast Everything

Teams fluctuate. Members join and leave. When they join, it's common for them to bring along preconceived solutions. They say things like: "When I was at company x, we named all of our variables after cheeses", or other things that make little sense without context.

It's unwise to override the choices of the team that pre-exists, without consideration. It's even more unwise to show up to the party with a prescribed solution pattern and the intention to apply it unconditionally. The environment you're working in must play a factor in your end result, and you won't be able to adapt if you always use the same pattern. Technology, techniques, and catchy acronyms, can be seen similarly to the way E.P. Box saw models: all of them are wrong, but some are useful. Be willing to change your approach for the benefit of the product.

Remember that the absence of incumbent pattern does not circumvent the need for discussion, justification, and adoption.

### Hammer of the Month

Think of software tools as a hammer-of-the-month club. Every month's hammer is a specific library, or a language. If you're starting out as a developer, you probably have no choice but to hammer every nail with January's hammer. Once April comes around, though, consider the hammers you already have. Consider the tools that you can borrow from your friends. When you come across a dissonant solution, consider the possibility that a hammer was used to drive a screw.

Keep adding more tools to your toolbox. Learning how similar problems are solved differently provides counterpoint, perspective, and balance. You can't know the weaknesses of a tool unless you practice exercising the options. The Pragmatic Programmer suggests that you practice to the point where code feels like an extension of your thoughts. This practice also gives the added benefit of improving your skill at acquiring skill.

Don't just find better ways to toast bread; find toasting alternatives.

### Discrete Design

I’m reading through Code Complete, and one of the reiterated points is “Program into a language, rather than in it.” In other words, consciously decide on an approach or design before translating it into a toolset. Traditions and preconceptions that come along with any technology will influence your solution, but the presence of a technology-agnostic design can improve things. The discrete design step alone won't prevent sacrifice, but it can be used as guidance when balancing trade-offs.

For example, C# is a very feature-rich language, but it doesn’t yet support immutable classes. It’s possible to write classes that prevent mutation, but you’ll run into friction when trying to work with WCF and seemingly anything that uses proxy classes. Without defending beneficial principles while implementing, they will likely not be as prevalent or powerful in the finished product. If design dictates an aversion to flexible state, the team is more likely to correctly reflect that in the resulting code. In my case, while creating a WCF service, I was forced to add setters on properties, but only on the derived class. The interface was allowed to avoid them, but I may not have tried this without guiding design.

My recent design process centers around the desire for minimum viable product. I'm using that term somewhat abstractly, but I mean to say that I design one component at a time until I have designed something of value. At that point, I switch from design to translation. I look at my toolset, and the environment, and I attempt to implement as close to the design as possible. Working this way, I keep from working too far in the wrong direction.

### Conclusion

Understanding problems without being coupled to specific tech is a useful exercise. When you learn a new way to translate design into implementation, you might feel like liberally applying it to every problem surface. It's important to recognize that trap. Acquiring new tools and sharpening old ones builds up your instincts and adaptability, and this boosts your ability to choose the right guidelines for each unique situation.

Thanks for reading,

Adam Krieger
