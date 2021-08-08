ex)
---
layout: default
title: 제목
lang: kr
lang-ref: title(언어에 따라 바뀌지 않는 고유제목)
parent: 상위 파일 제목
permalink: /kr/[상위_파일_lang-ref]/[2-1]
nav_order: [page_num]
writer: [Github_ID]
---

# [Title]
ex) # 연립 일차 방정식
{: .no_toc }

[Subtitle]
ex) Chapter 1 : Systems of Linear Equations
{: .fs-5 .fw-300 }


{% include writer.html writer=page.writer lang=page.lang %}

---

- 목차
    {: .text-gamma }

    1. TOC
    {:toc}

---

## Title 1

[Contents]

## Title 2

### SubTitle

[Contents]

---

{% include category.html category=page.parent id=[page_num] %}

