Title: Push Button, Get Value
Category: DevOps
Tags: delivery, devops
Summary: That time I compared Continuous Integration to pneumatic tubes, and I recommended that they become products in and of themselves.

Pneumatic tube delivery systems are as awesome as they are comical. I tried my best to find The Simpsons's parody of the tube scene from Stolen Kisses, but couldn't. I did, however, find this pneumatic-tube-themed Heineken commercial. This is what software delivery should be: push-button, stuff happens, ecstatic customers. So where do you start, and where are the easy wins?

<!--more-->

<iframe width="560" height="315" src="https://www.youtube.com/embed/wZu6tcvl6vE" frameborder="0" allowfullscreen></iframe>

Let the beer represent value. Still with me? Good. The fact that the beer gets delivered used to be enough. Old models of software delivery are analogous to a beer-delivering butler, or even a team of beer-delivering butlers. Those butlers would've had a forty-page manual explaining exactly how to get the beer from the fridge to the *Master of the House*. That manual would be covered in margin notes, maintained by the most senior butler, and never read by anyone.

How do we get from hand-holding, manual delivery, to the orchestrated dance of a fully automated system?

### Break It Down

**Distill the delivery process down to an algorithm.** Pull the components apart until they start to look more like steps. Build systems to perform those steps. Reassemble the systems using methods that lead into one another.

After doing so, it should look a little like this:

- Write the software
- Package it
- Deploy it
- Install it
- Verify that it works

Picture each of these steps as a function with discrete inputs and outputs. Abstract the idea of *input* so that it doesn't just look like data in a data structure. Files, source code, ideas, and requirements, are only a few examples of input in the broader sense.

| Step |       | Input                  | Process                         | Output |
| ---  | ----- |:-----                 |:-------                        |:----- |
| 1.| Code     | Software conception    | Press keys                      | Local source code |
| 2.| SCM      | Commit change and push | Envelope in commit and transfer | Code marked with assigned revision |
| 3.| Build    | New revision present   | Build outputs                   | Binaries in a directory |
| 4.| Transfer | New binaries present   | Transfer to environment         | Binaries on a server |
| 5.| Install  | New binaries on server | Installation (*waves fingers*)  | Installed and running product |
| 6.| Verify   | Startup complete       | Run automated checks            | E-mail sent to the client |

Each of these steps could be performed by a ~~code butler~~ human. Each of them is more comprehensible and transparent when looked at individually. **Focusing in on building, transferring, and installing the product**, there are a number of improvements worth their weight in logged hours.

### Triggered Build and Transfer

**Continuous Integration** servers, or CIs, watch source code repositories for changes. Each repository commit can trigger a build and a round of automated tests. Most CI servers will also give you some way to notify the team of the build and test results. Jenkins, Travis, and TeamCity, are just a few examples. Some are free, and some aren't. It's a huge topic, so I'll have to gloss over it for now. Whether you continuously deliver to production or not, use a CI server and trigger a build on commit.

At this point you've already got unexpected benefits. The developers - *your production line* - get near-instant feedback about the work they've just committed. If the build results in an error, or tests fail, very little time passes before the team knows they have something to fix.

> **Tip:** The types of problems you see at this point should be related to integration. If developers are making mistakes that should have been caught on their personal environment, there's a coaching opportunity.

> **Another Tip:** Make sure the developers are using the same compiler and version as the build server. It sounds obvious, but double-check, maybe even triple.

> **Oh-hold-on-one-more Tip:** Try to use a CI server that has an affinity for your framework. Hopefully the server will boast that it's the best way to build and push *Framework X*.

Now automate the transfer step that moves binaries et al to the destination server. These files will eventually pile up, so make sure to automate the reclamation of space as well. This is likely to be implemented with a combination of CI server functionality and shell scripting.

The output of the build and transfer steps will be the input of the installation step.

### Flow of Installation

Installation automation can be an incredibly complex step depending on your framework. It may even be useful to automate a piece at a time, while giving the operations personnel cues about when to perform manual tasks. A given installation will most likely include a number of these steps:

- Service shutdown and startup
- Binary or script replacement
- Database migration
- Directory creation
- Security configuration
- Special handling for transactions in progress

Solutions for this can range from off-the-shelf products like Octopus, to completely customized toolsets like Chef and Puppet, to even more customized shell scripts. The path taken to automate installation is extremely important. The most maintainable and productive installation automations are designed to be:

- *Comprehensible*
   - New team members, as well as those that haven't touched the process for a while, should be able to pick up the flow quickly.
   - Clear beats clever, especially during deployment.
- *Cohesive*
   - Use a system that lets you code within your framework, if possible. Chef for Ruby, Puppet for Java, etc. Teams will spend less time hunting down syntax options and implement more advanced techniques.
- *Adopted*
   - Get the whole team on board, or at least 80%. The delivery process is going to need support, so make sure you have a lot of it.
   - Delivery is a responsibility, not a job title.

#### Two Quick Notes on Installation and Value

Automating the installation molds it into a product, as opposed to a process. Heavy processes are wasteful and bloated, but heavy products can be rich with value. This a powerful paradigm shift that reveals itself when installation is decoupled from the person or the team doing the installation. The value was there before, but it's now something that can be touted and revered.

Trust is key in repeat business. Consumers will continue to shop at a store they know because that retailer has built a level of trust that is *valuable*. Automated installation can provide that same level of value. Giving clients the ability to predict smooth delivery will bear fruit on every successive tree of communication.

### Now What?

I've barely scratched the surface, but I believe in automating delivery. The value is there, and it's worth investing in. Explicitly declare that delivery is value by referring to it as product. Push the button, get the solution to the client, and don't forget to celebrate!

Thanks,

Adam Krieger