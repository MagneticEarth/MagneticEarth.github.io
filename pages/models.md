---
layout: page
title: Geomagnetic models
sidebar_link: true
sidebar_sort_order: 4
---

[TODO: intro to models, spherical harmonics; interactive visualisation?; add links for Swarm model descriptions, and how to access and evaluate them]

Contents:
- table of contents
{:toc}

## Overview of models

There are many models which aim to describe the global geomagnetic field (or one of the sources within it).
The field itself is complex so naturally there are many decisions to be made when creating a model:

- what magnetic source(s) are we interested in?
- what data should we use and how should we "clean" them?
- how should we parameterise the model? ...

This situation has led to a range of models with different applications and varying levels of cross-compatibility.
The following table lists most of the contemporary models available which are applicable near to Earth (between Earth's surface and at low- to mid-Earth orbit).
If you are new to this, then a good place to start is the IGRF, the International Geomagnetic Reference Field, which is collaboratively produced by the scientific community to give a reasonable estimate of the "main field" (i.e. that which is mostly produced by the core).

{% include_relative figs/table_models.html %}

**\*** *Whereas the other items in this list are smoothly varying models that provide a prediction of the field everywhere, these crustal **grids** are maps of discrete values which are compiled (and cross-calibrated) from a large number of individual surveys.*

### Other lists of models
- <https://www.space.dtu.dk/english/research/scientific_data_and_models/magnetic_field_models>
- <https://geomag.colorado.edu/geomagnetic-and-electric-field-models.html>
- <http://geomag.org/models/index.html>
- <http://www.geomag.bgs.ac.uk/research/modelling/modelling.html>

## Swarm models

A number of models are produced within the framework of the Swarm mission.
These "Level 2" data products themselves are described in the [official documentation](https://earth.esa.int/web/guest/missions/esa-eo-missions/swarm/data-handbook/level-2-product-definitions) as well as in scientific papers.
The models follow a naming convention according to the physical source they target and the operational processing chain that produces them:

| Model of the ...   | C: Comprehensive | D: Dedicated | F: Fast-track |
|--------------------|------------------|--------------|---------------|
| MCO: Core          | &#10004; 	      | &#10004; 	   | &#10004; 	   |
| MMA: Magnetosphere | &#10004; 	      | - 	         | &#10004; 	   |
| MIO: Ionosphere    | &#10004; 	      | &#10004; 	   | - 	           |
| MLI: Lithosphere   | &#10004; 	      | &#10004; 	   | -        	   |

The *comprehensive* inversion chain aims to co-estimate the four sources together.
*Dedicated* inversions attempt to filter out the effect of other sources and make a better isolation of a particular source.
The *fast-track* products deliver an estimate of the field more rapidly than the other products, so they are available sooner but are less accurate.

{% include_relative figs/table_models_swarm.html %}
