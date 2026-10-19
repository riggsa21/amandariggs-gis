GEOSITE INTEL - UNIFIED WEBSITE REFRESH
October 19, 2026

WHAT THIS IS
A full website source update prepared by comparing the older land-intelligence site,
September 2026 multi-service packages, and October 2026 automation packages.

DESIGN / NAVIGATION
Home | Land Intelligence | Workflow Studio | Portfolio | About | Social | Contact
- Contour G used in all primary page headers, footer, and favicon.
- Land/property work and custom workflow tools are separate, equal services.
- Portfolio has clearly separate Property and Automation sections.
- Research/published paper appears on About only, with DOI and author attribution.
- Rowan & Pixel appear only on Social (plus a brief footer navigation link).
- No brand explanation explaining the contour G to visitors.
- Only standard short hyphens in visible prose. No generic G-logo replacements.
- All primary pages share the same header, navigation, colors and footer.
- All included files are FLAT. No assets subfolder is required.

UPLOAD TO GITHUB PAGES REPOSITORY ROOT
1. Download and extract this ZIP locally.
2. Back up your repository before replacing files.
3. Open the repository root containing the current index.html.
4. Upload all files inside this ZIP, not the ZIP itself, and not a containing folder.
5. Commit, then wait for GitHub Pages to deploy.
6. Hard refresh using Ctrl+F5 (or an incognito window).
7. Test Home, Land Intelligence, Workflow Studio, Portfolio, About, Social, Contact,
   several case study pages, the 0 Mills Road PDF, and the Python sample ZIP.
8. Keep any existing legacy assets or maps not included here. They may still have inbound links.

KEY FILES
- geosite-contour-g.png, geosite-contour-logo.png and favicon.png: approved logo assets.
- gsi.css / gsi.js: shared style and mobile menu behavior.
- index.html / land.html / studio.html / portfolio.html / about.html / social.html / contact.html.
- project detail pages and workflow-demo.html.
- GeoSite_0_Mills_Rd_Property_Intelligence_Report.pdf (actual original report).
- GSI_Python_Order_Validation_Sample.zip: working synthetic example with files + code.
- work.html, research.html, services.html and other legacy filenames remain as redirects.

KNOWN FOLLOW-UPS
- Add your confirmed GeoSite Facebook page URL to social.html. It is intentionally not guessed.
- Your master's portfolio pieces, other GIS maps and dashboard screenshots were NOT
  provided in this batch of website ZIPs. We can add them to the property/technical portfolio
  after verifying authorship, data license, and suitability for public display.
- Report preview graphics are actual pages from the included original PDF.
- Other representative aerial/office visuals came from your uploaded older website packages.
- This package does not change your live website until you upload it to GitHub.

COMPATIBILITY
Static HTML, CSS and JS; no framework, build process, server functions, external fonts,
or API keys. Synthetic Python sample runs with Python 3 standard library.

SUGGESTED COMMIT MESSAGE
Unify GeoSite land intelligence and workflow studio with contour G branding
