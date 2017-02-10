Title: This Blog Just Got Shoved (Shove v0.1.0)
Category: Projects
Tags: golang, aws, blogging
Summary: That time I updated my blog to Hugo and wrote a tool to deploy it to S3 with Go.

A firefighter doesn't tie his boots while he's holding the hose. A president doesn't write her speech while she's orating. A Winnipeg Jet doesn't sharpen his skates while splitting the defense. Why the heck was I fiddling around with the S3 management console after I completed a post? Here's a story of the difficulties and triumphs experienced while making sure I don't get slowed down while delivering my content.

<!--more-->

AdamKrieger.ca was originally written using my a personally-developed static site framework: Fable. I was even writing the markdown parser, so developing content was sometimes mixed up with the creation process. If I wanted to include a list in my post, I had to program list parsing into Fable. While sometimes slow, this was really fun, and it taught me a lot about what my product needed in order to be a viable option.

Today, AdamKrieger.ca is generated with [Hugo](https://gohugo.io/). I switched because the availability of something complete (pagination, full markdown, themes) combined with the friction of being both producer and consumer outweighed the learning benefits. There's a bit of a comment on the Agile software process in there, but I'm intentionally leaving it alone for now.

### The Deployment Process Improvement Process

Brief list of steps to roll out a new post after Hugo, but before Shove:

1. Create a new post markdown file
2. Write the post
3. Finalize the post's config values
4. Build the static site
5. Delete the contents of the S3 bucket hosting the site
6. Copy the contents of the output directory back into the S3 bucket via a click-and-drag UI

So that seems like no big deal, but last week after I hit a snag. After deleting the contents of the bucket, there was no easy way to copy the files back in. I don't know if Amazon removed the click-and-drag UI, or if I simply couldn't find it, but there I was with a finished product and step 6 had become this:

- Deploy files
   1. Copy the contents of the root folder into the S3 bucket via the upload dialog
   2. Create all child folders
   3. Repeat these two steps until finished recursively walking the tree

Holy crap. That went from a two minute process to a fifteen minute one that was extremely error-prone. That had to be fixed, and quickly. Luckily, AWS has a few SDKs out there. Since Hugo is written in Go, I decided to use that one. A few tutorials, forum searches, and head-scratchers later, I'd developed 0.1.0 of [Shove](https://github.com/adamkrieger/shove).

Shove will:

1. Recursively walk the provided directory
2. Skip files named '.DS_Store'
3. Skip empty files
4. Print out the file names as they are uploaded to the specified bucket

Here are some things I learned, neat Go libs, and tips and tricks.

### [AWS Go SDK](https://github.com/aws/aws-sdk-go/aws)

* Easy to follow
* Great documentation
* Excellent code samples

### [CodeGangsta's Go CLI framework](https://github.com/codegangsta/cli)

Starting from scratch with this CLI tool allowed Shove to grow organically. Defaults became options, and then global options. Procedures moved from root operations to nested commands. I highly recommend this one. Check out the main func of [shove.go](https://github.com/adamkrieger/shove/blob/master/shove.go) for examples. Also has great documentation.

### [Fatih's 'Color'](https://github.com/fatih/color)

This is an array of functions for printing ANSI-escape colored text to terminal output. Very easy to use. I had a long list of files, and needed to write 'Skipped' in red when that file was getting ignored. It has the power to use standard printf forms.

### Quickfire

1. Uploading a file to S3 via SDK without setting ContentType will default the ContentType to binary/octet-stream. Html files will get downloaded by default and CSS files won't affect style.
2. It's not obvious from looking at the S3 console, but buckets have a region. Uploading files to a bucket without assigning the appropriate region in the config will give you nothing but errors.
3. Moving cohesive funcs out of the main Go file is easily done with a "./pkgname" import. Keep yourself sane by keeping your file sizes down.
4. Creating and deploying blog content is now entirely a command-line exercise. No more GUIs. I feel like I shed a heavy backpack of mouseclicks.

### The Bottom Line

If delivery is the most painful, error prone, or time consuming part of your process, does it have to be? Most of the software projects I've worked with deploy to the same place every time. Even the ones that don't have some pretty standard behaviours. Iron those wrinkles out. Treat your deployment process like a product.

That's all for now. If you have any questions about how I did something or if this utility is three lines of code away from working for you, let me know.
