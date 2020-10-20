import os
import pandas as pd
from shareplum import Site
from shareplum import Office365
from shareplum.site import Version


class SPInterface:
    """This is a class to interact with Sharepoint from Python"""

    def __init__(self, sharepoint_base_url, username, password):
        self.username = username
        self.password = password
        self.sharepoint_base_url = sharepoint_base_url
        self.authcookie = Office365(sharepoint_base_url, username=username, password=password).GetCookies()


    def download_file_sharepoint(self, source_path, sink_path, filename, sharepoint_site):
        """This fucntion will download a file from the Sharepoint to specified sink path.
        Parameters:
            source_path = r'Shared Documents/Shared/<Location>'
            sink_path = r'/full_sink_path/'
            filename = 'filename.ext'
            sharepoint_site = 'https://xxx.sharepoint.com/sites/<site_name>'
        """
        site = Site(sharepoint_site, version=Version.v2016, authcookie=self.authcookie)
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
                print("Attempt #No: ", attempt)
                print("Downlowded file size is ", round(os.path.getsize(full_sink_path) / 1024, 2), " KB")
            except Exception as e:
                if (attempt < 2):
                    print("Try again!")
                    continue
                print("Error", e)
                raise e
            break


    def upload_file_sharepoint(self, source_path, sink_path, filename, sharepoint_site):
        """This fucntion will upload a file from the source path to Sharepoint.
        Parameters:
            source_path = r'/full_sink_path/'
            sink_path = r'Shared Documents/Shared/<Location>'
            filename = 'filename.ext'
            sharepoint_site = 'https://xxx.sharepoint.com/sites/<site_name>'
        """
        site = Site(sharepoint_site, version=Version.v2016, authcookie=self.authcookie)
        full_source_path = os.path.join(source_path, filename)
        full_sink_path = os.path.join(sink_path, filename)
        print(full_source_path)
        print(full_sink_path)
        folder = site.Folder(sink_path)
        with open(full_source_path, mode='rb') as file:
            filecontent = file.read()
        for attempt in range(0, 3):
            try:
              folder.upload_file(filecontent, full_sink_path)
              print ("Attempt #No:", attempt)
            except Exception as e:
              if(attempt<2):
                print("Trying again!")
                continue
              print("Error", e)
              raise e
            break

    def list_item_sharepoint(self, directory_path, sharepoint_site):
        site = Site(sharepoint_site, version=Version.v2016, authcookie=self.authcookie)
        folder_source = site.Folder(directory_path)
        #get files in a directory
        files_item = folder_source.files

        items_df = pd.DataFrame()
        for i in files_item:
            items_df = items_df.append(pd.DataFrame.from_dict([i]))

        if len(items_df) > 0:
            # subset the columns
            subset_cols = ['Length', 'LinkingUrl', 'MajorVersion','MinorVersion', 'Name', 'TimeCreated', 'TimeLastModified']
            items_df = items_df[subset_cols]

            #parse url to remove everything after ? mark
            items_df['LinkingUrl'] = [ i.split('?')[0] for i in items_df['LinkingUrl']]
            # convert bytes to KB
            items_df['Length'] = [round(int(i)/1000,2) for i in items_df['Length']]
            #sort based on file names
            items_df.sort_values('Name', inplace=True)

            # rename to more friendlier names
            items_df.columns = ['FileSize', 'FullFileUrl', 'FileVersion','MinorVersion', 'FileName', 'TimeCreated', 'TimeLastModified']
            return items_df
        else:
            print(f'No files in {directory_path} directory')
            return pd.DataFrame()

def main():
    """Main function"""
    pass

if __name__ == '__main__':
    main()
