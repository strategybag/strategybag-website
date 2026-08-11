STRATEGY BAG — PRODUCTION WEBSITE
=================================

APPROVED BRAND DIRECTION
------------------------
Headline: UNLEASH BRAND POWER
Hero message: BETTER BRANDS. FASTER GROWTH. BIGGER IMPACT.
Brand name: STRATEGY BAG (always capitalized; no LLC)
Representative logo order:
1. Heineken
2. Mobil 1
3. Esso
4. Direct Energy
5. Lactaid

WHAT IS INCLUDED
----------------
index.html                 Main website
styles.css                 Responsive production styling
script.js                  Navigation, contact links and Insights loader
config.js                  Your email and LinkedIn settings
insights.json              Current homepage insight cards
assets/                    STRATEGY BAG logo, hero and brand images
scripts/update_insights.py Daily automated article selector
.github/workflows/         GitHub Actions automation

STEP 1 — PERSONALIZE TWO LINKS
------------------------------
Open config.js in Notepad.

Replace:
YOUR_EMAIL@YOURDOMAIN.COM
with your actual STRATEGY BAG email address.

Replace:
https://www.linkedin.com/
with your desired LinkedIn page/profile URL.

Save config.js.

STEP 2 — TEST ON YOUR COMPUTER
------------------------------
You can double-click index.html to inspect the layout.

Because browsers often block local file requests, the dynamic Insights cards
may show the built-in placeholder when opened directly from your computer.
They will work normally after the site is hosted.

FREE HOSTING: GITHUB PAGES
--------------------------
1. Go to github.com and create/sign in to a free GitHub account.
2. Click "+" > New repository.
3. Name it: strategy-bag-site
4. Set it to Public.
5. Click Create repository.
6. Upload EVERYTHING inside this STRATEGY_BAG_Production folder.
   Be sure the .github folder is included.
7. Commit the uploaded files.
8. Open repository Settings > Pages.
9. Under "Build and deployment":
      Source: Deploy from a branch
      Branch: main
      Folder: /(root)
10. Click Save.

GitHub will publish the temporary site at an address similar to:
https://YOUR-GITHUB-USERNAME.github.io/strategy-bag-site/

CONNECT YOUR GODADDY DOMAIN
---------------------------
IMPORTANT: You use email on this domain. Do NOT delete MX, TXT, SPF, DKIM,
Microsoft 365, Google Workspace, or other email-related DNS records.

1. First confirm the GitHub Pages temporary site works.
2. In GitHub go to Settings > Pages > Custom domain.
3. Enter your domain, for example:
      strategybag.com
4. GitHub will tell you the custom-domain configuration.

For an apex/root domain, GitHub Pages currently documents these A records:
      185.199.108.153
      185.199.109.153
      185.199.110.153
      185.199.111.153

For www, use a CNAME pointing to:
      YOUR-GITHUB-USERNAME.github.io

5. In GoDaddy go to Domain > DNS > Manage DNS.
6. Replace ONLY the website A record for @ that currently points to GoDaddy
   hosting/parking with GitHub's A records.
7. Set or update the www CNAME to your GitHub Pages hostname.
8. Leave all email-related records untouched.
9. Return to GitHub Pages and enable "Enforce HTTPS" after DNS verification.

AUTOMATIC INSIGHTS
------------------
A GitHub Action is included. It checks once per day for current articles
covering:
- AI + marketing
- brand strategy / brand value
- innovation / commercialization

It updates insights.json and republishes the site automatically.

After upload:
1. Go to GitHub repository > Actions.
2. Open "Refresh STRATEGY BAG Insights".
3. Click "Run workflow" once to test it.
4. If GitHub reports a permissions error:
   Settings > Actions > General > Workflow permissions
   Select "Read and write permissions", then save and run it again.

The workflow requires no paid API.

NOTES
-----
- The five logos in the Representative Experience section are the exact five
  requested and appear in the approved order.
- The site is fully responsive for desktop, tablet and mobile.
- Footer copyright year updates automatically.
- The hero uses the approved rocket direction and approved headline.
- Do not cancel your email subscription when moving website hosting.
