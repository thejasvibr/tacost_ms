---
title: 'tacost: Test and simulate the accuracy of acoustic tracking systems'
tags:
  - Python
  - acoustics
  - bioacoustics
  - sound
  - acoustic tracking
authors:
  - name: Thejasvi Beleyur
    orcid: 0000-0001-5360-4383
    affiliation: "1"

affiliations:
 - name: Acoustic and Functional Ecology, Max Planck Institute for Ornithology, Seewiesen, Germany
   index: 1
date: July 2020
bibliography: references.bib
---

# Introduction
Acoustic tracking is a common method used to study vocalising animals such as birds and echolocating animals like bats and cetaceans [@suzuki2017harkbird]


# Motivation
The design of `tacost` focusses on a reproducible and user-friendly method to generate WAV files that can be used 
to test acoustic tracking. 

# Installation 
`tacost` is hosted on the Python Package Index (PyPI) and can be installed with the following command:

```python 
pip install tacost
```

# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Fenced code blocks are rendered with syntax highlighting:
```python
for n in range(10):
    yield f(n)
```	

# Acknowledgements
This work was supported by a doctoral fellowship from the German Academic Exchange Service (DAAD) and the International Max Planck Research School for Organismal Biology. 
I would like to thank Lena De Framond for running test runs of the package.

# References