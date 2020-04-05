import json
import re
import urllib.request

from pytube import YouTube

class Helper:
    def __init__(self):
        pass

    def title_to_underscore_title(self, title: str):
        title = re.sub('[\W_]+', "_", title)
        return title.lower()

    def id_from_url(self, url: str):
        url = url.rsplit("=", 1)[1]
        return url.rsplit("\n", 1)[0]

    def extract_from_file(self, file: str):
        with open(file, "r") as f:
            return f.readlines()
    
    def create_url(self, video_id: str, api_key: str):
        return f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
    
    def loopPrint(self, enumerable=[]):
        if isinstance(enumerable, list):
            for i in range(0, len(enumerable)):
                print(enumerable[i])
        elif isinstance(enumerable, dict):
            for i in enumerable:
                print(i + ": " + enumerable[i])
        else:
            print("invalid")
        print("\n")

#variables
api_key = "AIzaSyCQvy487SXrJkKKzfTjArz0iBIpsCcqKeo"
direct_path_to_file = "C:\\Users\\Rikard Hallberg\\Desktop\\Workspace\\Python files\\Data science\\YoutubeLinks.txt"
helper = Helper()

#Step 0: get the videos into the youtubelinks.txt file, automating the whole process
search_results = urllib.request.urlopen()

#Step 1: extract from target file where all youtube links are
video_keys = helper.extract_from_file(direct_path_to_file)
for i, item in enumerate(video_keys):
    #Step 2: extract the key of the video from each item in the video_keys
    video_keys[i] = helper.id_from_url(item)

helper.loopPrint(video_keys)
#Step 3: open a url with the apikey and the key of the video, store in an video_keys
video_names = []
json_content = []
for item in video_keys:
    json_url = urllib.request.urlopen(helper.create_url(item, api_key))
    json_content.append(str(json.loads(json_url.read())))

#Step 4: split off all the unnecessary data except for the title of the video, store in the video_names video_keys
for i, item in enumerate(json_content):
    video_names.append(json_content[i].rsplit("\', \'description\'", 1)[0])
    video_names[i] = video_names[i].rsplit("\'title\': \'", 1)[1]

helper.loopPrint(video_names)
#Step 5: Create a kvp dictionary with the video key as the key and the title name as the value
dictionary = {}
for i, item in enumerate(video_keys):
    if item not in dictionary.keys():
        dictionary[item] = video_names[i]
#Step 6: Print out all eleements

helper.loopPrint(dictionary)


