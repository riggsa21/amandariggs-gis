GEOSITE INTEL - IMAGE SIZE REFINEMENT (OCTOBER 19, 2026)
=======================================================

WHAT THIS FIXES
- Home: Rowan & Pixel portrait illustration is reduced and centered to a
  maximum of 310px wide on desktop (265px on phones).
- Home: Automation Studio banner is limited to 405px on desktop (330px on phones).
- Rowan & Pixel series page: illustration is capped at 345px wide (275px on phones).
- Corrected width/height metadata for the panoramic Automation Studio image.
- Images remain proportional and are not cropped. Text stays prominent.
- These adjustments are responsive for desktop, tablet, and mobile.
- Revisions include a new CSS URL parameter to avoid showing cached old styles.

UPLOAD METHOD
1. Extract this ZIP on your computer.
2. Open your GitHub Pages website repository. Open the same ROOT directory that
   contains the live index.html file.
3. Upload the following four updated files from the extracted folder:
       index.html
       rowan-and-pixel.html
       data-access.html
       gsi-refresh.css
   Replace files with those exact names and commit your update.

Only four files are needed if you successfully uploaded the images before.
The ZIP also includes gsi-refresh.js, rowan-pixel.webp, workflow-studio.webp,
and topography.svg in case you prefer to upload all eight again.
All files in this ZIP are FLAT / at the repository ROOT (no assets/ folder).

Preserve: services.html, work.html, examples.html, research.html, about.html,
business-automation.html, and other existing files. Do not delete the old
assets/ folder because other pages may use it.

SUGGESTED COMMIT MESSAGE
Reduce homepage and Rowan & Pixel imagery sizes

VERIFY
https://geositeintel.com/
https://geositeintel.com/rowan-and-pixel.html
On Windows force reload with Ctrl+F5 if the images still appear at old sizes.

The ZIP passed file/reference checks. Live visual rendering must be checked after the upload.
