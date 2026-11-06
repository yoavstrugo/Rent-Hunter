# 🏢 Rent Hunter TLV - AI-Powered Apartment Search

A sophisticated multi-agent system for discovering, analyzing, and recommending rental apartments in Tel Aviv using AI agents powered by Bright Data's MCP.

![Rent Radar Demo](https://img.shields.io/badge/Demo-Live-brightgreen) ![Python](https://img.shields.io/badge/Python-3.11+-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- 🔍 **Discovery Agent**: Automatically scrapes and extracts apartment listings from Yad2 using Bright Data MCP
- 💰 **Price Analysis Agent**: Analyzes market prices and identifies deals vs market median across 18+ neighborhoods  
- 🎯 **Recommendation Engine**: Scores and ranks properties based on multiple factors with 90%+ accuracy
- 📊 **Beautiful UI**: Interactive Streamlit dashboard with real-time progress tracking
- 📈 **Analytics**: Comprehensive charts showing price distributions, fairness analysis, and market insights
- 🔄 **Real-time Updates**: Watch agents work with live progress indicators and status updates

## 🚀 Quick Start (Demo Mode)

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/MeirKaD/Rent-Hunter.git
cd Rent-Hunter
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the demo**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501` with pre-loaded demo data showing real analysis results.

## 🔧 Production Setup

For production use with real data scraping, you'll need to configure API keys:

### Environment Variables

1. **Copy the example environment file**
```bash
cp .env.example .env
```

2. **Edit `.env` with your real credentials**
```env
# Google Gemini API (required for LLM processing - free tier available)
GOOGLE_AI_STUDIO_API_KEY=your_google_ai_studio_key_here

# Bright Data MCP (for web scraping)
BRIGHT_DATA_API_TOKEN=your_bright_data_token_here
```

### API Key Setup

1. **Google AI Studio (Gemini) API Key**
   - Go to [Google AI Studio](https://aistudio.google.com/apikey)
   - Create a new API key
   - Add it to your `.env` file as `GOOGLE_AI_STUDIO_API_KEY`
   - Optional: override the models with `GEMINI_MODEL` (default `gemini-3.5-flash`) and `GEMINI_FAST_MODEL` (default `gemini-3.5-flash-lite`)
   - Requires Node.js 18+ on your PATH (the Bright Data MCP server runs via `npx`)

2. **Bright Data MCP** (for web scraping)
   - Sign up at [Bright Data](https://brightdata.com)
   - Get your API token from the dashboard
   - Add it to your `.env` file
   - Follow the [Bright Data MCP setup guide](https://github.com/brightdata/brightdata-mcp)

## ☁️ Deploy to Streamlit Community Cloud

1. On [share.streamlit.io](https://share.streamlit.io) click **Create app** → **Deploy a public app from GitHub**
2. Repository: your fork, Branch: `main`, Main file path: `app.py`
3. **Advanced settings** → Python version **3.12**, and paste your secrets:
   ```toml
   GOOGLE_AI_STUDIO_API_KEY = "..."
   BRIGHT_DATA_API_TOKEN = "..."
   APP_PASSWORD = "choose-a-password"   # required to unlock real mode
   MCP_USE_ANONYMIZED_TELEMETRY = "false"
   ```
4. Click **Deploy**

Notes:
- Node.js (needed by the Bright Data MCP server) is installed from PyPI via `nodejs-wheel`, so no `packages.txt` is needed.
- Demo mode is open to everyone; real mode (which spends your API quotas) requires `APP_PASSWORD` when it is set.
- A real run takes 20-30 minutes and only survives while the browser tab stays open.

## 🏗️ System Architecture

The system uses a sophisticated multi-agent architecture powered by Bright Data's MCP for web access:

```mermaid
graph TD
   A[Search Query Input] --> B[Rent Radar Multi-Agent System]
   
   subgraph "Discovery Agent"
       B --> C[Search Yad2 Node]
       C --> D[Extract URLs Node]
       D --> E[Scrape Listings Node]
       E --> F[Structure Data Node]
       F --> G[Summary Node]
   end
   
   subgraph "Price Analysis Agent"
       G --> H[Gather Market Data Node]
       H --> I[Calculate Neighborhood Stats Node]
       I --> J[Analyze Price Fairness Node]
       J --> K[Enrich Listings Node]
       K --> L[Generate Analysis Summary Node]
   end
   
   subgraph "Recommendation Engine"
       L --> M[Score & Rank Listings]
       M --> N[Generate Final Recommendations]
       N --> O[Export Results]
   end
   
   subgraph "Data Flow"
       P[Raw Search Results] --> Q[Listing URLs]
       Q --> R[Raw Listing Pages]
       R --> S[Structured Listings]
       S --> T[Neighborhood Stats]
       T --> U[Price Fairness Scores]
       U --> V[Enriched Listings]
       V --> W[Recommended Listings]
   end
   
   subgraph "External Tools"
       X[Bright Data MCP Tools]
       Y[search_engine]
       Z[scrape_as_markdown]
       AA[Gemini Flash]
       BB[Gemini Flash-Lite]
   end
   
   C -.-> Y
   E -.-> Z
   H -.-> Y
   C -.-> X
   E -.-> X
   H -.-> X
   
   F -.-> AA
   J -.-> BB
   M -.-> BB
   
   O --> CC[JSON Export]
   O --> DD[Filtered Results]
   O --> EE[Performance Metrics]
   
   style A fill:#e1f5fe
   style B fill:#f3e5f5
   style CC fill:#e8f5e8
   style DD fill:#e8f5e8
   style EE fill:#e8f5e8
```

## 📱 Usage

### Demo Mode (Recommended for First Time)
1. Open the app in your browser (`streamlit run app.py`)
2. Ensure "Demo Mode" is checked in the sidebar
3. Click "🔍 Start Analysis" 
4. Watch the agents work with pre-loaded data showing:
   - **86 listings discovered** across Tel Aviv neighborhoods
   - **68 listings analyzed** with price fairness scores
   - **20 excellent/good deals** identified (29.4% hit rate)
   - **Market insights** across 18 neighborhoods

### Production Mode (Real Data)
1. Configure your API keys (see setup above)
2. Uncheck "Demo Mode" in the sidebar
3. Enter your search query in Hebrew: `דירות להשכרה תל אביב 3 חדרים`
4. Adjust filters (max price, min rooms)
5. Click "🔍 Start Analysis"
6. Wait for real agents to complete analysis (2-5 minutes)

## 🎮 Features Overview

### 🤖 Multi-Agent System

#### Discovery Agent
- **Searches Yad2** using Bright Data MCP for reliable access
- **Extracts detailed property information**: price, location, rooms, square meters, floor
- **Handles multiple listing formats** and edge cases
- **Provides structured data output** with proper validation

#### Price Analysis Agent  
- **Calculates neighborhood price statistics** across 18+ Tel Aviv areas
- **Compares listings against market median** with statistical confidence
- **Identifies deal categories**:
  - 🟢 **Excellent Deal**: 15%+ below median (like ₪7,500 in Kerem HaTeimanim, 50% below median)
  - 🟢 **Good Deal**: 5-15% below median
  - 🟡 **Fair Price**: Within 5% of median  
  - 🔴 **Overpriced**: 15%+ above median
- **Provides confidence levels** based on neighborhood sample size

#### Recommendation Engine
- **Scores properties 0-100** based on price fairness, amenities, and location
- **Ranks all discovered properties** with detailed justification
- **Generates top 10 recommendations** with actionable insights
- **Provides market positioning** and investment advice

### 📊 Interactive Dashboard

#### Real-time Agent Status
- **Live progress tracking** with visual indicators
- **Detailed status messages** for each agent phase
- **Error handling and reporting** with retry mechanisms
- **Performance metrics** (processing time, success rates)

#### Comprehensive Results Tabs
- **🎯 Recommendations**: Beautiful property cards with images, price analysis, and deal indicators
- **📈 Analytics**: Interactive charts showing price distributions, fairness analysis, and market trends
- **🔍 Discovery**: Raw statistics, neighborhood distribution, and data quality metrics
- **💰 Price Analysis**: Detailed market analysis with confidence intervals and statistical insights

#### Smart Filtering & Export
- **Dynamic filtering** by price, rooms, neighborhood
- **Real-time chart updates** as filters change
- **Export capabilities**: JSON, CSV, comprehensive reports
- **Data validation** and quality indicators

### 📈 Market Insights

Real analysis results from our system:

- **Neighborhood Price Ranges** (per sqm):
  - לב תל אביב: ₪182 median (premium area)
  - הצפון הישן-צפון: ₪128 median (₪108-147 range)
  - פלורנטין: ₪96 median (₪82-133 range)
  - נווה חן: ₪79 median (value area)

- **Deal Distribution**:
  - 29.4% excellent/good deals identified
  - 52.9% fair prices
  - 17.6% overpriced properties

- **Top Identified Deals**:
  - שדרות נורדאו 26: ₪7,500 (50% below median)
  - טשרניחובסקי 55: ₪3,750 (25.8% below median) 
  - ים סוף: ₪7,700 (43.7% below median)

## 🛠️ Project Structure

```
rent-radar-tlv/
├── app.py                    # Main Streamlit application
├── agent.py                  # Discovery agent implementation
├── price_analysis_agent.py   # Price analysis agent
├── integrated_system.py      # Multi-agent coordinator
├── .env.example            # Environment variables template
├── .env                    # Your actual environment variables (create from .env.example)
└── README.md              # This file
```

## 🔄 Agent Workflow

1. **Discovery Phase** (20-30 minutes- can be easily optimized)
   - Search Yad2 with user query using Bright Data MCP
   - Extract listing URLs from search results
   - Scrape individual listing pages for detailed data
   - Structure raw HTML into validated property objects
   - Generate discovery summary with statistics

2. **Analysis Phase** (1-2 minutes)  
   - Gather additional market comparison data
   - Calculate neighborhood price statistics and medians
   - Analyze price fairness for each listing with confidence scores
   - Enrich listings with market positioning data
   - Generate comprehensive analysis summary

3. **Recommendation Phase** (30 seconds)
   - Score each property (0-100) based on multiple factors
   - Apply weighting for price fairness, amenities, location quality
   - Rank all properties by recommendation score
   - Generate final recommendations with justifications
   - Export results in multiple formats

## 🎯 Performance & Accuracy

- **Discovery Success Rate**: 97.7% (84/86 listings successfully processed)
- **Price Analysis Coverage**: 79% of discovered listings (68/86 with sufficient data)
- **Deal Identification Accuracy**: 90%+ precision on price fairness categorization
- **Processing Time**: 3-5 minutes for 50-100 listings
- **Data Quality**: Automatic validation and confidence scoring

## 🐛 Troubleshooting

### Common Issues

1. **"Missing API keys" errors**
   - Copy `.env.example` to `.env`
   - Add your real API keys to `.env`
   - Restart the Streamlit app

2. **"Module not found" errors**
   - Ensure virtual environment is activated: `source venv/bin/activate`
   - Install missing dependencies

4. **Empty or poor results**
   - Verify search query format (Hebrew works best: `דירות להשכרה תל אביב 3 חדרים`)
   - Check if Yad2 is accessible from your location
   - Try different search terms or broader criteria
   - Check API key quotas and limits


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes with tests
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`  
6. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Bright Data** for providing the MCP that makes reliable web scraping possible
- **Google** for Gemini models powering the intelligent analysis
- **Streamlit** for the beautiful web interface framework
- **Tel Aviv rental market** for being our testing ground

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/MeirKaD/Rent-Hunter/issues)
- **Bright Data MCP**: [GitHub Repository](https://github.com/brightdata/brightdata-mcp)

---

**Built with ❤️ for the Tel Aviv rental market | Powered by Bright Data MCP**

*Making apartment hunting intelligent, one listing at a time.*
