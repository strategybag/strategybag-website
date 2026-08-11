STRATEGY BAG HEADER-ONLY FIX v2
===============================

This revision fixes the exact problems shown in your screenshot:

1. The hero image is no longer forced into a tall 570px box.
2. The rocket image uses a wide crop and matching aspect ratio, so it no longer zooms in.
3. The right-side BETTER BRANDS / FASTER GROWTH / BIGGER IMPACT text stays visible.
4. The header container no longer creates horizontal overflow.
5. The LET'S TALK button stays inside the viewport.
6. The left headline is scaled down to match the approved design more closely.
7. The eyebrow line stays on one line on desktop.

FILES
-----
index.html
styles.css
strategy-bag-logo.jpg
rocket-hero-wide.png

HOW TO APPLY
------------
If you only want to change your existing site's header/hero:
- replace your existing header + hero HTML with the blocks from index.html
- replace the existing header/hero CSS with the CSS in styles.css
- upload rocket-hero-wide.png beside index.html
- keep all other sections of your current site unchanged

Then commit to GitHub Pages and hard refresh with Ctrl+F5.
