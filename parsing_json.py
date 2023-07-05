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
#Main fucntion is use to call all fucntion sequentially
         def main(self):
              self.json_data("demo.json")
              self.get_json_detail("demo.json")

data=jsonFile()
data.main()
