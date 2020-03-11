import csv


valid_file = open('valid.csv', mode='w')
writer = csv.writer(valid_file, delimiter=',',
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL)

with open('to_parse.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for i, row in enumerate(csv_reader):
        vid_id, video_url, *video_type = row
        if video_url.strip() != 'None':
            writer.writerow(row)

valid_file.close()