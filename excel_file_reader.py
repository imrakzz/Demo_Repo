def file_reader(file_path: str):
    """
    file reader tool.
    reading the jira tasks created by architect.

    Read Excel file and return its content as a formatted string.

        Args:
            file_path (str): Path to the Excel file

    Returns:
            str: Formatted content of the Excel file
        """
    try:
        if not os.path.exists(file_path):
            return "Error: Excel file not found at the specified path.test"

        # Read Excel file
        df = pd.read_excel(file_path)

        # Convert DataFrame to string with proper formatting
        excel_content = df.to_string(index=False, max_rows=None, max_cols=None)

        return f"{excel_content}"

    except Exception as e:
        return f"Error reading Excel file: {str(e)}"
