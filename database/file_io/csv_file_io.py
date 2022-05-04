import csv



with open('USvideos.csv', 'r', encoding='utf-8-sig') as reader_csv:

	reader = csv.reader(reader_csv, delimiter=',')

	for row in reader:
	    print (row)



with open('tmp_csv.csv', 'w', encoding='utf-8-sig', newline='') as writer_csv:

	writer = csv.writer(writer_csv, delimiter=',')

	writer.writerow(['love'] * 3 + ['banana'])


