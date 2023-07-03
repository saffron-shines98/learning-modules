import json
class jsonFile:
     # json_data funtion is taking a input as filename and loads it and returns the loaded json
         def json_data(self, file_name):
              try:
                   with open(file_name) as s:
                        jsonload = json.load(s)
                        return jsonload
              except Exception as e:
                   print("file not found",e)
                   return None


     # get_json_detail function is extract and print the titles from JSON data
         def get_json_detail(self, file_name):
              try:
                   jsonload = self.json_data(file_name)
                   get_title = jsonload['message']['order']['quote']['breakup']
                   for i in get_title:
                        print(i.get('title'))
                        return None
              except Exception as e:
                   print("title key is not available",e)
# data is a object of jsonfile
data = jsonFile()
# data.get_data is Load the JSON data from the file
data.json_data('demo.json')
# data.get_json_detail is extract and print the titles from the JSON data
data.get_json_detail("demo.json")
