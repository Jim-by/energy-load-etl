import sys
from pathlib import Path

project_root = Path(__file__).parent if Path(__file__).parent.name == 'src' else Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import pipeline modules
from extract import download_timeseries  # Module for raw data extraction
from transform import transform_load     # Module for data cleaning/transformation
from validate import validate_load       # Module for data quality validation
from analyze import analyze_load_data    # Module for data analysis/visualization

def main():
    """Orchestrator for the full ETL+A pipeline: Extract → Transform → Validate → Analyze."""
    try:
        print("="*50)
        print("Starting Full Electricity Load Analysis Pipeline")
        print("="*50)

        # Step 1: Download raw time series data from the public source
        print("\n[Step 1/4] Downloading raw data...")
        raw_data_path = download_timeseries()
        print(f"   ✓ Raw data ready: {raw_data_path}")

        # Step 2: Transform raw data (filter columns, clean missing values, standardize format)
        print("\n[Step 2/4] Transforming and cleaning data...")
        processed_data_path = transform_load(raw_data_path)
        print(f"   ✓ Processed data ready: {processed_data_path}")

        # Step 3: Validate processed data quality (check gaps, duplicates, outliers)
        print("\n[Step 3/4] Validating data quality...")
        is_data_valid = validate_load(processed_data_path)
        if is_data_valid:
            print("Data passed validation!")
        else:
            print("Data has minor issues (but is still usable).")

        # Step 4: Run analysis and generate visualizations (only if data is valid)
        print("\n[Step 4/4] Running data analysis...")
        if is_data_valid:
            analyze_load_data(processed_data_path)
            print("\nAnalysis completed successfully! Results saved to the plots/ folder.")
        else:
            print("\nSkipping analysis: data failed validation.")

        print("\n" + "="*50)
        print("Pipeline finished!")
        print("="*50)

    except ImportError as e:
        print(f"\nImport error: {str(e)}")
        print("Check that all modules exist in src/: extract.py, transform.py, validate.py, analyze.py.")
        print("Test individually: python src/validate.py (to check syntax and imports).")
        raise
    except FileNotFoundError as e:
        print(f"\nFile error: {str(e)}")
        print("Ensure processed data exists: run transform.py to create data/processed/processed_load_data.csv.")
        raise
    except ValueError as e:
        print(f"\nData error: {str(e)}")
        raise
    except Exception as e:
        print(f"\nPipeline execution error: {str(e)}")
        raise  

if __name__ == "__main__":
    main()
