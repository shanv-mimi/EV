PROJECT = {
    "name": "EV Market Intelligence",
    "tagline": "Powering the shift. Understanding the market.",
    "description": (
        "Explore the electric vehicle landscape through interactive market "
        "overview, performance analysis and visual storytelling."
    ),
    "market_url": "https://public.tableau.com/views/tableau_17934611427150/MarketOverview?:showVizHome=no&:embed=true",
    "performance_url": "https://public.tableau.com/views/tableau_17934611427150/PerformanceAnalysis?:showVizHome=no&:embed=true",
    "story_url": "https://public.tableau.com/views/tableau_17934611427150/EVMarketAnalysisStory?:showVizHome=no&:embed=true",
    "market_public_url": "https://public.tableau.com/app/profile/shanvi.bansal/viz/tableau_17934611427150/MarketOverview?publish=yes",
    "performance_public_url": "https://public.tableau.com/app/profile/shanvi.bansal/viz/tableau_17934611427150/PerformanceAnalysis?publish=yes",
    "story_public_url": "https://public.tableau.com/app/profile/shanvi.bansal/viz/tableau_17934611427150/EVMarketAnalysisStory?publish=yes&showOnboarding=true",
    "focus_areas": [
        ("01", "Market overview", "Explore the EV market landscape and the patterns presented in the market overview dashboard.", "/market-overview"),
        ("02", "Performance analysis", "Compare the EV performance indicators and manufacturer or vehicle insights available in the dashboard.", "/performance-analysis"),
        ("03", "Market story", "Follow the Tableau story to understand the key findings in a guided visual sequence.", "/story"),
    ],
    "technologies": ["Python", "Flask", "Tableau Public", "HTML5", "CSS3", "JavaScript", "Render"],
}

PAGES = {
    "market": {
        "title": "Market Overview",
        "eyebrow": "01 / MARKET LANDSCAPE",
        "description": "Explore the electric vehicle market through the interactive Tableau market overview.",
        "embed": PROJECT["market_url"],
        "public": PROJECT["market_public_url"],
        "next": "/performance-analysis",
        "next_label": "Explore performance analysis",
    },
    "performance": {
        "title": "Performance Analysis",
        "eyebrow": "02 / PERFORMANCE",
        "description": "Dive into the performance analysis and explore the comparisons available in the Tableau dashboard.",
        "embed": PROJECT["performance_url"],
        "public": PROJECT["performance_public_url"],
        "next": "/story",
        "next_label": "Discover the market story",
    },
    "story": {
        "title": "EV Market Analysis Story",
        "eyebrow": "03 / DATA STORY",
        "description": "Explore the Tableau story and follow its visual narrative of the electric vehicle market.",
        "embed": PROJECT["story_url"],
        "public": PROJECT["story_public_url"],
        "next": "/",
        "next_label": "Back to project home",
    },
}
