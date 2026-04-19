def read_file(file_path):
    lines = []
    try:
        with open(file_path, "r" ,encoding="utf-8") as f:
            for line_number , line in enumerate(f, start=1):
                lines.append((line_number,line.strip()))


    except:
        pass
            
    return lines
