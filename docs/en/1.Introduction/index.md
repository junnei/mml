---
layout: default
title: Introduction
lang: en
lang-ref: introduction
nav_order: 1
description: "Index Page"
permalink: /en
---

# Introducing
{: .fs-9 }

This site is designed to organize knowledge of machine learning while conducting the "Mathematics for Machine Learning" study.
{: .fs-6 .fw-600 }


[PDF Book](https://mml-book.github.io/book/mml-book.pdf){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 } [Page](https://mml-book.github.io){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## Group Member

Here is an introduction of the people who participated in the study.

Participated in this study with <b>high-quality contents : [[Github Repository]](https://github.com/junnei/mml/)</b>

<br>

#### Here are contributors of MML Study !

<ul class="list-style-none">
{% for contributor in site.github.collaborators %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="64" height="64" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>

---


## Open Source Used

This page is based on the following author's creation. Heartily thank you.

- [Just the Docs](http://patrickmarsceill.com) &copy; 2017-2020
- [utteranc.es](https://utteranc.es/) &copy; 2021

---


## License

[CC BY-NC-SA 4.0 license](https://github.com/junnei/mml/blob/main/LICENSE). Subject to the this copyright.

You can freely use the works on this site without permission if you observe the following:

- **Attribution** : You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **NonCommercial** : You may not use the material for commercial purposes.
- **ShareAlike** : If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original(`CC BY-NC-SA 4.0`).