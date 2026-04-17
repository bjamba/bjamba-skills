The thing we got wrong isn't what you'd think. The fanout logic was fine. The retry policy was fine. What we got wrong was assuming our staging environment produced representative load — it didn't, by a factor of about 40x, because staging had never seen the kind of burst traffic the Black Friday queue generates.

Here's the uncomfortable part. We knew, in some back-of-the-mind way, that staging wasn't representative. Three people had said it in the last two quarters. But nobody had said it loudly enough, in the right forum, attached to a concrete risk. So it stayed a background fact. Then it became a Sunday night at 11:47 PM.

What I'd change: require any load-shedding system to run a monthly "representative load" test in production on a shadow path. Not a staging test. A production shadow. The cost of the test is 10x less than the cost of one more Sunday night.
