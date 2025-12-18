# Dashboard Creation Guide

## Overview
This guide provides instructions for creating a comprehensive dashboard using either **Power BI** or **Tableau** for the E-commerce Grey Market Data Analysis project.

## Prerequisites
- Processed data file: `processed_data.csv`
- Power BI Desktop (free) OR Tableau Desktop/Public (free)

---

## Option 1: Power BI Dashboard

### Step 1: Import Data
1. Open Power BI Desktop
2. Click **Get Data** → **Text/CSV**
3. Select `processed_data.csv`
4. Click **Load** to import the data

### Step 2: Data Model Setup
1. Ensure all numeric columns are properly formatted:
   - `price`, `mrp`, `discount_percent` → Decimal Number
   - `product_rating`, `review_rating` → Decimal Number
   - `num_ratings` → Whole Number
   - `suspicious_pricing`, `has_review` → Whole Number (0/1)

### Step 3: Create Key Visualizations

#### 3.1 Overview Page
- **KPI Cards:**
  - Total Products (Count of records)
  - Average Price (Average of `price`)
  - Average Rating (Average of `product_rating`)
  - Suspicious Products Count (Sum of `suspicious_pricing`)

- **Visualizations:**
  - **Pie Chart**: Platform Distribution (`platform`)
  - **Bar Chart**: Top 10 Brands (`brand`)
  - **Bar Chart**: Top 10 Sellers (`seller_name`)
  - **Card**: Total Unique Brands
  - **Card**: Total Unique Sellers

#### 3.2 Price Analysis Page
- **Visualizations:**
  - **Box Plot**: Price Distribution by Platform
  - **Histogram**: Price Distribution (filtered for reasonable range)
  - **Scatter Plot**: Price vs MRP (with trend line)
  - **Table**: Products with Highest Prices
  - **Table**: Products with Lowest Prices

#### 3.3 Rating & Reviews Page
- **Visualizations:**
  - **Histogram**: Product Rating Distribution
  - **Box Plot**: Rating by Platform
  - **Bar Chart**: Products with Reviews vs Without Reviews (`has_review`)
  - **Scatter Plot**: Rating vs Number of Ratings
  - **Table**: Top Rated Products

#### 3.4 Grey Market Indicators Page
- **Visualizations:**
  - **Bar Chart**: Suspicious Pricing Count (`suspicious_pricing`)
  - **Stacked Bar Chart**: Suspicious Pricing by Platform
  - **Table**: Products with Suspicious Pricing (Price < 50% of MRP)
  - **Scatter Plot**: Price/MRP Ratio Distribution
  - **Card**: Percentage of Suspicious Products

#### 3.5 Discount Analysis Page
- **Visualizations:**
  - **Histogram**: Discount Percentage Distribution
  - **Box Plot**: Discount by Platform
  - **Bar Chart**: Average Discount by Brand (Top 10)
  - **Scatter Plot**: Discount vs Price
  - **Table**: Products with Highest Discounts

### Step 4: Add Filters and Slicers
Add slicers for:
- Platform (multi-select)
- Brand (multi-select)
- Price Range (between)
- Rating Range (between)
- Suspicious Pricing (Yes/No)

### Step 5: Formatting
- Use consistent color scheme (e.g., Blue for normal, Red for suspicious)
- Add titles and descriptions to each visualization
- Set appropriate number formats (currency for prices, percentage for discounts)
- Enable cross-filtering between visuals

### Step 6: Publish
1. Click **Publish** → **Publish to Power BI**
2. Sign in with your Microsoft account
3. Select workspace and publish

---

## Option 2: Tableau Dashboard

### Step 1: Connect to Data
1. Open Tableau Desktop
2. Click **Connect to Data** → **Text file**
3. Select `processed_data.csv`
4. Click **Sheet 1** to start creating visualizations

### Step 2: Data Preparation
1. In Data Source tab, ensure data types are correct:
   - `price`, `mrp`, `discount_percent` → Number (Decimal)
   - `product_rating`, `review_rating` → Number (Decimal)
   - `num_ratings` → Number (Whole)
   - `platform`, `brand`, `seller_name` → String
   - `suspicious_pricing`, `has_review` → Number (Whole)

### Step 3: Create Worksheets

#### Worksheet 1: Overview Dashboard
- **Text Table**: Key Metrics
  - Total Products: `COUNT(Product Name)`
  - Avg Price: `AVG(Price)`
  - Avg Rating: `AVG(Product Rating)`
  - Suspicious Count: `SUM(Suspicious Pricing)`

- **Pie Chart**: Platform Distribution
  - Rows: `Platform`
  - Marks: Pie chart, Color by `Platform`, Size by `COUNT(Product Name)`

- **Horizontal Bar Chart**: Top 10 Brands
  - Rows: `Brand` (Top 10 by Count)
  - Columns: `COUNT(Product Name)`

