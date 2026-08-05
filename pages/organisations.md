---
layout: page
title: Organisations & resources
sidebar_link: true
sidebar_sort_order: 98
---

<div id="resources-embed" style="position:relative;">
  <button id="resources-embed-toggle" title="Expand" style="position:absolute; top:10px; right:10px; z-index:1001; width:44px; height:44px; display:flex; align-items:center; justify-content:center; cursor:pointer; border:1px solid #999; border-radius:6px; background:#fff; box-shadow:0 1px 4px rgba(0,0,0,0.25);">
    <svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#333" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3M16 3h3a2 2 0 0 1 2 2v3M21 16v3a2 2 0 0 1-2 2h-3M8 21H5a2 2 0 0 1-2-2v-3"/></svg>
  </button>
  <iframe id="resources-embed-iframe" src="https://magneticearth.org/resources/index.html" style="width:100%; height:1400px; border:none; display:block;" title="Organisations & resources"></iframe>
</div>

<script>
(function () {
  var expandIcon = '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#333" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3H5a2 2 0 0 0-2 2v3M16 3h3a2 2 0 0 1 2 2v3M21 16v3a2 2 0 0 1-2 2h-3M8 21H5a2 2 0 0 1-2-2v-3"/></svg>';
  var collapseIcon = '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="#333" stroke-width="2.5" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>';

  var wrap = document.getElementById('resources-embed');
  var btn = document.getElementById('resources-embed-toggle');
  var frame = document.getElementById('resources-embed-iframe');

  btn.addEventListener('click', function () {
    var expanded = wrap.classList.toggle('expanded');
    if (expanded) {
      wrap.style.cssText = 'position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:1000; background:#fff; margin:0;';
      frame.style.height = '100%';
      document.body.style.overflow = 'hidden';
    } else {
      wrap.style.cssText = 'position:relative;';
      frame.style.height = '1400px';
      document.body.style.overflow = '';
    }
    btn.innerHTML = expanded ? collapseIcon : expandIcon;
    btn.title = expanded ? 'Collapse' : 'Expand';
  });
})();
</script>
