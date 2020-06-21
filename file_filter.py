import os, shutil
def filefilter(folderpath):
    # NOTE: You can write every single extensions inside tuples 
    dict_extensions = {
        'audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac'),
        'video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
        'document_extensions' : ('.doc', '.pdf', '.txt'),
        'image_extensions':('.jpg','.png')
    }


    # folderpath = input('enter folder path : ')

    def file_finder(folder_path, file_extensions):
        # files = []
        # for file in os.listdir(folder_path):
        #     for extension in file_extensions:
        #         if file.endswith(extension):
        #             files.append(file)
        # return files
        return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]


    def CheckFolder(folder_path):
        if os.path.exists(folder_path):
            print(f"{folder_name} is Exist")
        else:
            os.mkdir(folder_path)
        return f"{folder_name}"

    # print(file_finder(folderpath, video_extensions))
    for extension_type, extension_tuple in dict_extensions.items():
        folder_name = extension_type.split('_')[0] + 'Files'
        folder_path = os.path.join(folderpath, folder_name)
        CheckFolder(folder_path)
      
        for item in file_finder(folderpath, extension_tuple):
            item_path = os.path.join(folderpath,item)
            item_new_path = os.path.join(folder_path,item)
            shutil.move(item_path,item_new_path)
        # print('calling file finder')
        # print(file_finder(folderpath, extension_tuple))````
    return "task completed"