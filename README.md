# Thomann UK ST-Style Guitars Dynamic Web Scraper

<img width="2696" height="1558" alt="Screenshot 2026-02-03 154051" src="https://github.com/user-attachments/assets/3bea8ac1-044a-4195-8c70-f4fb2bac3e7c" />



The objective was to reliably extract structured ST-style guitar product data despite challenges such as cookie consent overlays, client-side pagination driven by UI interactions rather than predictable URL parameters, and heavy JavaScript rendering.

I built a Python scraper using Playwright that simulates real browser behavior to extract ST-style guitar listings from Thomann UK.

### The scraper:
	•	Automatically handles cookie consent interruptions
	•	Navigates client-side pagination driven by UI interactions
	•	Waits for dynamic product content to fully render
	•	Extracts product data across pages

### Tech Stack
	•	Python
	•	Playwright (Sync API)
	•	Chromium (headless browser automation)
	•	CSS selectors & DOM evaluation
	•	Controlled wait strategies for JS-rendered content
