---
layout: page
title: About this site
sidebar_link: true
sidebar_sort_order: 99
---

This website is maintained as a voluntary effort and not tied to any particular institution. It is developed with an open source spirit, coordinated through a GitHub organisation - [Magnetic Earth](https://github.com/MagneticEarth).

## Contributing

If you have some suggestions, you can email <ashley.smith@ed.ac.uk> or [open an Issue on GitHub](https://github.com/MagneticEarth/MagneticEarth.github.io/issues/new/choose)

If you are familiar with GitHub and Jekyll (or even just Markdown), you can make Pull Requests directly with changes to the [content pages](https://github.com/MagneticEarth/MagneticEarth.github.io/tree/master/pages) (we can then test and verify contributions before they go live).


## Contributors

{% for author in site.data.authors %}
<li>
    <strong>{{ author.name }}</strong>
        {% if author.affiliation %}
        ({{ author.affiliation }})
        {% endif %}<br>|
        {% if author.github %}
        <a class="icon" href="https://github.com/{{ author.github }}">
        GitHub: {{ author.github }}
        </a>|
        {% endif %}
        {% if author.twitter %}
        <a class="icon" href="https://twitter.com/{{ author.twitter }}">
        Twitter: {{ author.twitter }}
        </a>|
        {% endif %}
        {% if author.email %}
        <a class="icon" href="mailto:{{ author.email }}">
        {{ author.email }}
        </a>|
        {% endif %}
        {% if author.website %}
        <a class="icon" href="{{ author.website }}">
        {{ author.website }}
        </a>|
        {% endif %}
</li>
{% endfor %}

