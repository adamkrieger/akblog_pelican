Title: Fable - The F# Static Site Generator
Category: Projects
Tags: fsharp, blogging
Summary: That time I tried to write a static site generator from scratch.

This project spawned from my need to express my ideas about software development. I often find myself madly scrawling thoughts into my notebook when a partially-formed idea comes to me. Those thoughts remain scrawlings unless I take the time to mull over them, package the good ones, weed the bad ones, and sequence them in a reasonably useful way. I also, to some extent, like showing off. I love what I do, and I love shipping what I do. Blogging is today's natural progression.

<!--more-->

I started by trying out blogspot and WordPress. Both of these solutions seemed alright, but they weren't for me. I considered building a similar type of site myself, but was dissuaded by several articles weighing the pros and cons against static site generators, re: security, hosting options. GitHub supports Jekyll natively, so I gave that product a shot, but found that it didn't work exactly as I'd hoped. Installation involved many more steps than I could really stomach. I also read several articles about the web moving beyond Twitter Bootstrap as the hammer-of-the-month, and I decided to keep pushing forward.

Along the way, I had several thoughts about audience, centered on defining audience and being honest about who is not your audience. Markets are flooded with products that don't define their audience, but why should they, if there's a chance that being honest will put off potential customers? I saw myself in the inverse camp; the group which got frustrated by wasting time on a product that wasn't for me. What it really came down to was that I didn't feel like the intended audience of WordPress, blogspot, or Jekyll. I knew I could make something from scratch, and I knew I could learn something doing it, so I did.

Fable is written in F#, with the help of FParsec. It only runs on a Windows machine, and it only does specific things, but it will get more versatile over time as I require it to be more and more seamless. I'm very sensitive to the importance of day 1 initialization. This is, sadly, one of the areas where Fable is currently falling short. Without knowing the inner workings of the app, there isn't much it will do for you. It's audience is probably, for today at least, made up of one.

Thanks for reading,

Adam Krieger
