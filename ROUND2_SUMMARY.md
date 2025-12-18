# Round 2 Submission Summary

## Overview
This document summarizes all Round 2 components submitted for the Envision Datathon.

## ✅ Completed Components

### 1. Preprocessing & Visualization ✓

#### Preprocessing Steps (`script/preprocessing.py`)
The preprocessing script performs the following operations:

1. **Data Loading**: Loads raw CSV data from `ecommerce_grey_market_data.csv`
2. **Data Cleaning**:
   - Cleans numeric columns (price, MRP, discount_percent)
   - Removes negative values and invalid data
   - Handles missing values appropriately
3. **Feature Engineering**:
   - Extracts ratings from text format
   - Cleans number of ratings (removes commas, handles negative values)
   - Calculates discount percentage where missing
   - Extracts brand names from product names
4. **Derived Features**:
   - `price_mrp_ratio`: Ratio of price to MRP
   - `suspicious_pricing`: Flag for products with price < 50% of MRP
   - `has_review`: Indicator for products with reviews
   - `rating_quality_score`: Combined rating and review count metric
5. **Data Export**: Saves processed data to `processed_data.csv`

#### Visualization Steps (`script/visualization.py`)
The visualization script generates comprehensive visualizations:

**Preprocessing Visualizations** (`visualizations/preprocessing/`):
- Missing values heatmap
- Data quality bar chart
- Numeric distributions

**Analysis Visualizations** (`visualizations/analysis/`):
- Platform distribution
- Price analysis by platform
- Discount distribution
- Rating analysis
- Top brands analysis
- Suspicious pricing analysis
- Correlation heatmap
- Seller analysis

**Dashboard Summary** (`visualizations/dashboard/`):
- Comprehensive dashboard-style summary visualization

### 2. Visualization Dashboard ✓

#### Dashboard Guide (`DASHBOARD_GUIDE.md`)
Complete instructions provided for creating dashboards using:
- **Power BI**: Step-by-step guide with visualization recommendations
- **Tableau**: Detailed worksheet and dashboard creation instructions

#### Key Dashboard Components:
- Overview page with KPIs
- Price analysis page
- Rating & reviews page
- Grey market indicators page
- Discount analysis page

#### Dashboard Data Source:
- Use `processed_data.csv` for dashboard creation
- All preprocessing steps documented and reproducible

### 3. Repository Update ✓

#### New Files Added:
1. `script/preprocessing.py` - Preprocessing implementation
2. `script/visualization.py` - Visualization generation
3. `script/run_round2.py` - Main execution script for Round 2
4. `DASHBOARD_GUIDE.md` - Dashboard creation guide
5. `ROUND2_SUMMARY.md` - This summary document
6. `processed_data.csv` - Processed dataset (generated)
7. `visualizations/` - Directory with all visualizations (generated)

#### Updated Files:
1. `README.md` - Updated with Round 2 information
2. `script/requirements.txt` - Added matplotlib and seaborn

## 📊 Key Metrics & Insights

### Data Quality
- Initial data shape: Varies based on scraping results
- Missing value handling: Comprehensive cleaning applied
- Data types: Properly formatted for analysis

### Grey Market Indicators
- Suspicious pricing detection: Products with price < 50% of MRP
- Rating quality assessment: Combined rating and review metrics
- Platform comparison: Analysis across Amazon, Flipkart, and Meesho

### Visualizations Generated
- **Preprocessing**: 3 visualizations
- **Analysis**: 8 visualizations
- **Dashboard**: 1 comprehensive summary

## 🚀 How to Run

### Quick Start
```bash
cd script
python run_round2.py
```

This will:
1. Load and preprocess the raw data
2. Generate all visualizations
3. Create processed dataset ready for dashboard

### Individual Steps
```bash
# Step 1: Preprocessing only
python preprocessing.py

# Step 2: Visualizations only
python visualization.py
```

## 📁 File Structure

```
EV09_CodeLayers/
├── script/
│   ├── preprocessing.py          # Preprocessing implementation
│   ├── visualization.py          # Visualization generation
│   ├── run_round2.py             # Main Round 2 script
│   └── requirements.txt          # Updated dependencies
├── ecommerce_grey_market_data.csv  # Raw data (Round 1)
├── processed_data.csv            # Processed data (Round 2)
├── visualizations/               # Generated visualizations
│   ├── preprocessing/            # Preprocessing visualizations
│   ├── analysis/                # Analysis visualizations
│   └── dashboard/               # Dashboard summary
├── DASHBOARD_GUIDE.md           # Dashboard creation guide
├── ROUND2_SUMMARY.md            # This file
└── README.md                    # Updated documentation
```

## ✅ Round 2 Requirements Checklist

- [x] **Preprocessing & Visualization**
  - [x] All preprocessing steps demonstrated
  - [x] Appropriate visualizations created
  - [x] Visualizations saved and organized
  
- [x] **Visualization Dashboard**
  - [x] Dashboard guide created (Power BI & Tableau)
  - [x] Instructions for dashboard creation provided
  - [x] Key metrics and visualizations documented
  
- [x] **Repository Update**
  - [x] All components added to repository
  - [x] Documentation updated
  - [x] Code properly organized and commented

## 📝 Notes

1. **Data Source**: The processed data is generated from the raw CSV file. Run `run_round2.py` to regenerate if needed.

2. **Visualizations**: All visualizations are saved as PNG files with high resolution (300 DPI) for presentation quality.

3. **Dashboard**: The dashboard should be created separately using Power BI or Tableau following the guide in `DASHBOARD_GUIDE.md`.

4. **Dependencies**: Ensure all dependencies are installed using `pip install -r script/requirements.txt`.

## 🎯 Next Steps

1. Review generated visualizations in `visualizations/` folder
2. Create Power BI or Tableau dashboard using `processed_data.csv`
3. Ensure all files are committed to the repository
4. Prepare presentation materials for Round 2 evaluation

---

**Team CodeLayers**
- Krushna Raut
- Abhijeet Mate

**Round 2 Submission Date**: [Update with submission date]

