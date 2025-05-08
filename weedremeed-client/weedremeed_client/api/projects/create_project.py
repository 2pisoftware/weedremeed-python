from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_project_response_400 import CreateProjectResponse400
from ...models.create_project_response_401 import CreateProjectResponse401
from ...models.create_project_response_403 import CreateProjectResponse403
from ...models.create_project_response_409 import CreateProjectResponse409
from ...models.create_project_response_500 import CreateProjectResponse500
from ...models.project import Project
from ...models.project_create import ProjectCreate
from ...types import Response


def _get_kwargs(
    *,
    body: ProjectCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/weedremeed-api/project",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        CreateProjectResponse400,
        CreateProjectResponse401,
        CreateProjectResponse403,
        CreateProjectResponse409,
        CreateProjectResponse500,
        Project,
    ]
]:
    if response.status_code == 201:
        response_201 = Project.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = CreateProjectResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = CreateProjectResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = CreateProjectResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 409:
        response_409 = CreateProjectResponse409.from_dict(response.json())

        return response_409
    if response.status_code == 500:
        response_500 = CreateProjectResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        CreateProjectResponse400,
        CreateProjectResponse401,
        CreateProjectResponse403,
        CreateProjectResponse409,
        CreateProjectResponse500,
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
    *,
    client: AuthenticatedClient,
    body: ProjectCreate,
) -> Response[
    Union[
        CreateProjectResponse400,
        CreateProjectResponse401,
        CreateProjectResponse403,
        CreateProjectResponse409,
        CreateProjectResponse500,
        Project,
    ]
]:
    """Create project

     Creates a new record of type Project.

    Args:
        body (ProjectCreate): Data transfer object for creating a new Project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse403, CreateProjectResponse409, CreateProjectResponse500, Project]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ProjectCreate,
) -> Optional[
    Union[
        CreateProjectResponse400,
        CreateProjectResponse401,
        CreateProjectResponse403,
        CreateProjectResponse409,
        CreateProjectResponse500,
        Project,
    ]
]:
    """Create project

     Creates a new record of type Project.

    Args:
        body (ProjectCreate): Data transfer object for creating a new Project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse403, CreateProjectResponse409, CreateProjectResponse500, Project]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProjectCreate,
) -> Response[
    Union[
        CreateProjectResponse400,
        CreateProjectResponse401,
        CreateProjectResponse403,
        CreateProjectResponse409,
        CreateProjectResponse500,
        Project,
    ]
]:
    """Create project

     Creates a new record of type Project.

    Args:
        body (ProjectCreate): Data transfer object for creating a new Project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse403, CreateProjectResponse409, CreateProjectResponse500, Project]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProjectCreate,
) -> Optional[
    Union[
        CreateProjectResponse400,
        CreateProjectResponse401,
        CreateProjectResponse403,
        CreateProjectResponse409,
        CreateProjectResponse500,
        Project,
    ]
]:
    """Create project

     Creates a new record of type Project.

    Args:
        body (ProjectCreate): Data transfer object for creating a new Project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateProjectResponse400, CreateProjectResponse401, CreateProjectResponse403, CreateProjectResponse409, CreateProjectResponse500, Project]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
