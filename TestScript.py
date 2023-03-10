import requests
import json
import csv


def get_list_data(api, filePath):
    dataFile = open(filePath)
    readFile = csv.DictReader(dataFile)
    for row in readFile:
        d1 = row.items()
        for i in d1:
            if '_id' in i:
                id = i[1]
                print(id)
                try:
                    response = requests.get(api + "/" + id)
                    print(response.status_code)

                    actual_response = response.json()
                    print(actual_response)

                    act_id = actual_response['_id']

                    if id == act_id:
                        print("Data Matched, Test PASSED")
                    else:
                        print("Test FAILED, Data Not Matched")

                except requests.exceptions.HTTPError as errh:
                    print("Http Error:", errh)
                except requests.exceptions.ConnectionError as errc:
                    print("Error Connecting:", errc)
                except requests.exceptions.Timeout as errt:
                    print("Timeout Error:", errt)
                except requests.exceptions.RequestException as err:
                    print("OOps: Something Else", err)


def get_data(api):
    try:
        response = requests.get(api)
        print(response.status_code)
        response.raise_for_status()
        resp = response.json()
        print(len(resp))
        i = 0
        while i < 5:
            id = resp[i]['_id']
            print(id)
            i = i + 1
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something Else", err)


file = 'C:/Users/dileep/Desktop/DataSheet.csv'


class MakeApiCall:

    def __init__(self, api):
        get_list_data(api, file)
        get_data(api)


if __name__ == "__main__":
    api_call = MakeApiCall("https://cat-fact.herokuapp.com/facts")
