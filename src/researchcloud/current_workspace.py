import socket

from .client import ResearchCloudClient


def get_client(token: str = "") -> ResearchCloudClient:
    if token:
        env = {
            "RESEARCH_CLOUD_TOKEN": token,
        }
    else:
        env = None
    return ResearchCloudClient().from_env(env=env)

async def get_workspace_for_current_ip(client: ResearchCloudClient) -> dict:
    hostname = socket.gethostname()
    result: list[dict] = await client.workspaces.list(
        attribute_filters={
            "resource_meta.workspace_fqdn": hostname
        },
    )
    if result:
        return result[0]
    else:
        raise RuntimeError(f"No workspace found for the current hostname {hostname}")


async def pause(token: str = ""):
    client = get_client(token)
    workspace = await get_workspace_for_current_ip(client)
    return await client.workspaces.pause(workspace["id"])
