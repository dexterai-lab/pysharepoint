# PySharepoint

PySharepoint is a Python library that provides an interface to interact with Microsoft Sharepoint.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pysharepoint
```

## Usage

```python
import pysharepoint as ps

sharepoint_base_url = 'https://<abc>.sharepoint.com/'
username = 'username'
password = 'password'

site = ps.SPInterface(sharepoint_base_url,username,password)

source_path = 'Shared Documents/Shared/<Location>'
sink_path = '/full_sink_path/'
filename = 'filename.ext'
sharepoint_site = 'https://<abc>.sharepoint.com/sites/<site_name>'

site.download_file_sharepoint(source_path, sink_path,filename,sharepoint_site)
site.upload_file_sharepoint(source_path, sink_path,filename,sharepoint_site)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://github.com/dexterai-lab/pysharepoint/blob/master/LICENSE)
