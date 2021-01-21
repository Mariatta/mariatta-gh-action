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
        pr_number = os.getenv('GH_PR_NUM')
        response = await gh.post(
            f'/repos/{os.getenv("GITHUB_REPOSITORY")}/issues/{pr_number}/comments',
            data={
                'body': 'Thanks for the PR!',
            }
        )


        # print(f"Issue created at {response['html_url']}")
        # issue_url = response["url"]
        # response = await gh.patch(issue_url, data={"state": "closed"})
        # print(response)
        # print("issue closed")


asyncio.run(main())