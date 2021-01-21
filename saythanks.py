import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI

async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(
            session,
            "mariatta",
            oauth_token=os.getenv("GH_AUTH")
        )
        gh_ref = os.getenv("GH_REF")
        print(gh_ref)
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