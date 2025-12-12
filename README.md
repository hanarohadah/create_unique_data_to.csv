# Competency Matrix Generator - Unique Analysis

A **Streamlit-based application** that analyzes and generates a unique competency matrix by cleaning and deduplicating skills data from multiple sources.

## 📋 Features

- **Data Cleaning**: Automatically removes bullet points (●), extra whitespace, and empty entries
- **Duplicate Removal**: Merges old and new skill data, eliminating duplicates
- **Unique Skills Extraction**: Generates a clean list of unique competencies
- **Interactive UI**: User-friendly Streamlit interface for data input and visualization
- **CSV Export**: Export analysis results to CSV format
- **Pandas Integration**: Leverage powerful data manipulation with pandas & numpy

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Install dependencies**:
   ```bash
   pip install -r "requirements(analisis unik).txt"
   ```

2. **Run the application**:
   ```bash
   streamlit run "analisis unik.py"
   ```

3. **Access in browser**:
   - **Local**: http://localhost:8501
   - **Network**: http://[YOUR-IP]:8501

## 📦 Requirements

- `streamlit>=1.28.0` - Web framework for data apps
- `pandas>=2.0.0` - Data manipulation & analysis
- `numpy>=1.24.0` - Numerical computing

See `requirements(analisis unik).txt` for the complete dependency list.

## 📖 How to Use

1. **Input Data**:
   - Enter new skills/competencies in the text input area
   - Each skill can be on a separate line
   - Bullet points (●) will be automatically removed

2. **Process Data**:
   - Click the processing button to clean and deduplicate data
   - The app combines new input with existing data

3. **View Results**:
   - See the cleaned, unique list of competencies
   - Review the analysis in tabular format

4. **Export**:
   - Download results as CSV for further analysis or documentation

## 🔍 Key Functions

### `bersihkan_dan_ambil_unik(list_baru, data_lama)`
- Merges old and new data
- Removes special characters (bullet points)
- Eliminates duplicates
- Returns clean, unique skill list

## 📁 Project Structure

```
Career Path/
├── analisis unik.py                      # Main Streamlit application
├── requirements(analisis unik).txt       # Python dependencies
├── README.md                             # This file
└── ANNUAL (1)/                           # Supporting data folder
```

## 💡 Tips & Best Practices

- **Data Format**: One skill per line for better parsing
- **Clean Input**: Remove unnecessary symbols before input
- **Regular Updates**: Upload new skills periodically to maintain current matrix
- **Backup**: Keep exported CSV files as historical records

## 🛠️ Technical Details

- **Framework**: Streamlit for rapid UI development
- **Data Processing**: Pandas for efficient data manipulation
- **Numerical Computing**: NumPy for array operations
- **State Management**: Streamlit session state for data persistence

## 📝 Notes

- All processing is deterministic (100% rule-based, no AI/ML)
- Data cleaning uses simple but effective string operations
- Perfect for HR departments managing competency frameworks
- Supports iterative data refinement

## 👥 Support & Contributions

For questions or improvements, please contact the development team or refer to the inline documentation in `analisis unik.py`.

---

**Version**: 1.0  
**Last Updated**: December 2025  
**Language**: Python 3.13+
