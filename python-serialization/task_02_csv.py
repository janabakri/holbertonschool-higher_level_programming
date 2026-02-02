#!/usr/bin/env python3
"""
Task 2: Converting CSV Data to JSON Format
Convert CSV data to JSON format using serialization techniques.
"""

import csv
import json
import os


def convert_csv_to_json(csv_filename: str) -> bool:
    """
    Convert a CSV file to JSON format.
    
    Args:
        csv_filename (str): The name/path of the CSV file to convert
        
    Returns:
        bool: True if conversion was successful, False otherwise
        
    Raises:
        FileNotFoundError: If the CSV file does not exist
        ValueError: If CSV file is empty or malformed
    """
    data = []  # List to hold all rows as dictionaries
    
    try:
        # 1. Check if file exists
        if not os.path.exists(csv_filename):
            raise FileNotFoundError(f"CSV file '{csv_filename}' does not exist")
        
        # 2. Check if file is empty
        if os.path.getsize(csv_filename) == 0:
            raise ValueError(f"CSV file '{csv_filename}' is empty")
        
        # 3. Open and read the CSV file
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            # Use DictReader to automatically convert each row to a dictionary
            csv_reader = csv.DictReader(csv_file)
            
            # Read all rows into a list of dictionaries
            for row in csv_reader:
                data.append(row)
            
            # Check if any data was read
            if len(data) == 0:
                raise ValueError(f"CSV file '{csv_filename}' contains no data rows")
        
        # 4. Serialize to JSON and write to file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            # Use indent for pretty printing, ensure_ascii for Unicode support
            json.dump(data, json_file, indent=2, ensure_ascii=False)
        
        print(f"✅ Successfully converted '{csv_filename}' to 'data.json'")
        print(f"   Converted {len(data)} rows of data")
        
        # Optional: Print summary of conversion
        if data:
            print(f"   Fields: {', '.join(data[0].keys())}")
        
        return True
    
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        return False
    except ValueError as e:
        print(f"❌ Error: {e}")
        return False
    except csv.Error as e:
        print(f"❌ CSV parsing error: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON serialization error: {e}")
        return False
    except IOError as e:
        print(f"❌ I/O error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


# Additional helper functions for enhanced functionality
def validate_csv_file(csv_filename: str) -> bool:
    """
    Validate that a CSV file exists and has valid format.
    
    Args:
        csv_filename (str): CSV file to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    try:
        if not os.path.exists(csv_filename):
            return False
        
        with open(csv_filename, 'r', encoding='utf-8') as f:
            # Read first few lines to check format
            sample = f.read(1024)
            f.seek(0)
            
            # Check if file contains comma (or other delimiters)
            if ',' not in sample and '\t' not in sample:
                return False
            
            # Try to parse as CSV
            csv_reader = csv.reader(f)
            headers = next(csv_reader, None)
            
            if not headers:
                return False
            
            return True
    
    except Exception:
        return False


def get_conversion_stats(csv_filename: str, json_filename: str = 'data.json') -> dict:
    """
    Get statistics about the conversion.
    
    Args:
        csv_filename (str): Original CSV file
        json_filename (str): Converted JSON file
        
    Returns:
        dict: Statistics about the conversion
    """
    stats = {
        'csv_file': csv_filename,
        'json_file': json_filename,
        'rows_converted': 0,
        'csv_size_bytes': 0,
        'json_size_bytes': 0,
        'fields': []
    }
    
    try:
        # Get CSV stats
        if os.path.exists(csv_filename):
            stats['csv_size_bytes'] = os.path.getsize(csv_filename)
            
            with open(csv_filename, 'r', encoding='utf-8') as f:
                csv_reader = csv.DictReader(f)
                data = list(csv_reader)
                stats['rows_converted'] = len(data)
                
                if data:
                    stats['fields'] = list(data[0].keys())
        
        # Get JSON stats
        if os.path.exists(json_filename):
            stats['json_size_bytes'] = os.path.getsize(json_filename)
        
        return stats
    
    except Exception:
        return stats


# Test code when module is run directly
if __name__ == "__main__":
    import sys
    
    def main():
        """Main test function"""
        print("=" * 50)
        print("CSV to JSON Converter - Test Mode")
        print("=" * 50)
        
        # Test cases
        test_files = []
        
        # Create test CSV file if it doesn't exist
        if not os.path.exists("data.csv"):
            test_csv_content = """name,age,city
John,28,New York
Alice,24,Los Angeles
Bob,22,Chicago
Eve,30,San Francisco
Mohamed,35,Cairo
安娜,29,北京"""
            
            with open("data.csv", "w", encoding="utf-8") as f:
                f.write(test_csv_content)
            print("✅ Created test CSV file: data.csv")
        
        test_files.append("data.csv")
        
        # Test edge cases
        edge_cases = [
            ("empty.csv", ""),  # Empty file
            ("headers_only.csv", "name,age,city\n"),  # Headers only
            ("single_row.csv", "name,age,city\nJohn,28,New York"),  # Single row
            ("unicode.csv", "name,city\nمحمد,القاهرة\n安娜,北京"),  # Unicode
        ]
        
        for filename, content in edge_cases:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            test_files.append(filename)
        
        # Run conversion tests
        success_count = 0
        for csv_file in test_files:
            print(f"\n{'='*30}")
            print(f"Testing: {csv_file}")
            print(f"{'='*30}")
            
            result = convert_csv_to_json(csv_file)
            
            if result:
                success_count += 1
                print(f"✅ SUCCESS")
                
                # Show stats if data.json was created
                if os.path.exists("data.json"):
                    stats = get_conversion_stats(csv_file)
                    print(f"   Rows: {stats['rows_converted']}")
                    print(f"   Fields: {', '.join(stats['fields'])}")
                    
                    # Show sample of converted data
                    if stats['rows_converted'] > 0:
                        with open("data.json", "r", encoding="utf-8") as f:
                            data = json.load(f)
                            if data:
                                print(f"   Sample row: {data[0]}")
            else:
                print(f"❌ FAILED")
        
        # Test with non-existent file
        print(f"\n{'='*30}")
        print("Testing: non_existent.csv")
        print(f"{'='*30}")
        
        if not convert_csv_to_json("non_existent.csv"):
            print("✅ Correctly handled non-existent file")
        
        # Cleanup
        print(f"\n{'='*30}")
        print("Cleanup")
        print(f"{'='*30}")
        
        for file in test_files + ["data.json"]:
            if os.path.exists(file):
                try:
                    os.remove(file)
                    print(f"Removed: {file}")
                except Exception:
                    pass
        
        print(f"\n{'='*50}")
        print(f"Test Summary: {success_count}/{len(test_files)} successful")
        print(f"{'='*50}")
    
    # Run tests
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️ Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Test error: {e}")
        sys.exit(1)
