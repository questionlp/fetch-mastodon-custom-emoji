# fetch-mastodon-custom-emoji

A very rudimentary Python script that fetches the list of custom emojis from a Mastodon API endpoint and downloads each custom emoji out, using the short code value as the file name.

This script requires Python 3.6 or newer, though it is only tested with Python 3.8 and 3.10.

## Using the Script

Currently, the API endpoint is defined within the script itself by setting a value to the `CUSTOM_EMOJIS_URL` variable.

This script requires [urllib3](https://pypi.org/project/urllib3/) to be installed and it is referenced in the included `requirements.txt` file.

With a valid API endpoint defined and the required dependencies are installed, running the script will fetch data from the API endpoint and loop through the results. For each custom emoji that it encounters, it will download the image, using the emoji's short code as the file name and writes out to the `output` directory.

## Code of Conduct

This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to version 2.1 of the [Contributor Covenant](http://contributor-covenant.org) code of conduct. A copy of the [code of conduct](CODE_OF_CONDUCT.md) is included in this repository.

## License

This project is licensed under the terms of the [MIT License](LICENSE)
