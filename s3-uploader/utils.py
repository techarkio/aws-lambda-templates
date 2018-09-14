def get_filename(header):
    filename = None
    if not isinstance(header, dict):
        return filename

    content_disposition = header[b'Content-Disposition'].decode('utf-8')
    for item in content_disposition.split(';'):
        if 'filename' in item and '=' in item:
            if item.split('=')[0] == 'filename':
                if item.split('=')[1] in ['"', "'"]:
                    filename = item.split('=')[1][1:-1]
                else:
                    filename = item.split('=')[1]

    return filename
