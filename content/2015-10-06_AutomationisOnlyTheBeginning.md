Date: 2015-10-06 20:54:53-05:00
Title: Automation is Only The Beginning
Category: DevOps
Tags: automation, devops
Summary: That time I try to keep The Paradox of Automation in mind when building and maintaining pipeline products.

You've decided to automate a system. Software delivery, report creation, CPU threshold e-mails, whatever. Excellent! But beware: automation itself is not a solution, but a procedure for creating solutions. This nuance is so often overlooked that it has its own paradox named after it. Being ever original, it's known as *The Paradox of Automation*.

<!--more-->

> The more efficiently a system is automated, the more important humanity is in its success.

It's a common belief (thus the paradox) that a computer-modelled system requires less human involvement. Certain jobs, such as 'pudding cup filler', have been grossly replaced by machines. *(Aside from that farm-to-table, organic, vegan, pudding place that just opened in the canning district.)* Fewer humans needed, right? Great, end of story. See you in a couple of weeks.

**Not quite.**

Different humans are required. Engineers, maintenance technicians, and programmers, are all crucial to supporting and improving the system. The benefits of automated systems aren't in the manpower saved. Automated systems require more skilled work than manual systems.

### What's the Point of Automating?

So given that more skill is required to run these things, we must look elsewhere to get benefits.

- Predictability
   - Humans are human, and it is in our nature to vary results slightly
- Speed/Strength
   - Manual operations are restricted by human physiology
- Correctness
   - Shared perception of the right thing is key

Correctness can't quite be summed up in the quippy way that I just attempted, though.

### The Nature of Automated Mistakes

Correctly automating anything requires a thorough understanding of exactly what is supposed to happen. In order to guard against the paradox's effects, the resulting system must be correct. It's very hard to believe that one hundred people running a complex manual process in parallel will arrive with one hundred consistent results. Conversely, a mistake in an automated parallel process will be replicated one hundred times. Automation exchanges one class of problem for another.

### Teaching the Product

> "If you can't explain it simply, you don't understand it well enough." - Albert Einstein

People that can manually perform an operation, but cannot explain it, are less skilled than those that can do both.

Senior operators are often called on to teach juniors when a team needs to grow or cycle. Automators take the role of trainers, but rather than teaching the system to other administrators or developers, they explain the system using toolsets. This explanation is itself a living product that performs the process; the representation is a perception that stands apart from the conceiver. What a beautiful thing!

The automated product is therefore a perception of the process, albeit one with no ego or inertia. (Well, hopefully no ego.) Manual operators making mistakes have perceptions of their own. Frank, for example, might've learned how to press widgets from Karl. Any mistake, therefore, could be either Frank's or Karl's, or that of anyone else on the team whom has interacted with Frank. This already sounds like a lot of work to fix. In an automated process, the expressed product is the only thing that would need fixing, and the only question is whether or not it is correct. Neither Karl nor Frank need to feel sheepish.

### Raw Technical Prowess

Similar to the nature of mistakes, automation exchanges one class of problem for another when it comes to the vehicle. Significant effort and resources are needed to comprehensively and comprehensibly represent a process via a product. Humans trying to understand one another have the benefit of instinct and a plethora of senses. For example, it's easier to show someone how to play baseball than it is to explain it. Computers, however, only do what they are told through several layers of abstraction. The language, the interpreter, the virtual machine, the physical machine, plus or minus others. Automators must work with multiple mediums to express a process.

It's important to take as many steps as possible to **keep the system consistent**. The more the team shares expertise in a language, the easier the comprehension of the system. This explains why people deliver Ruby solutions with Chef (using Ruby syntax), or Java solutions with Puppet (using Java syntax). Ever tried to learn a new programming language and a new computer science concept with the same example? It's harder to comprehend than trying just one or the other. Using Ruby to deliver a Java product creates a persistent dissonance that gets re-encountered every time the system needs maintenance.

You can never really get away from naming problems. **Transparency is critical.** A file transfer action should look like a file transfer. There's no need to dress it up with terms like "binary delivery" or "payload upload". If there's a simple way to name the automation, *do it*. Leave ego on the nightstand.

Unnecessary complexity often creeps in as a result of mixed or coincidental cohesion. Importantly, **cohesion isn't a boolean quality**. There are many [types of cohesion](https://en.wikipedia.org/wiki/Cohesion_%28computer_science%29). Delivery is especially dense with sequential cohesion. That is to say, the output of one operation is required by the other. Sequential operations should be grouped only with others in that sequence, and the containing method should probably be named ____Sequence. Similarly, operations that have specific temporal or procedural constraints should be achingly clear about which is which.

### Mandatory Cyclic Conclusion

It's important to remember that the skill necessary to succeed in getting things done is always increasing. You never know, one day we might all be replaced with machines. Of course, we would then be responsible for programming and maintaining the systems on those machines.

Thanks much,

Adam Krieger