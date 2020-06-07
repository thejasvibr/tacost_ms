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
date: 07 June 2020
bibliography: references.bib
---

# Introduction
Acoustic tracking is a common method used to study vocalising animals such as birds and echolocating animals like bats and cetaceans [@suzuki2017harkbird;aubauer1996acoustical;mohl2000sperm;Goerlitz2010;Hugel2017].

The localisation accuracy of an acoustic tracking system depends on a variety  of what I define as 'internal' and 'external' factors. Internal factors include aspects such as microphone array geometry,
localisation algorithms to detect signals of interest and the mathematical formulations used to localise sounds once the signals have been detected (time-of-arrival, time-of-arrival-difference) `REFS`. External 
factors include aspects related to the actual signal itself, ie. signal-to-noise ratio, and emitted sound. A microphone array's localisation accuracy may not be uniform over 3D space. This accuracy 
is independent of the actual signal and recording conditions of the input data, but rather dependent on the mathematical formulations used to calculate source sound position. While the accuracy of a few 
microphone array configurations have been experimental characterised `REFS`, the accuracy of custom and novel array configurations is a manually-intensive task. The intrinsic accuracy of such arrays can be 
relatively quickly characterised by the use of simulated audio files with sounds simulated to arrive from various positions. `tacost` provides an easy to use solution to test the accuracy of acoustic tracking 
systems, by allowing the simulation of multiple factors relevant to localication accuracy. 

# Motivation and design
Generating simulated audio for a set of source sounds and a given array configuration is a relatively simple task. However, to this author's knowledge, there 
are no publicly available, tested and documented packages published to date. Codebases that are publicly available have the advantage of being used by a larger user-base and can thus 
benefit from bug discoveries much faster than in-house or one-time use scripts `REFS`.  `tacost` aims to provide a robust and well-documented software workflow with user [@Taschuk2016] 
and developer friendly documentation [hosted online](https://tacost.readthedocs.io/en/latest/) and in the code itself. `tacost` contributes to the 
Python scientific ecosystem and hopes to promote the growth of acoustics and bioacoustic research in open-source languages like Python. 

The design of `tacost` focusses on a reproducible and user-friendly method @[Wilson2012] to generate WAV files that form the input for acoustic tracking softwares. Users may interact with `tacost` through custom-written Python scripts
by calling it as a Python package with ```import tacost``` or in the 'no-coding' mode. The 'no-coding' mode is based around a parameter file which is used to specify various parts of the actual simulated WAV file to be created.
Through the parameter file the user can define the emitted sound, positions, inter-sound-intervals, sampling rate and other relevant variables to customise the output WAV file. 

# Installation
`tacost` is hosted on the Python Package Index (PyPI) and can be installed with the following command:

```python 
pip install tacost
```

or by cloning the source repository (see repository hyperlink in paper), navigating to the repository and installing the package with ```pip install .```. 

# Examples 

## Using `tacost` in a custom-written script
In this example, a 4-channel array is tested 

# Acknowledgements
This work was supported by a doctoral fellowship from the German Academic Exchange Service (DAAD) and the International Max Planck Research School for Organismal Biology. 
I would like to thank Lena De Framond for running test runs of the package.

# References