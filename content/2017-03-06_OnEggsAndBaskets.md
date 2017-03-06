Title: On Eggs and Baskets
Category: Architecture
Tags: cloud, architecture, devops
Summary: That time I reflected on the s3 failure of early February 2017.
Illustration: trunk_board.jpg

On February 28th, my favourite *annual* day of February, an S3 outage caused a sudden and rippling wave of disruption that upended a good portion of the the known internet. 

*I can’t really speak of what it did to the unknown part.*

If you’re not familiar with S3, it’s possibly the most popular data bucket service out there. Your data is an egg, and S3 is a basket. Really though, it’s more like a massive network of baskets. It comes OOTB with a tremendous amount of redundancy and safeguarding, but on that fateful day, one individual at AWS entered a command which put all of those baskets in one **freaking-huge** basket and proceeded to drop it.

The tech media had a hay day. As far as I can tell, it’s the first ever use of the term [‘cloudsplaining’](https://techcrunch.com/2017/03/02/aws-cloudsplains-what-happend-to-s3-storage-on-monday/). I, naturally, hope this term makes it into the lexicon of the IT industry for years to come.

### Egg on the Internet

Web apps don’t advertise which pillars of supporting services they rest on, but even the non-savvy consumer now has a pretty good idea of which sites are backed by S3. And son of a racehorse, that thing is pervasive.

### Diverting Power from Non-Essential Services

The failure affected different products in different ways. A lot of sites simply fell over, but we ought to learn a thing or two from the services that ran, or limped along, despite dependency on a failing service. Slack’s image-uploading capabilities were inaccessible, but chat was largely unaffected. Slack has constructed a product that interfaces with capabilities, but reduces its service offering when those interfaces don’t bear fruit. This is known as **Graceful Degradation**. Netflix is well-known for reducing the quality of streams and throwing away value-adds as if they were dented armour that encumbers more than it protects. 

Network connections have proven to be unstable in practice. 

*Who knew?* 

But developers have the option, and probably the responsibility, to salvage as much experience as they can. If my stack of buzzword bingo cards are to be believed, experience is what keeps your users and customers coming back and choosing you over the competition. Software experiences are relationships, and it’s the way a relationship behaves in times of trouble that reveals its quality.

### You Have to Ask One Question, Twice

Not only was S3 down, but AWS’s status panel continued to indicate that it was still up. The status panel, as it happens, was also dependent on S3. Whether you gracefully degrade service or not, accurate information is paramount. Services can be built to find out for themselves whether or not their dependencies are accessible. And truly, this puts the determination of service uptime in the place where it matters most: the place where it’s being used.

Regularly attempting communication with a downed service can be resource-intensive, but assuming that a traffic light is giving you the best information can be just as costly. Making use of more than one stream of information will likely lead you closer to the truth.

### Egg on AWS

The event brought down a great number of services. *Yes.* AWS probably cost their client base a non-trivial amount of money in lost revenue. *Check.* But I don’t suspect it will make a long-term dent in the use of their services. Product developers will continue to use AWS, and each party should use this as a learning experience. Resiliency, as it turns out, is both a vendor and a client concern.

### Hybrid-Basket Infrastructure

To achieve the next level of resiliency, applications dependent on any one suite need to bridge across two or more. Cloud-only solutions may need to be supported by on-premesis resources. So AWS may see a reduction in use as consumption is balanced across more vendors, but they’ll also see an increase as wise product developers branch out to AWS from other sources.

Hybrid cloud tools should see a rise in popularity and development. 

*So take the sheer slope on your line graph and turn it into a vertical wall.* 

We will need more expertise with multi-cloud deployment tools, and with negotiating subtle nuances between the destinations. Ansible, Puppet, and Chef, which abstract the deployment action, will more often be deploying to multiple hosting platforms.

Once deployed, we’ll also need to abstract the host. Bridging a quorum across multiple infrastructure providers with Mesos, Kubernetes, or Swarm, could become a standard practice. A resilient node-network may even need to be aware of what percentage of its services rest on any one platform, and make adjustments as necessary. 

*Or, you know, we could continue on like we sometimes seem to, and prefer to apologize rather than engineer our way out.*

### Internals Can Have Products, Too!

Administrators give themselves too much rope. They, myself included, are not perfect. In the case of this outage, servers were supposed to go down, just not that many. This was an intended and scheduled maintenance action gone awry.

DevOps practices share the best Dev practices with Ops (and vice versa). UX tells us that interfaces should guide and assist the user. Ops staff should therefore be using a developed interface to perform tasks. If we need a new software feature, we wouldn't open the database to Tier 1 support and get them to manually punch things in; we would design how it will be used and build a service. Ops should get the same red carpet service that external users get.

I’m assuming a little about the S3 case. I’m assuming that this individual, whom I’ll call Alice *(I’m narrowing my eyes at you, gender-biased tech media)*, left something off a command that would have narrowed down the scope of servers. On a command line, mixed with two hundred other characters, two keywords at different scopes can look pretty similar. 

Amazon has said that they will improve procedures and tools to ensure a “minimum required capacity level”. That, to me, sounds like a job for a declarative language combined with a constraint system that’s tied into a monitoring interface. 

*Side note: Ansible uses a declarative language to define actions, and this empowers us to express intentions independent of implementation.*

### SmartRope

I’ll call this fictional admin tool SmartRope. 

*Giving you less to hang yourself with since 2017.* 

Rather than telling this tool “shut down these servers”, you will tell it that you want the servers in a shut down state. This tool would probably do the same thing as a terminal command in practice, but this allows us to pass the end-state picture into a constraint system. If one of the constraints says that we can never have more than 10% of the platform offline at any one time, and the state we’ve desired would violate that, the operation would be aborted. 

In order for these constraints to work well, they’d have to be supplied with a good understanding of how much of the platform is currently offline. And there you have a need for a stream of trustworthy information.

This very quickly becomes a full-blown product, but certainly one that I’d be interested in building, and even using.

### TLDR

Overall, this event teaches us that we can achieve better resiliency by

- Bridging service platforms
- Balancing sources of information
- Productizing infrastructure operations

Thanks much,

Adam Krieger