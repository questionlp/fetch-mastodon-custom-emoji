# fetch-mastodon-custom-emoji

A very rudimentary Python script that fetches the list of and downloads a copy of custom emojis from a Mastodon instance, using the custom emoji API endpoint. The script downloads each custom emoji, saving them into an output directory and names each file based on the custom emoji's short code.

This script requires Python 3.6 or newer, though it is only tested with Python 3.8 and 3.10.

## Setting Up the Script

Included in this repository is a `requirements.txt` file that includes any of the required packages that the script needs to run. To install the dependencies, run the following command (preferably in a virtual environment):

```bash
pip3 install -r requirements.txt
```

## Using the Script

In order to use the Python script to download custom emojis from a Mastodon instance, you will need to define the custom emoji API endpoint for that instance. By default, the custom emoji API endpoint path is `/api/v1/custom_emojis`.

For example, if you want to download custom emojis from a Mastodon instance available at `mastodon.example.org`, the default custom emoji API endpoint for that instance would be:

```text
https://mastodon.example.org/api/v1/custom_emojis
```

To use the script against any given custom emoji API endpoint, you would pass that URL as an argument when running the script:

```bash
python3 fetch.py [-o output-path] custom-emoji-api-endpoint
```

The `-o` option is used to save the downloaded custom emoji files to a specific location. By default, the script will create a directory named `output` (if it doesn't already exist) and save the files directly into the directory.

## Code of Conduct

This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to version 2.1 of the [Contributor Covenant](http://contributor-covenant.org) code of conduct. A copy of the [code of conduct](CODE_OF_CONDUCT.md) is included in this repository.

## License

This project is licensed under the terms of the [MIT License](LICENSE)
