
def get_filename(header):
    filename = None

    content_disposition = header[b'Content-Disposition'].decode('utf-8')
    for item in content_disposition.split(';'):
        if 'filename' in item and '=' in item:
            if item.split('=')[0].strip() == 'filename':
                if item.split('=')[1].strip()[0] in ['"', "'"]:
                    filename = item.split('=')[1].strip()[1:-1]
                else:
                    filename = item.split('=')[1].strip()

    return filename
