# Magnetic Earth website

Check the live deployment of the site at https://magneticearth.org/

Use Gitpod to develop on the website:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/MagneticEarth/MagneticEarth.github.io)

## Technical details

The site is built using [Jekyll](https://jekyllrb.com/) and hosted for free using [GitHub Pages](https://pages.github.com/). We use the [Hydeout](https://github.com/fongandrew/hydeout) Jekyll theme.

Changes to the [repository main branch](https://github.com/MagneticEarth/MagneticEarth.github.io) are automatically built and deployed.

## Local development

1. [Install Jekyll](https://jekyllrb.com/docs/installation/)

2. Get the repository and install the environment:
```bash
git clone git@github.com:MagneticEarth/MagneticEarth.github.io.git
cd MagneticEarth.github.io
bundle install
```
(you may need to run `bundle update` if you encounter version conflicts)

3. Serve the website locally:
```bash
bundle exec jekyll serve
```
Browse to [http://127.0.0.1:4000/](http://127.0.0.1:4000/). Make changes and refresh the page to see them.

### Tips for working with Jekyll

- [Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Put images in `pages/figs/` and insert in-line with e.g. `![Swarm spacecraft](/pages/figs/swarm_sc.png)`
- Include html from static files (e.g. html tables) stored in `pages/figs/` with `{{ "{% include_relative figs/table_models.html " }}%}`
- Figures generated from code have their scripts in `pages/figs/src/`. Each declares its own dependencies inline ([PEP 723](https://peps.python.org/pep-0723/)), so regenerating one is just `uv run pages/figs/src/make_igrf_map.py` ([install uv](https://docs.astral.sh/uv/getting-started/installation/)). The resulting image is committed, so this is only needed when the figure itself changes.
