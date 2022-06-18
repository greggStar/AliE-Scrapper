import json
import csv

def createCSV():
    with open('./categories2.json') as json_file:
        data = json.load(json_file)

    # print(data[0]['main-category'])
    headers = ['Main', 'Category', 'Sub-Category']
    f = open('categories.csv', 'w')
    writer = csv.writer(f)
    for x in range(len(data)):
        if x == 0:
            writer.writerow(headers)
        
        main_cate = data[x]['main-category']
        # print(data[x]['categories'][0])
        for cate in data[x]['categories'].values():
            # print(cate)
            cate = list(cate.values())
            # print(cate[1])
            cate_name = cate[0]

            
            for sub in cate[1]:
                row = main_cate,cate_name,sub
                writer.writerow(row)
                print(row)

    f.close()
        
    
            
        

    # cate_data = data[key]

    # data_file = open('data_file.csv', 'w')

    # csv_writer = csv.writer(data_file)

    # count = 0

    # values = [value for value_dict in data.values() for value in value_dict.values()]
    # print(values)

    # for cate in cate_data:
    #     if count == 0:

    #         header = cate.keys()
    #         csv_writer.writerow(header)
    #         count += 1
 
    # # Writing data of CSV file
    #     csv_writer.writerow(cate.values())
    
    #     data_file.close()

if __name__ == '__main__':
    createCSV() 


