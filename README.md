# Magnetic Earth website

Check the live deployment of the site at https://magneticearth.org/

Use Gitpod to develop on the website:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/MagneticEarth/MagneticEarth.github.io)

## Technical details

The site is hosted for free using [GitHub Pages](https://pages.github.com/) and built using [Jekyll](https://jekyllrb.com/), which makes the site easy to maintain and version control, and enabling external contributions through pull requests.
We use the [Hydeout](https://github.com/fongandrew/hydeout) Jekyll theme.
Changes to the [repository main branch](https://github.com/MagneticEarth/MagneticEarth.github.io) are automatically built and deployed.
To test the changes locally is more complicated:

1. [Install Jekyll](https://jekyllrb.com/docs/installation/)
2. Get the repository and make changes:
```bash
git clone https://github.com/MagneticEarth/MagneticEarth.github.io.git
cd MagneticEarth.github.io
...
```
3. Serve the website locally:
```bash
bundle install
bundle exec jekyll serve
```
4. Browse to [http://127.0.0.1:4000/](http://127.0.0.1:4000/)

### Tips for working with Jekyll

- [Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- Put images in `pages/figs/` and insert in-line with e.g. `![Swarm spacecraft](/pages/figs/swarm_sc.png)`
- Include html from static files (e.g. html tables) stored in `pages/figs/` with `{{ "{% include_relative figs/table_models.html " }}%}`
- Follow the [style guide of The Carpentries](https://docs.carpentries.org/topic_folders/communications/guides/adhere-style-guide.html)