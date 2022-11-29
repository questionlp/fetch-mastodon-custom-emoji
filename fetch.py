import json
import os
import shutil
import sys
import urllib3

# Set API endpoint used to retrieve custom emojis
CUSTOM_EMOJIS_URL = ""

http = urllib3.PoolManager()
custom_emojis_req = http.request("GET", CUSTOM_EMOJIS_URL)

# Fetch and loop through the results, if the response status is 200
if custom_emojis_req.status == 200:
    custom_emojis_json = custom_emojis_req.data
    custom_emojis_req.release_conn()
    custom_emojis = json.loads(custom_emojis_json.decode("utf-8"))

    # Check to see if output directory exists, and create if necessary
    if not os.path.exists("output"):
        try:
            os.makedirs("output", exist_ok=True)
        except:
            print("Error: Unable to create 'output' directory.")
            sys.exit(1)

    for custom_emoji in custom_emojis:
        short_code = custom_emoji["shortcode"]
        url = custom_emoji["url"]

        # TODO: This logic assumes that all custom emojis are in PNG format
        # though GIF is also supported. Need to update logic to use the
        # file extension that is provided in the URL
        file_path = os.path.join("output", f"{short_code}.png")

        with http.request("GET", url, preload_content=False) as resp, open(file_path, "wb") as emoji:
            shutil.copyfileobj(resp, emoji)

        resp.release_conn()
else:
    custom_emojis_req.release_conn()
