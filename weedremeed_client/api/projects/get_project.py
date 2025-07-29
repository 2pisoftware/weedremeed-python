from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_project_response_400 import GetProjectResponse400
from ...models.get_project_response_401 import GetProjectResponse401
from ...models.get_project_response_403 import GetProjectResponse403
from ...models.get_project_response_404 import GetProjectResponse404
from ...models.get_project_response_500 import GetProjectResponse500
from ...models.project import Project
from ...types import Response


def _get_kwargs(
    project_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/weedremeed-api/project/{project_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        GetProjectResponse400,
        GetProjectResponse401,
        GetProjectResponse403,
        GetProjectResponse404,
        GetProjectResponse500,
        Project,
    ]
]:
    if response.status_code == 200:
        response_200 = Project.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = GetProjectResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = GetProjectResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = GetProjectResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = GetProjectResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = GetProjectResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        GetProjectResponse400,
        GetProjectResponse401,
        GetProjectResponse403,
        GetProjectResponse404,
        GetProjectResponse500,
        Project,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        GetProjectResponse400,
        GetProjectResponse401,
        GetProjectResponse403,
        GetProjectResponse404,
        GetProjectResponse500,
        Project,
    ]
]:
    """Get project

     Returns a record of type Project.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectResponse400, GetProjectResponse401, GetProjectResponse403, GetProjectResponse404, GetProjectResponse500, Project]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        GetProjectResponse400,
        GetProjectResponse401,
        GetProjectResponse403,
        GetProjectResponse404,
        GetProjectResponse500,
        Project,
    ]
]:
    """Get project

     Returns a record of type Project.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProjectResponse400, GetProjectResponse401, GetProjectResponse403, GetProjectResponse404, GetProjectResponse500, Project]
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        GetProjectResponse400,
        GetProjectResponse401,
        GetProjectResponse403,
        GetProjectResponse404,
        GetProjectResponse500,
        Project,
    ]
]:
    """Get project

     Returns a record of type Project.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetProjectResponse400, GetProjectResponse401, GetProjectResponse403, GetProjectResponse404, GetProjectResponse500, Project]]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        GetProjectResponse400,
        GetProjectResponse401,
        GetProjectResponse403,
        GetProjectResponse404,
        GetProjectResponse500,
        Project,
    ]
]:
    """Get project

     Returns a record of type Project.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetProjectResponse400, GetProjectResponse401, GetProjectResponse403, GetProjectResponse404, GetProjectResponse500, Project]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
