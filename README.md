# Ferguson & Ferguson — Pedestrian Accident Lawyer Pages

Static site for Ferguson & Ferguson, a personal injury law firm serving Cullman County, Alabama.

## Pages

- **index.html** — Landing page with county overview and links to all city pages
- **pages/** — 12 individual city pages with unique content:
  - Cullman, Hanceville, Good Hope, Baileyton, Berlin, Colony
  - Dodge City, Fairview, Garden City, Holly Pond, South Vinemont, West Point

## Local Preview

Open `index.html` in any browser — no build step or server needed.

## Deploy to GitHub Pages

1. Create a new repository on GitHub
2. Push this folder:
   ```bash
   git init
   git add -A
   git commit -m "Initial commit — 12 city pages"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```
3. Go to **Settings > Pages** in the GitHub repo
4. Set source to **Deploy from a branch** > **main** > **/ (root)**
5. Site will be live at `https://YOUR_USERNAME.github.io/YOUR_REPO/`

## Structure

```
├── index.html
├── css/style.css
├── pages/
│   ├── cullman.html
│   ├── hanceville.html
│   ├── good-hope.html
│   ├── baileyton.html
│   ├── berlin.html
│   ├── colony.html
│   ├── dodge-city.html
│   ├── fairview.html
│   ├── garden-city.html
│   ├── holly-pond.html
│   ├── south-vinemont.html
│   └── west-point.html
├── images/          (placeholder — for future local images)
└── README.md
```
