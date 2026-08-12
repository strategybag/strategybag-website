STRATEGY BAG — COMPLETE REBUILD
===============================

This is a clean rebuild from scratch using the approved mockup as the design specification.

INCORPORATED CORRECTIONS
------------------------
- STRATEGY BAG is always capitalized; no LLC.
- Headline: UNLEASH BRAND POWER.
- Hero slogan: BETTER BRANDS. FASTER GROWTH. BIGGER IMPACT.
- Real HTML/CSS for navigation, headline, supporting copy, buttons and slogan.
- Only the rocket/sky/cloud scene is raster artwork.
- No legacy CSS overrides or accumulated hotfixes.
- No horizontal overflow.
- Hero body copy deliberately avoids single-word orphan lines on desktop.
- Representative Experience heading is exactly "REPRESENTATIVE EXPERIENCE".
- Representative logo order:
  1. Heineken
  2. Mobil 1
  3. Esso
  4. Direct Energy
  5. Lactaid
- Final cleaned Direct Energy logo included.
- Clean Heineken logo reused in Selected Experience.
- Three Insights cards always remain visible as fallback content.
- Insights automation only replaces them when all three categories are available.
- Complete site includes: hero, representative experience, capabilities, impact,
  selected experience, insights, about, call-to-action and footer.
- Responsive desktop, tablet and mobile layout.

FILE STRUCTURE
--------------
All page-loaded files are at repository root to avoid path problems:
index.html
styles.css
script.js
config.js
insights.json
update_insights.py
strategy-bag-logo.jpg
favicon.png
rocket-scene.jpg
heineken.png
mobil1.png
esso.png
direct-energy.png
lactaid.png

Only the GitHub Actions workflow is nested:
.github/workflows/refresh-insights.yml

BEFORE PUBLISHING
-----------------
Edit config.js:
- replace YOUR_EMAIL@YOURDOMAIN.COM with your STRATEGY BAG email
- replace https://www.linkedin.com/ with the desired LinkedIn URL

GITHUB PAGES
------------
1. Remove the old website files from the repository.
2. Upload everything in this package, preserving .github/workflows/.
3. Settings > Pages.
4. Source: Deploy from a branch.
5. Branch: main.
6. Folder: /(root).
7. Save.
8. Wait 1–3 minutes.
9. Hard refresh with Ctrl + F5.

AUTOMATED INSIGHTS
------------------
If GitHub Actions cannot write:
Settings > Actions > General > Workflow permissions
Select "Read and write permissions".

GODADDY / EMAIL
---------------
This rebuild does not require changing email-related DNS records.
Do not delete MX, SPF, DKIM or other business-email records.
