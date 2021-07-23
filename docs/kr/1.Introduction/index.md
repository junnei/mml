---
layout: default
title: Introduction
lang: kr
lang-ref: introduction
nav_order: 1
description: "Index Page"
permalink: /kr
redirect_from:
  - /
---

# 소개
{: .fs-9 }

이 사이트는 <b>"Mathematics for Machine Learning" 스터디</b>를 진행하면서,
{: .fs-6 .fw-300 }

<b>머신러닝에 대한 지식</b>들을 체계적으로 정리하기 위해 만들어졌습니다.
{: .fs-6 .fw-300 }

[PDF Book](https://mml-book.github.io/book/mml-book.pdf){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 } [Page](https://mml-book.github.io){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## 그룹 멤버

아래는 스터디에 참여하신 분들의 소개입니다.

[Github 레포지토리](https://github.com/junnei/mml/)를 통해 <b>높은 퀄리티의 컨텐츠 제공</b>으로 스터디에 참여해주셨습니다.

<br>

#### Here are contributors of MML Study !

<ul class="list-style-none">
{% for contributor in site.github.contributors %}
  <li class="d-inline-block mr-1">
     <a href="{{ contributor.html_url }}"><img src="{{ contributor.avatar_url }}" width="64" height="64" alt="{{ contributor.login }}"/></a>
  </li>
{% endfor %}
</ul>

---


## 홈페이지 구축에 사용한 오픈소스

이 페이지의 원본 소스는 다음의 저자가 만든 것을 활용한 것입니다. 진심으로 감사드립니다.

- [Just the Docs](http://patrickmarsceill.com) &copy; 2017-2020
- [utteranc.es](https://utteranc.es/) &copy; 2021

---


## 라이센스

[CC BY-NC-SA 4.0 license](https://github.com/junnei/mml/blob/main/LICENSE)를 따릅니다. 다음 사항을 지키면 본 사이트에 있는 저작물들을 별도 허락 없이 자유롭게 사용할 수 있습니다.

- **저작권정보 표시** : 저작물 이용시 본 블로그 주소와 저작자를 표시해야 합니다.
- **비영리** : 이 저작물은 영리 목적으로 이용할 수 없습니다.
- **동일조건 변경 허락** : 이 저작물을 변경(2차 저작물 작성 포함) 가능하나 자신이 만든 저작물에 본 저작물과 같은 이용조건(`CC BY-NC-SA 4.0`)을 적용해야 합니다.
