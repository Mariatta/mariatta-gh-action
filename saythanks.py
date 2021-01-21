import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI
import json
async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(
            session,
            "mariatta",
            oauth_token=os.getenv("GH_AUTH")
        )
        gh_ref = os.getenv("GITHUB_REF")
        print(gh_ref)

        payload_file = os.getenv("GITHUB_EVENT_PATH")
        with open(payload_file) as json_file:
            payload = json.load(json_file)
            print(payload)
        # response = await gh.post(
        #     f'/repos/{os.getenv("GITHUB_REPOSITORY")}/issues',
        #     data={
        #         'title': 'test it',
        #         'body': 'in action',
        #     }
        # )
        # print(f"Issue created at {response['html_url']}")
        # issue_url = response["url"]
        # response = await gh.patch(issue_url, data={"state": "closed"})
        # print(response)
        # print("issue closed")


asyncio.run(main())