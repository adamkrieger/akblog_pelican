Title: Python as a DevOps Vehicle
Category: DevOps
Tags: devops, python
Summary: That time I justify the use of Python as goto DevOps glue.
Illustration: trunk_board.jpg

The answer is Python. The question is:

> What language should we use to get an introduction to DevOps development?

I believe that's a pretty safe answer, but if you don't agree, let me see if I can win you over with the following points.

### Baked in with Linux

DevOps practices run better on Linux. I'm not sure if I have to back that up, or if the conjecture alone is enough. The development landscape today, for quite a while, and probably for quite a while to come, has felt better to me on Linux. And what language comes in the box with Linux? That's right, bash. 

_Wait, what?_

Let's consider bash for a sec. You can do just about anything you want with it. You can even write a web framework, such as the industry standard goto: [Bash on Balls](https://github.com/jneen/balls). Here's an excerpt from the readme:

> Because, you know, we can.

_A ringing endorsement._

Bash, in actual seriousness, is a good language. It has a massive body of use, extensive support, and it certainly is going to be in use for generations to come. Bash is also very composable. Composability, the quality of a language that tells you how easy it is to assemble its parts, is *very* important for DevOps. There are many moving parts in a typical enterprise-level infrastructure, and the easier it is to move them around at-will, the fewer headaches you're likely to experience.

Bash also carries the advantage of knowledge and muscle memory. Every sysadmin that I've encountered knows their way around bash. From a developer-first perspective, which I admitedly _have_, bash doesn't lend well to learning the fundamentals of modern day software practices. Inputs and outputs, data structures, and the treatment of 'entities', is where the bash argument falls flat for me.

Python is almost as baked-in with Linux as bash is, but has the feature set of a productivity-friendly programming language. I believe we should use the lesson in composability as a reminder. Our component pieces of DevOps glue should be small and abstract, if not generic. 

We may have a tough time convincing our respective sysadmins to learn Python. Learning Python as a programming language is different than learning bash as a shell language, and can require a paradigm shift. It's worth it though, for all 'Ops' techs to make that leap. Just as it is worth it for the typical sheltered developer to get their hands dirty with load balancers and virtual machine configuration.

### SDKs, the Clouds, and Declarative Simplicity

AWS, Azure, and Google Cloud, all have Python SDKs available on pip, the Python package repository. For those not in the clouds, VMWare even has a Python SDK. The other frameworks usually featured are .Net, Java, PHP, and Ruby. 

Like I laid out in the bash example, we want a language thats easy to learn, to use in small doses, and is very compositional. .Net and Java, in my opinion, fall short because they are both a little too strict. They will help keep you in line when it comes to objects, but infrastructure representations can be very flexible. If you can rapidly gain or lose Configurable Items (CIs), we need an implementation that's equally flexible. 

PHP and Ruby, for me, are just okay, even as developer languages. I tend to group them into the realm of esoterica for the uses that DevOps requires. I, admittedly, do have less experience with them, but this use case doesn't seem to be their strength.

Python, on the other hand, has some very interoperable tendencies, particularly with data structures. I mentioned that they must be flexible, and I therefore recommend sticking to dicts and lists for all of your models, and JSON for the notation. JSON and Python work very fluidly together, as any JSON data structure can be pasted verbatim into Python code. The data that gets assigned becomes a nest of Python dicts and lists. Addutionally, in the event that you need to step out of SDK functionality and make use of a REST service, you are already writing in JSON notation. Python structures and JSON are declarative, but also very simple, only making use of squigglies, squares, commas, colons, and quotes. An extra point in the easy-to-learn column.

### Use the Tools that Use the Language

Ansible is written in Python on the Linux platform. Ansible is a wonderful tool to learn for resource provisioning. It's agentless, thereby using a more flow-friendly implementation, and as such makes use of ssh and Python on the client (which is actually a server) side. So you're running Python to run Python, and you can program in Python that gets run by Python. All learning done in this space is therefore cumulative.

Jinja2 is a robust and widely use template language. _Heck, it's even used by Ansible._ Templates are useful for a wide range of things, from your first configuration settings to, well, your other three hundred configuration settings.

### Have an Opinion

Python comes with opinions on how to do things. It has its own [Zen](https://www.python.org/dev/peps/pep-0020/). Python even has its own nomenclature for practitioners (Pythoneers) and quality (Pythonic). 

_Nevermind, ignore the last point. Pythonista koolaid makes my eyes roll. The Zen's good though... read the Zen._

Python 2.X is executed with `python`, and 3.X is executed with `py`. This turns out to be a useful decision in practice, as you can maintain tools in old versions without accidentally executing them under the wrong framework.

But after all this, I encourage you to have an opinion as well. Please try it out. Write some deployment glue for a product, no matter how small, and let me know if Python was right for you in the comments. This blog is being deployed with a combination of Docker and Python. The conversion from the old deployment pipe was very simple, and the process is fully automated with Travis.CI. I wish you the same levels of success.

Thanks much,

Adam Krieger