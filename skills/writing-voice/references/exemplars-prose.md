# Prose exemplars

Passages from barelyenough.org, chosen to show rhythm and stance. Obvious typos are corrected, because the skill copies the voice and not the slips. Don't reuse these sentences in new writing. Read for how they move.

## Contents

- Stating a disagreement
- Turning a claim into reasoning
- Telling the story of a change of mind
- Practical advice
- War story, with a playful structure
- Digressing and returning
- Hedged, open-ended thinking
- Personal and travel
- Short posts

## Stating a disagreement

From "Is ruby immature?" (2010):

> A friend of mine recently described why he feels ruby is immature. I, of course, disagree with him. There is much in ruby that could be improved, but the issues he raised are a) intentional design choices or b) weaknesses in specific applications built in ruby. Neither of those scenarios can be fairly described as immaturity in the language, or the community using the language.

> Following these principles does result in some rough edges occasionally, but the benefits are worth the trade. The 80% solution is how Unix succeeded. An 80% solution today is better than a 100% solution 3 months from now. (As long as you can improve it when needed.) We always have releases to get to, after all.

From "When to use exceptions" (2007, earlier style, but it shows the directness and the handling of an opponent's words):

> Exceptions are not about “exceptional situations”, whatever that means. They are a way for methods to tell their caller that it was not able to do what the caller asked it to do.

> Either way my advice is: Do *not* use `nil` as a way to indicate that the object was unable to perform the requested operation, that is the job of exceptions. If you see a method that returns `nil` demand an affirmative defense for that behavior because it is often incorrect.

## Turning a claim into reasoning

From "Instant legacy status" (2009). The opener is the punchline, and the title is its subject:

> That is what you gain when you allow more than one module of software to access any single database. Any integration database confers legacy status on all modules that access it.

> So far not so good, but that was the good part. The really disastrous part is that by integrating at the database level you are required to introduce staggering levels of Connascence of Algorithm.

> After a while the cost of change will become so high that only improvements that provide huge value to the business will be worth the cost. For weak, undisciplined teams this will happen very rapidly. For strong, smart and highly disciplined teams it will take a bit longer, but it will happen.

From "Embedding" (2012). The appeal first, then the cost:

> This approach is very appealing. All the data needed to display or operate on an invoice is right there at our fingertips which nicely manages the number of requests that need to be made. The data is also arranged in a logical way that makes sense to our human brains.

> For all of its upsides, the downsides to this approach are substantial. The biggest issue, to my mind, is that it limits our ability to evolve this message over time.

> **Embedding one representation inside another is an optimization. Be sure it is not premature before proceeding.**

> Annoyingly, sometimes optimizations really are required.

## Telling the story of a change of mind

From "Why i don't love schemas" (2018), the best single model for the current voice:

> Once, long ago, i thought that schemas were great and that they could provide much value. Schemas hold the promise of declaratively and unambiguously defining message formats. Many improvements would be “easy” once such a definition was available.

> At every turn i found the returns on investment disappointing. Schema languages are hard for humans to write and even harder to interpret. They are usually unable to express many real world constraints (you can only have that radio with this trim package, you can only have that engine if you are not in California, etc). High quality documentation is super hard even with a schema. Generation from schema solves the easy part of documentation, explaining why the reader should care is the hard part.

> JSON emerged primarily as a reaction to the complexity of XML. However, XML didn’t start out complex, it accreted the complexity over time. Unsurprisingly the cycle is repeating. JSON schema is a thing and seems to be gaining popularity. It is probably a fool's errand to try stemming the tide but i’m going to try anyway.

> What would it take for schemas to be net positive? Only a couple of really hard things.

> Designing schemas for humans and avoiding the One True Schema are both really hard. And, unfortunately, i doubt our ability to reach consensus and execute on them.

## Practical advice

From "Componentizing monoliths" (2017):

> Micro-service architectures are all the rage these days. Let’s say, totally hypothetically, that you already have a large code base that has all the pathologies we have come to expect from monoliths.

> That is a great goal, but how do you get from a huge, highly coupled, monolith to a constellation of cooperating components? Most “efforts” to modularize monolithic software are abandoned at about the time someone serious considers that question. That is, before the effort even starts.

> Decomposing a significant monolith *will* take time. It took tens or hundreds of man years to build the monolith. Breaking it up is going to take a while. Accept it. Plan for it.

> This is just a rule of thumb. Any real system will have situations that simply don’t allow for the preferred data locality for all operations. Engineering is all about trade offs.

> The key is to understand the existing code base enough to see seams in it that could be used to cleave off a bit of functionality. This functionality will likely be the best factored and designed part of the monolith. It is ironic that the easiest part to remove is the best part, but c’est la vie.

> Basically, component extraction is just normal, every day incremental refactoring, but in the large.

## War story, with a playful structure

From "mod_proxy_balancer is a two timing hussy" (2008). The section headings are "Maybe Monogamy", "Broken Trust" and "Rebound":

> A quick scan through the Apache docs reveals the `max` parameter for ProxyPass. Sweet, a nice simple solution.

> Unfortunately, upon deploying the configuration above into a high load environment it will rapidly become obvious that it does not solve the problem.

> So now you know that you cannot trust Apache’s mod_proxy_balancer. You can use Pen. It is easy to configure, fast and it works great. Oh, except for the fact that it does not queue requests if all the backends are busy.

> It seems that HAProxy might be the best choice. I’ll let you know how it works out.

## Digressing and returning

From "Instant legacy status" (2009). The headings are "Pardon me while i digress…" and "Back on point":

> I recently attended Mountain West RubyConf. While there i had the pleasure of hearing a brilliant talk by Jim Weirich about connascence in software.

> While we are on this point, remember that if your mad data modeling skills did manage to avoid significant Connascence of Meaning you did it by adding significant amounts of Connascence of Name. That is what a lookup-table is.

## Hedged, open-ended thinking

From "Nucleic teams" (2009):

> I am not sure if this structure and the reason behind it are good, or bad, for the Rails community as a whole. The nucleic team model might turn out to be a competitive advantage in itself because it embodies the benefits of both internal and external development teams. On the other hand, it is bound to be a bit off putting for organizations that are not used to it.

From "How i judge software engineers" (2018):

> My kid’s teachers routinely provide rubrics for assignments. At first blush, rubrics are tools to make grading an assessment easier. They are effective in that role. They turn out to be at least as effective at communicating expectations.

> Recently i developed a rubric to help me judge the performance of engineers (it was review season yet again). The engineers on my team have appreciated the transparency and clarity this tool provides. Hopefully, it will be helpful to others.

## Personal and travel

From "South America - Santiago (and Atlanta)" (2022):

> I was booked to fly from Denver to Santiago with a short layover in Atlanta. However, my flight from Denver was slightly delayed so i missed the Santiago leg and had to spend 24 hours in Atlanta (there is only one flight to Santiago per day). This turned out to be really nice.

> After that i headed to the nearby Piedmont Park. There was a Jazz festival happening so I lazed about the park listening to Joe Alterman and some other artists that escape my memory until it was time to head to the airport. All in all it was a great way to spend an unexpected visit to Atlanta.

> Tomorrow we are off to explore other parts of Chile.

From a 2014 post:

> While at the national portrait gallery Audrey was looking pretty underwhelmed by all the beautiful portraits. All of a sudden she perks up and says “look, there’s a picture of a dog!” and scoots off across the room.

## Short posts

> Any one know of a good javascript bdd/spec framework that works on rhino? So far i am underwhelmed.

> `rvm use {whatever}` does not work if you pipe the output. As it turns out neither does `export {var}={value}`.

> Seeing Ben Folds with my favorite daughter.

> I chose better than my daughter.
