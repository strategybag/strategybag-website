STRATEGY BAG V2 — CLEAN PRODUCTION BUILD
========================================

THIS VERSION FIXES THE BLUR PROBLEM
-----------------------------------
The hero is no longer one giant screenshot.

The following are rendered by the browser as real HTML/CSS:
- STRATEGY BAG logo
- navigation
- UNLEASH BRAND POWER
- supporting text
- both hero buttons
- BETTER BRANDS. FASTER GROWTH. BIGGER IMPACT.
- green/blue ribbons

Only the rocket/cloud/sky artwork is a raster image:
assets/rocket-scene.jpg

This keeps the typography and UI crisp on large and high-resolution displays.

BEFORE UPLOADING
----------------
Open config.js and replace:
YOUR_EMAIL@YOURDOMAIN.COM
and
https://www.linkedin.com/

RECOMMENDED GITHUB INSTALL
--------------------------
For the cleanest result, replace the current repository contents with this V2 build.

Upload:
index.html
styles.css
script.js
config.js
insights.json
update_insights.py
assets/ folder
.github/workflows/refresh-insights.yml

GitHub Pages:
Settings > Pages
Source: Deploy from a branch
Branch: main
Folder: /(root)

IMPORTANT
---------
Do not flatten the assets folder in this version.
The HTML/CSS intentionally use assets/... paths.

After committing:
1. Wait 1-3 minutes.
2. Ctrl + F5 on Windows.
3. If needed, test in an Incognito window.

AUTOMATED INSIGHTS
------------------
The workflow updates three categories once per day:
AI + Marketing
Brand Strategy
Innovation

If GitHub Actions cannot write:
Settings > Actions > General > Workflow permissions
Choose Read and write permissions.

EMAIL
-----
This is website hosting only. Do not delete or change your GoDaddy email DNS
records when connecting your custom domain.


FINAL LOGO REVISION
-------------------
This build incorporates the final corrected logos:
Heineken, Mobil 1, Esso, Direct Energy, and Lactaid, in that order.
The final cleaned Direct Energy asset is included.
Selected Experience also uses the clean Heineken logo.
