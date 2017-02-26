Title: Migrate with Clean and Renewable User Power
Category: DevOps
Tags: devops, service transition
Summary: That time I let users migrate the schema themselves.
Illustration: trunk_board.jpg

Way back in the day of a couple years ago, my team’s product needed a new storage schema for its inventory items, and a migration of the old ones. This was a challenging task. _"Poppycock! Routine!"_, you might say, but the new change was experimental, so a straightforward swap might've been a bad idea. 

*I would, however, enjoy your resurrection of old vocabulary.*

### My Pre-Existing Tried and True Migration Sequence

1. Shut the server down
2. Back up the data
3. Add the new schema
4. Run a ton of SQL cycles to transform the data and save it in the new schema
5. Delete the old schema
6. Start the server back up
7. Hope that you don't need that backup

What usually goes wrong? (Asking for a friend.)

- The SQL times out because you didn’t test on a set that large.
- The server doesn’t start smoothly; it’s still expecting the old schema somewhere.
- You corrupt your new data.
- You corrupt your old data.
- Someone messes up the requirements and now all of a sudden you're immediately shutting down again and rolling back the experimental change that you think will work but hasn't been proven outside of the brains of the individuals that devised it.

*I was especially concerned with that last one.*

That tried-and-true method also takes all of the risk to each environment and crams it right into the first interaction with the system following server restart.

### But wait, there’s more!

It would've taken significant effort to build an automated migration process. The best requirement I could get was that the new data 'looked right'. The most cost effective manual way was to get a user (admittedly, an internal one) to look at each new record, compare it with the old, and hand-verify that it was pretty much correct. If we rolled out the traditional way, the deployment would be coupled to the user!

And even if there was a trusted automatic migration, we still haven't addressed the business risk of the change hitting clients all at once, or the technical risk of performing so much change without the system's feedback.

### Multi-Point Service Transition

I would learn this later, but data migrations fall under ITIL’s Service Transition stage. I like that term; a migration is a change to a service, and its transition to the new state is a non-trivial concern. Also, 'Transition' and 'Migration' are words make me think of a process that takes time, or covers distance. 

I believe that we, as developers, enjoy clean start-and-stop processes. Running production transactions between the migration of your first and last record *feels* like a bad idea. But today’s rapidly-evolving products demand that we think more flexibly. For instance, what if, not only do you deploy multiple times to execute a migration, but the schema migration is a seamless on-demand process which the user doesn't know that they are a part of?

### User-Driven Migrations

One of the new delivery trends is called ‘Dark Deployments’, where a service change is deployed, but its function is enabled by a switch (a Feature Toggle), and it's deployed in the ‘off’ position. This puts your change into the environment without it being released to the user. And given a default-off feature toggle with a user interface, the possibility of a non-development, non-operations, service release, is completely reasonable. Product Owners have always wanted to be the ones to release new services, and this enables them to do so.

For this particular transition, I deployed the new schema to production without migrating anything. I didn't deploy it fully 'dark', though, maybe more like a 'dim deployment'. I simply told the users, through a new menu item, how to make use of the new feature. Every time they modified a record, which didn't happen naturally too often, they were saving records in the new schema. 

*It really sounds like I wasn’t doing my job if I put it that way. Isn't the migration my responsibility? Maybe I should edit this part out of the post.* 

The natural user patterns powered the migration along.

### Compartmentalize Risk

We should think of ways to take on some risk early, but defer the rest until the new service has proven itself in real situations. One strategy for this is to use ‘Canary Deployments’, where an increasingly larger set of servers/records/devices must prove themselves before the deployment continues.

In this case I introduced the new schema to production without removing the old. The old schema already had a UI, and the new one needed a UI, so I grandfathered the old UI and allowed new schema creation with the aforementioned menu selection. 

I was able to watch and record the results of actual users gradually moving data to the new schema. Once that had proved itself, it was time for a larger canary set. The users were internal, so we used verbal communication, rather than automation. We published a list of records that we wanted the users to modify, and made it clear to them what the business reason was. If your users are external, you can still use them to drive canary sets, but you may need to build in limits or round-robin mechanisms.

### Design the Whole Flow

It’s prudent to know what would happen in case of a failure, even a partial failure. This is more than having a simple backup/restore plan. Since we can now stretch the migration over a series of deployments, there are more interactions where things can go wrong. The idea though, is to have fewer things that can go wrong at each stage.

Building this migration required that I clear it with the relevant parties at some point. It’s a lot easier to do that when I’m also answering their questions before they ask them. Mapping out both good and bad scenarios facilitated discussion, and supported my plan. If the new functionality wasn't a success, its impact would be relatively low, and the old data could be swapped back in via the UI.

Both related and unrelated to software: If you communicate negative possibilities without implication, it doesn’t make them any more likely to occur, but it sets relevant expectations, and in my opinion, can build trust.

### Your Success

I have the advantage of applying some new knowledge gained from becoming ITIL Foundation certified and attending the DevOps Enterprise Summit (2016, San Francisco). It reinforces some of the things I did, and makes me interested in taking that concepts further in the future. For example, if the users weren’t internal, how much UX would be necessary to communicate what I could in a product meeting? 

I’m interested in hearing your stories of migration success or failure, and maybe situations where transitioning in non-traditional ways has solved your problems.

Thanks for reading,

Adam Krieger