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

async def get_workspace_for_ip(client: ResearchCloudClient) -> dict:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
    local_ip_address = s.getsockname()[0]
    s.close()
    result: list[dict] = await client.workspaces.list(
        attribute_filters={
            "resource_meta.ip": local_ip_address
        },
    )
    if result:
        return result[0]
    else:
        raise RuntimeError(f"No workspace found for the current IP address {local_ip_address}")


async def pause(token: str = ""):
    client = get_client(token)
    workspace = await get_workspace_for_ip(client)
    return await client.workspaces.pause(workspace["id"])
