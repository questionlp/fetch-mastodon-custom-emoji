import argparse
import json
import pathlib
import sys

import urllib3

# Use argparse to add arguments and flags that will be used in the main
# portion of the script
parser = argparse.ArgumentParser(
    description="Fetches custom emojis from a Mastodon instance"
)
parser.add_argument("endpoint", type=str, help="Custom emoji API endpoint URL")
parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Fetch and parse custom emojis, but do not download any files",
)
parser.add_argument(
    "--output",
    "-o",
    type=str,
    default="output",
    help="Output path for the downloaded custom emojis",
)
args = parser.parse_args()

# Only continue if an API endpoint is provided
if args.endpoint:
    http = urllib3.PoolManager()
    try:
        custom_emojis_req = http.request("GET", args.endpoint)

        # Fetch data from the custom emoji API endpoint
        if custom_emojis_req.status == 200:
            custom_emojis_json = custom_emojis_req.data
            custom_emojis_req.release_conn()
            custom_emojis = json.loads(custom_emojis_json.decode("utf-8"))

            # Create an absolute path from the output argument
            output_path = pathlib.Path(args.output)
            path = output_path.resolve()

            if not args.dry_run:
                # Check to see if output path exists, create if necessary,
                # or if the output path is a directory
                if not path.exists():
                    try:
                        path.mkdir()
                    except PermissionError:
                        print(f"Error: Unable to create {path} directory. Exiting.")
                        sys.exit(1)
                elif not path.is_dir():
                    print(f"{path} is not a directory. Exiting.")
                    sys.exit(1)

            # Loop through each custom emoji in the response data and
            # download the files to the requested output path
            for custom_emoji in custom_emojis:
                short_code = custom_emoji["shortcode"]
                url = custom_emoji["static_url"]

                # Parse the URL for the custom emoji and get the file
                # extension
                source_file_url = urllib3.util.parse_url(url)
                source_file_path = source_file_url.path
                source_file_ext = pathlib.Path(source_file_path).suffix

                # Generate the output file path
                file_path = path / f"{short_code}{source_file_ext}"
                short_file_path = output_path / f"{short_code}{source_file_ext}"

                if args.dry_run:
                    print(f"[DRY RUN] Fetching {source_file_path} -> {short_file_path}")
                if not args.dry_run:
                    print(f"Fetching {source_file_path} -> {short_file_path}")
                    emoji = http.request("GET", url, preload_content=False)

                    if emoji.status == 200:
                        file_path.write_bytes(emoji.data)
                        emoji.release_conn()
                    else:
                        print(f"Skipping {url} due to HTTP status code {emoji.status}.")
        else:
            custom_emojis_req.release_conn()
    except (urllib3.exceptions.NewConnectionError, urllib3.exceptions.MaxRetryError):
        print("Unable to access API endpoint provided. Exiting.")
        sys.exit(1)
else:
    print("No API endpoint provided. Exiting.")
    sys.exit(1)