#### Worksheet 2: Price Analysis
- **Box Plot**: Price by Platform
  - Rows: `Platform`
  - Columns: `Price` (Box plot)

- **Histogram**: Price Distribution
  - Rows: `Price` (Bins)
  - Columns: `COUNT(Product Name)`

- **Scatter Plot**: Price vs MRP
  - Columns: `MRP`
  - Rows: `Price`
  - Color by `Platform`

#### Worksheet 3: Rating Analysis
- **Histogram**: Rating Distribution
  - Rows: `Product Rating` (Bins)
  - Columns: `COUNT(Product Name)`

- **Box Plot**: Rating by Platform
  - Rows: `Platform`
  - Columns: `Product Rating`

- **Scatter Plot**: Rating vs Number of Ratings
  - Columns: `Number of Ratings`
  - Rows: `Product Rating`
  - Size by `COUNT(Product Name)`

#### Worksheet 4: Grey Market Indicators
- **Bar Chart**: Suspicious Pricing Count
  - Rows: `Suspicious Pricing` (as dimension)
  - Columns: `COUNT(Product Name)`

- **Stacked Bar Chart**: Suspicious by Platform
  - Rows: `Platform`
  - Columns: `COUNT(Product Name)`
  - Color by `Suspicious Pricing`

- **Table**: Suspicious Products
  - Columns: `Product Name`, `Platform`, `Price`, `MRP`, `Price/MRP Ratio`
  - Filter: `Suspicious Pricing = 1`

#### Worksheet 5: Discount Analysis
- **Histogram**: Discount Distribution
  - Rows: `Discount Percent` (Bins)
  - Columns: `COUNT(Product Name)`

- **Box Plot**: Discount by Platform
  - Rows: `Platform`
  - Columns: `Discount Percent`

### Step 4: Create Dashboard
1. Create a new **Dashboard**
2. Add worksheets to the dashboard:
   - **Layout**: Use tiled layout
   - **Filters**: Add filters for Platform, Brand, Price Range, Rating Range
   - **Actions**: Enable filter actions for cross-filtering

3. **Dashboard Layout:**
   ```
   ┌─────────────────────────────────────────┐
   │         Overview Metrics (Row 1)        │
   ├──────────────────┬──────────────────────┤
   │  Platform Dist.  │   Top Brands         │
   ├──────────────────┴──────────────────────┤
   │         Price Analysis                  │
   ├──────────────────┬──────────────────────┤
   │  Rating Analysis │  Grey Market Flags   │
   └──────────────────┴──────────────────────┘
   ```

### Step 5: Formatting
- Apply consistent color palette
- Use appropriate number formats
- Add titles and tooltips
- Enable tooltips with additional information

### Step 6: Publish
1. Click **Server** → **Publish Workbook**
2. Sign in to Tableau Public/Server
3. Add description and tags
4. Publish

---

## Key Metrics to Include

### Primary KPIs
1. **Total Products**: Count of all products
2. **Average Price**: Mean price across all products
3. **Average Rating**: Mean product rating
4. **Suspicious Products**: Count of products with suspicious pricing

### Secondary Metrics
1. **Platform Distribution**: Products per platform
2. **Brand Diversity**: Number of unique brands
3. **Seller Diversity**: Number of unique sellers
4. **Review Coverage**: Percentage of products with reviews
5. **Discount Statistics**: Average discount percentage

### Grey Market Indicators
1. **Suspicious Pricing Flag**: Products with price < 50% of MRP
2. **Price/MRP Ratio**: Distribution of price to MRP ratios
3. **Low Rating Products**: Products with rating < 3.0
4. **High Discount Products**: Products with discount > 70%

---

## Best Practices

1. **Data Quality**: Always verify data types and handle missing values
2. **Performance**: Use filters to limit data scope if dataset is large
3. **Interactivity**: Enable cross-filtering and drill-down capabilities
4. **Accessibility**: Use color-blind friendly palettes
5. **Documentation**: Add descriptions and tooltips to explain metrics
6. **Mobile Responsive**: Design dashboards to work on different screen sizes

---

## Dashboard Checklist

- [ ] All data imported correctly
- [ ] Data types are correct
- [ ] Key metrics/KPIs displayed
- [ ] Visualizations are clear and informative
- [ ] Filters and slicers are functional
- [ ] Color scheme is consistent
- [ ] Titles and labels are descriptive
- [ ] Dashboard is published/shared
- [ ] Documentation is complete

---

## Additional Resources

- **Power BI**: [Microsoft Power BI Documentation](https://docs.microsoft.com/power-bi/)
- **Tableau**: [Tableau Learning Resources](https://www.tableau.com/learn)
- **Data Visualization Best Practices**: [Storytelling with Data](https://www.storytellingwithdata.com/)

---

**Note**: The processed data file (`processed_data.csv`) contains cleaned and transformed data ready for dashboard creation. All preprocessing steps have been documented in the `preprocessing.py` script.

