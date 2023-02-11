def verify_srt(file_path):
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
            index = 1
            while index < len(lines):
                if not lines[index].strip().isdigit():
                    return False
                index += 1
                if index >= len(lines):
                    break
                if not '-->' in lines[index]:
                    return False
                index += 1
                while index < len(lines) and lines[index].strip():
                    index += 1
                index += 1
            return True
    except:
        return False
