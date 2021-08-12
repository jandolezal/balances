import gzip
import io
import requests

URL = 'https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/nrg_bal_c.tsv.gz'


def process_line(line: str):
    """Return line with only commas as separators.
    Original dataset mixes tabas and commas as separators.
    """
    return line.replace('\t', ',').replace(' ', '')


def clean_dataset(url: str, filename: str = 'balances-june-2021'):
    """Download and extract the original tsv file. Clean and save as csv." """
    r = requests.get(url)
    data = gzip.decompress(r.content)
    with open(f'{filename}.tsv', 'wb') as fbout:
        fbout.write(data)

    with open(f'{filename}.tsv', 'r') as fin:
        with open(f'{filename}.csv', 'w') as fout:
            for line in fin.readlines():
                fout.write(process_line(line))


if __name__ == '__main__':
    clean_dataset(URL)
