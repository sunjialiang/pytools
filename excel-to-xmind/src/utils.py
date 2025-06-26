def read_excel(file_path):
    import pandas as pd
    df = pd.read_excel(file_path)
    return df

def write_xmind(data, output_path):
    import xmind
    workbook = xmind.load(output_path)
    sheet = workbook.createSheet("Sheet 1")
    root = sheet.getRootTopic()
    root.setTitle("Mind Map")

    for index, row in data.iterrows():
        topic = root.addSubTopic()
        topic.setTitle(row['Title'])  # Assuming the Excel has a 'Title' column
        # Add more attributes as needed

    xmind.save(workbook)