import fitz
import re


class SDS:

    def __init__(self, filepath):
        self.filepath = filepath

    def extract(self,keys=['PRODUCT NAME', 'PRODUCT NUMBER', 'BRAND'], pageNo=None):
        data = []
        with fitz.open(self.filepath) as doc:
            for page in doc:
                text = page.get_text().split('\n')
                data.append(text)
        res = {}
        if pageNo is not None:
            for idx in range(len(data[pageNo]) - 2):
                line = data[pageNo][idx]
                key = line.strip().upper()
                key = re.sub('[^A-Z\s]', '', key)
                if key in keys:
                    res[key] = re.sub('[:]+', '', data[pageNo][idx + 1].strip().upper()).strip()

        else:
            for pageNum in range(len(data)):
                for idx in range(len(data[pageNum]) - 2):
                    line = data[pageNum][idx]
                    key = line.strip().upper()
                    key = re.sub('[^A-Z\s]', '', key)
                    if key in keys:
                        res[key] = re.sub('[:]+', '', data[pageNum][idx + 1].strip().upper()).strip()
        return res



def get_sds_data(filepath, keys=['PRODUCT NAME', 'PRODUCT NUMBER', 'BRAND'], pageNo=None):
    data = []
    with fitz.open(filepath) as doc:
        for page in doc:
            text = page.get_text().split('\n')
            data.append(text)
    res = {}
    if pageNo is not None:
        for idx in range(len(data[pageNo]) - 2):
            line = data[pageNo][idx]
            key = line.strip().upper()
            key = re.sub('[^A-Z\s]', '', key)
            if key in keys:
                res[key] = re.sub('[:]+', '', data[pageNo][idx + 1].strip().upper()).strip()

    else:
        for pageNum in range(len(data)):
            for idx in range(len(data[pageNum]) - 2):
                line = data[pageNum][idx]
                key = line.strip().upper()
                key = re.sub('[^A-Z\s]', '', key)
                if key in keys:
                    res[key] = re.sub('[:]+', '', data[pageNum][idx + 1].strip().upper()).strip()
    return res