GEOSITE INTEL WEBSITE — FLAT ROOT UPLOAD FIX (19 OCTOBER 2026)
============================================================

WHY THE IMAGES WERE MISSING
The previous package referred to files inside /assets/.
When GitHub's browser uploader is open in the repository root and you upload
files chosen *from inside* a local assets folder, GitHub can place the chosen
individual files in the REPOSITORY ROOT instead. The HTML still looked for
/assets/workflow-studio.webp etc., so the images could not load.

THIS REPAIR PACKAGE HAS NO ASSETS FOLDER.
Every file belongs directly alongside index.html in the website repository.

UPLOAD ALL EIGHT (8) FILES BELOW TO THE REPOSITORY ROOT:
  index.html                  REPLACE
  rowan-and-pixel.html       ADD or REPLACE
  data-access.html           ADD or REPLACE
  gsi-refresh.css            ADD or REPLACE
  gsi-refresh.js             ADD or REPLACE
  rowan-pixel.webp           ADD or REPLACE
  workflow-studio.webp       ADD or REPLACE
  topography.svg             ADD or REPLACE

IMPORTANT: Do NOT upload this ZIP as-is to GitHub Pages.
Extract it first; select these 8 files together using GitHub > Add file >
Upload files in your repository's ROOT (same level as index.html).
You should see the image filenames directly below index.html, NOT inside assets/.

Do not delete or replace services.html, examples.html, work.html,
research.html, about.html, business-automation.html, other existing
images, videos, scripts, PDFs, or site.css.

SUGGESTED COMMIT MESSAGE
Fix homepage and Rowan & Pixel image references for GitHub Pages

VERIFY AFTER DEPLOYMENT (use Ctrl+Shift+R / Ctrl+F5 if cached)
  https://geositeintel.com/
  https://geositeintel.com/rowan-and-pixel.html
  https://geositeintel.com/data-access.html
  https://geositeintel.com/rowan-pixel.webp
  https://geositeintel.com/workflow-studio.webp
  https://geositeintel.com/topography.svg

If a direct image URL opens, but the page still displays an empty image area,
clear the cache and inspect the filename spelling and capitalization.
If GitHub Pages is not showing updated files, check the repository's
Settings > Pages branch and folder are the same as the place you uploaded.

CHANGES RELATIVE TO PREVIOUS ZIP
- All image and background references are now ROOT-relative.
- Social preview images now point to root URLs.
- CSS/JS links have a refreshed version parameter to help bust caches.
- No other existing website page or asset needs to change.
- Sitemap additions (if not already made):
  https://geositeintel.com/rowan-and-pixel.html
  https://geositeintel.com/data-access.html

No licensed third-party GIS data are bundled in this update.
