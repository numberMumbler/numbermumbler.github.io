---
layout: default
title: "About"
in-menu: true
fa: fa-coffee
---

I'm a senior-level software developer, working mostly on web sites and web services. Currently, my interest is in integrating AI and machine learning into mainstream, line-of-business applications. I'm also grinding my way through a Master's in CS at Georgia Tech.

If you stop me on the street and hand me a laptop, I could bang out code in any of the following languages:

- C#
- Python
- JavaScript
- Clojure
- Rust (well, not yet by hopefully soon)

Here's how to get ahold of me:

{% if site.social.twitter %}
[<i class="fa fa-twitter fa-3x" title="Twitter"></i> @{{ site.social.twitter }}](https://twitter.com/{{ site.social.twitter }}/)
{% endif %}
{% if site.social.github %}
[<i class="fa fa-github fa-3x" title="GitHub"></i> {{ site.social.github }}](https://github.com/{{ site.social.github }}/)
{% endif %}
{% if site.social.linkedin %}
[<i class="fa fa-linkedin-square fa-3x" title="LinkedIn"></i> {{ site.author }}](https://www.linkedin.com/in/{{ site.social.linkedin }})
{% endif %}
{% if site.social.keybase %}
[keybase.io/{{ site.social.keybase }}](https://keybase.io/{{ site.social.keybase }})
{% endif %}