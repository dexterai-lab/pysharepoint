import os
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version

# Replace the scope and key to your own Service Account credentials on Azure Keyvault

authcookie = Office365('https://abc.sharepoint.com', username='username@abc.com', password='password').GetCookies()
sharepoint_site='https://abc.sharepoint.com/sites/FVCDevOps/'

class SPInterface:
    """This is a class to interact with Sharepoint from Python"""

    def __init__(self, sharepoint_site, username, password):
        self.username = username
        self.password = password
        self.sharepoint_site = sharepoint_site


    def download_file_sharepoint(self,source_path, sink_path, filename, sharepoint_site):
        site = Site(sharepoint_site, version=Version.v2016, authcookie=authcookie)
        full_source_path = os.path.join(source_path, filename)
        full_sink_path = os.path.join(sink_path, filename)
        print(full_source_path)
        print(full_sink_path)
        folder = site.Folder(source_path)
        for attempt in range(0, 3):
            try:
                output_file = open(full_sink_path, 'wb')
                input_file = folder.get_file(filename)
                binary_format = bytearray(input_file)
                output_file.write(binary_format)
                output_file.close()
                print("output file size is ", round(os.path.getsize(full_sink_path) / 1024, 2), " KB")
                print("Attempt No:", attempt)
            except Exception as e:
                if (attempt < 2):
                    print("Try again!")
                    continue
                print("Error", e)
                raise e
            break


    def upload_file_sharepoint(self, source_path,sink_path,filename,sharepoint_site):
      site = Site(sharepoint_site, version=Version.v2016, authcookie=authcookie)
      full_source_path=os.path.join(source_path,filename)
      full_sink_path=os.path.join(sink_path,filename)
      print(full_source_path)
      print(full_sink_path)
      folder = site.Folder(sink_path)
      with open(full_source_path, mode='rb') as file:
        filecontent = file.read()
      for attempt in range(0,3):
        try:
          folder.upload_file(filecontent, full_sink_path)
          print("Attempt No:", attempt)
        except Exception as e:
          if(attempt<2):
            print("Try again!")
            continue
          print("Error", e)
          raise e
        break


def main():
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
