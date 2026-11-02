# EV Market Intelligence

An interactive Electric Vehicle (EV) market analytics website built with **Python Flask** and **Tableau Public**. The site brings together a market overview dashboard, a performance analysis dashboard and an EV market analysis story.

## Live Tableau visualizations

- [Market Overview](https://public.tableau.com/app/profile/shanvi.bansal/viz/tableau_17934611427150/MarketOverview?publish=yes)
- [Performance Analysis](https://public.tableau.com/app/profile/shanvi.bansal/viz/tableau_17934611427150/PerformanceAnalysis?publish=yes)
- [EV Market Analysis Story](https://public.tableau.com/app/profile/shanvi.bansal/viz/tableau_17934611427150/EVMarketAnalysisStory?publish=yes&showOnboarding=true)

## Website pages

| Page | Local route | Purpose |
|---|---|---|
| Home | `/` | Project introduction and navigation |
| Market Overview | `/market-overview` | Embedded Tableau market overview |
| Performance Analysis | `/performance-analysis` | Embedded Tableau performance dashboard |
| Story | `/story` | Embedded Tableau story |

## Technology stack

- Python and Flask
- Tableau Public
- HTML5 and CSS3
- Gunicorn
- GitHub
- Render

## Run locally

1. Install Python 3.10 or newer.
2. Clone or download this repository.
3. Open a terminal in the project root (the folder containing `app.py`).
4. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

6. Start the Flask development server:

   ```bash
   python app.py
   ```

7. Open http://127.0.0.1:5000 in your browser.

## Deploy on Render

1. Push the project to a GitHub repository.
2. In Render, choose **New → Web Service** and connect the repository.
3. Set the runtime to Python.
4. Set the build command to `pip install -r requirements.txt`.
5. Set the start command to `gunicorn app:app`.
6. Deploy. Render will provide a public URL.

The included `render.yaml` and `Procfile` provide the same deployment commands.

## Run

https://ev-3hi4.onrender.com/

## Project structure

```text
ev-market-intelligence/
├── app.py
├── config.py
├── requirements.txt
├── Procfile
├── render.yaml
├── README.md
├── .gitignore
├── templates/
│   ├── base.html
│   ├── index.html
│   └── tableau.html
└── static/
    └── css/
        └── style.css
```

## Screenshots

Add screenshots of the deployed homepage and the Tableau pages here after deployment.

```markdown
![EV Market Intelligence homepage](screenshots/homepage.png)
![Market Overview dashboard](screenshots/market-overview.png)
![Performance Analysis dashboard](screenshots/performance-analysis.png)
```

## Notes

- Tableau visualizations are embedded from Tableau Public. They require an internet connection.
- If an embedded view does not load, use the **Open in Tableau Public** link on that page.
- The project intentionally does not claim dataset sizes, market statistics or dashboard findings that have not been independently verified. Add those details after checking the workbook and source data.

## Credits

Tableau visualizations are linked to the Tableau Public profile and workbook supplied for this project.
