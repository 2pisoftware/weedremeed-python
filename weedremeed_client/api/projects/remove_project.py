from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_project_response_400 import RemoveProjectResponse400
from ...models.remove_project_response_401 import RemoveProjectResponse401
from ...models.remove_project_response_403 import RemoveProjectResponse403
from ...models.remove_project_response_404 import RemoveProjectResponse404
from ...models.remove_project_response_500 import RemoveProjectResponse500
from ...types import Response


def _get_kwargs(
    project_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/weedremeed-api/project/{project_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        None,
        RemoveProjectResponse400,
        RemoveProjectResponse401,
        RemoveProjectResponse403,
        RemoveProjectResponse404,
        RemoveProjectResponse500,
    ]
]:
    if response.status_code == 204:
        response_204 = cast(None, response.json())
        return response_204
    if response.status_code == 400:
        response_400 = RemoveProjectResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = RemoveProjectResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = RemoveProjectResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = RemoveProjectResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = RemoveProjectResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        None,
        RemoveProjectResponse400,
        RemoveProjectResponse401,
        RemoveProjectResponse403,
        RemoveProjectResponse404,
        RemoveProjectResponse500,
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
        None,
        RemoveProjectResponse400,
        RemoveProjectResponse401,
        RemoveProjectResponse403,
        RemoveProjectResponse404,
        RemoveProjectResponse500,
    ]
]:
    """Delete project

     Deletes a record of type Project.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[None, RemoveProjectResponse400, RemoveProjectResponse401, RemoveProjectResponse403, RemoveProjectResponse404, RemoveProjectResponse500]]
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
        None,
        RemoveProjectResponse400,
        RemoveProjectResponse401,
        RemoveProjectResponse403,
        RemoveProjectResponse404,
        RemoveProjectResponse500,
    ]
]:
    """Delete project

     Deletes a record of type Project.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[None, RemoveProjectResponse400, RemoveProjectResponse401, RemoveProjectResponse403, RemoveProjectResponse404, RemoveProjectResponse500]
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
        None,
        RemoveProjectResponse400,
        RemoveProjectResponse401,
        RemoveProjectResponse403,
        RemoveProjectResponse404,
        RemoveProjectResponse500,
    ]
]:
    """Delete project

     Deletes a record of type Project.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[None, RemoveProjectResponse400, RemoveProjectResponse401, RemoveProjectResponse403, RemoveProjectResponse404, RemoveProjectResponse500]]
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
        None,
        RemoveProjectResponse400,
        RemoveProjectResponse401,
        RemoveProjectResponse403,
        RemoveProjectResponse404,
        RemoveProjectResponse500,
    ]
]:
    """Delete project

     Deletes a record of type Project.

    Args:
        project_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[None, RemoveProjectResponse400, RemoveProjectResponse401, RemoveProjectResponse403, RemoveProjectResponse404, RemoveProjectResponse500]
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
        )
    ).parsed
