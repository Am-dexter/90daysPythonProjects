#this program downloads a csv file from the internet and saves it

from urllib import request

sample_data_url = 'https://www.sample-videos.com/csv/Sample-Spreadsheet-100-rows.csv'


def download_product_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'sampledata.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()


download_product_data(sample_data_url)

