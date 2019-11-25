---
layout: page
title: About this site
sidebar_link: true
sidebar_sort_order: 99
---

This website is maintained as a voluntary effort and not tied to any particular institution. It is developed with an open source spirit, coordinated through a GitHub organisation - [Magnetic Earth](https://github.com/MagneticEarth).

## Contributing

If you are familiar with GitHub and Jekyll (or even just Markdown), you can make Pull Requests directly with changes to the [content pages](https://github.com/MagneticEarth/MagneticEarth.github.io/tree/master/pages) (we can then test and verify contributions before they go live). You can also just [email us directly](mailto:ashley.smith@ed.ac.uk) with any text/figures you would like added/changed.

## Technical details

The site is hosted for free using [GitHub Pages](https://pages.github.com/) and built using [Jekyll](https://jekyllrb.com/), which makes the site easy to maintain and version control. We use the [Hydeout](https://github.com/fongandrew/hydeout) Jekyll theme. Changes to the [repository master branch](https://github.com/MagneticEarth/MagneticEarth.github.io) are automatically built and deployed; to test the changes locally is a bit more complicated:

1. [Install Jekyll](https://jekyllrb.com/docs/installation/)
2. Get the repository and make changes:
```bash
git clone https://github.com/MagneticEarth/MagneticEarth.github.io.git
cd MagneticEarth.github.io
...
```
3. Serve the website locally:
```bash
jekyll serve --baseurl=''
```
4. Browse to [http://127.0.0.1:4000/](http://127.0.0.1:4000/)

### Tips for working with Jekyll

- [Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Put images in `pages/figs/` and insert in-line with e.g. `![Swarm spacecraft](/pages/figs/swarm_sc.png)`
- Link to other pages like `[About this site]({{ site.baseurl }}{% link pages/about.md %})`
- Include html from static files stored in `pages/figs/` with `{{ "{% include_relative figs/mag_obs_map.html " }}%}`
