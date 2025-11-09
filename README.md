# Solar Data Discovery: Week 0 Challenge

## Project Overview

This project analyzes solar farm data from Benin, Sierra Leone, and Togo to identify high-potential regions for solar installation and support MoonLight Energy Solutions' strategic sustainability goals.

## Business Objective

MoonLight Energy Solutions aims to develop a strategic approach to enhance operational efficiency and sustainability through targeted solar investments. This analysis focuses on identifying key trends and valuable insights to support data-driven recommendations for high-potential solar installation regions.

## Dataset Overview

The dataset contains solar radiation measurement data including:
- **GHI** (W/m²): Global Horizontal Irradiance
- **DNI** (W/m²): Direct Normal Irradiance
- **DHI** (W/m²): Diffuse Horizontal Irradiance
- **ModA/ModB** (W/m²): Module sensor measurements
- **Tamb** (°C): Ambient Temperature
- **RH** (%): Relative Humidity
- **WS/WSgust** (m/s): Wind Speed and Gust
- **WD** (°N): Wind Direction
- **BP** (hPa): Barometric Pressure
- **Cleaning**: Cleaning events (1 or 0)
- **Precipitation** (mm/min): Precipitation rate
- **TModA/TModB** (°C): Module temperatures

## Project Structure

```
solar-challenge-week0/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .vscode/
│   └── settings.json
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── data/
│   └── README.md
├── notebooks/
│   ├── __init__.py
│   ├── benin_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── compare_countries.ipynb
│   └── README.md
├── scripts/
│   ├── __init__.py
│   └── README.md
├── tests/
│   ├── __init__.py
│   └── test_data_processing.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Environment Setup

### Prerequisites
- Python 3.9 or higher
- Git
- GitHub account

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd solar-challenge-week0
   ```

2. **Create a virtual environment**
   ```bash
   # Using venv
   python -m venv venv
   
   # Activate on Windows
   venv\Scripts\activate
   
   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Jupyter kernel (if using notebooks)**
   ```bash
   python -m ipykernel install --user --name=solar-challenge
   ```

## Running the Project

### Exploratory Data Analysis (EDA)
1. Navigate to the `notebooks/` directory
2. Open the country-specific EDA notebooks:
   - `benin_eda.ipynb`
   - `sierra_leone_eda.ipynb`
   - `togo_eda.ipynb`
3. Open the comparison notebook:
   - `compare_countries.ipynb`

### Streamlit Dashboard
1. Ensure data files are in the `data/` directory (gitignored)
2. Run the Streamlit app:
   ```bash
   streamlit run app/main.py
   ```

## Branch Structure and Git Workflow

### Branches
1. **setup-task**: Initial repository setup and configuration
2. **eda-benin**: EDA for Benin dataset
3. **eda-sierra-leone**: EDA for Sierra Leone dataset
4. **eda-togo**: EDA for Togo dataset
5. **compare-countries**: Cross-country comparison analysis
6. **dashboard-dev**: Streamlit dashboard development

### Git Commands by Branch

See [GIT_WORKFLOW.md](GIT_WORKFLOW.md) for detailed git commands and commit messages for each branch.

## Key Dates
- **Challenge Introduction**: 9:30 AM UTC on Wednesday, 05 Nov 2025
- **Interim Submission**: 8:00 PM UTC on Sunday, 09 Nov 2025
- **Final Submission**: 8:00 PM UTC on Wednesday, 12 Nov 2025

## Tasks

### Task 1: Git & Environment Setup ✅
- Repository initialization
- Virtual environment setup
- CI/CD pipeline configuration
- Documentation

### Task 2: Data Profiling, Cleaning & EDA
- Summary statistics and missing value reports
- Outlier detection and cleaning
- Time series analysis
- Correlation analysis
- Wind and distribution analysis
- Temperature analysis

### Task 3: Cross-Country Comparison
- Metric comparison (GHI, DNI, DHI)
- Statistical testing (ANOVA/Kruskal-Wallis)
- Key observations and insights
- Visual summaries

### Bonus: Interactive Dashboard
- Streamlit application
- Interactive visualizations
- Country selection widgets
- Deployment to Streamlit Community Cloud

## Contributing

1. Create a feature branch from `main`
2. Make your changes
3. Commit with descriptive messages (following conventional commits)
4. Push to your branch
5. Create a Pull Request

## License

This project is part of the 10 Academy AI Mastery program.

## References

- [Python Testing Guide](https://docs.python-guide.org/writing/tests/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Git Documentation](https://git-scm.com/doc)
- [CI/CD with GitHub Actions](https://docs.github.com/en/actions)

