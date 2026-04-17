The multiplayer rewrite you shipped last spring is the kind of project I keep coming back to — not because of the CRDT math, but because of the discipline of shipping it in pieces instead of all at once. The "we moved one document type at a time" thread from your infra lead still lives in a Slack channel at work.

I've spent four years at Acme building infrastructure that nobody asks to see until it breaks. Distributed tracing, Kafka at scale, a homegrown service mesh that we're now replacing with something less homegrown. What I've learned is that the most valuable infra work is the work that stops being dramatic — the incident count going down, the oncall rotation getting boring.

Figma's infra org is at an inflection point where boring is the goal, and I want to help get there. I care about the things that don't make it into a launch post: the fleet that still runs on an older runtime, the deploy pipeline with three exceptions, the dashboard nobody looks at.

First week I'd want to walk through your incident retros from the past quarter — the patterns there tell you more than any architecture diagram.

Happy to talk whenever works.
