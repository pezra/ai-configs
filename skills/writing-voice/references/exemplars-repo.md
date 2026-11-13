# README exemplars

Passages from Peter's READMEs. Don't reuse these sentences. Read for length, tone and how little commentary surrounds the code.


From Peter's edit of the MeetingBuzz README, the closest model for an app:

> MeetingBuzz vibrates the phone shortly before any calendar event that involves another person, and it keeps vibrating until the alarm is dismissed.

> An event gets a buzz if someone other than you is on its attendee list. Conference rooms and projectors are not people, as far as MeetingBuzz is concerned. All-day events, canceled events and events you have declined are skipped.

> The one trigger you control is Shortcuts. The app provides a **Refresh MeetingBuzz** action, and i recommend a personal automation that runs it a few times a day.

From phoenix_cowboy_logging, a whole opening:

> Add logging of request acceptance and parse errors that happen at the cowboy level to your Phoenix app.

From filequeue:

> ...is a simple file based queue written in Ruby that uses the Ruby `File` class in standard library to push and pop items into a queue. It's not web scale but is nice for lightweight async queuing apps.

From hash-selector, setting up an example and explaining the failure case:

> Consider a complex and deeply nested hash such as the following:

> Say we want to find the user name of legacy db but if we do not find it use a default value. With just the basic hash behavior this can be rather onerous.

> If the location specified by a `HashSelector` does not exist in the hash it will raise a `KeyError` unless a block is provided.

From hal-client, tutorial "we":

> Once we have a representation we will want to navigate its links. This can be accomplished using the `#related` method.

From parallel-each, the most opinion a README carries:

> I/O bound work is where `#p_each` will really shine.
