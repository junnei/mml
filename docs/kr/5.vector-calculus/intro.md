---
layout: default
title: 벡터 미적분학
lang: kr
lang-ref: vector-calculus
has_children: true
permalink: /kr/vector-calculus
nav_order: 5
writer: jo0n-lab, CSJasper
---


# 벡터 미적분학
{: .no_toc }


Introduction : Vector Calculus
{: .fs-5 .fw-300 }


{% include writer.html writer=page.writer lang=page.lang %}

---

## 벡터 미적분학

**벡터 미적분(Vector Calculus)**은 벡터 차원에서의 미적분을 뜻한다.

일차원의 미분과 달리 벡터의 미분은 전과 후의 차원이 유지되지 않는다.
이 때문에 딥러닝 모델의 gradient descent 에서 벡터의 shape 으로 애먹을 때가 많다.
따라서,
이번 장에서는 벡터의 미분 전과 후의 shape 변화에 대해 알아보고, 이러한 변화가 일어나는 이유를 예제를 통해 살펴보고자 한다.