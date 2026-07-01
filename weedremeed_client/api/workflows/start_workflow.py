from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.start_workflow_response_400 import StartWorkflowResponse400
from ...models.start_workflow_response_401 import StartWorkflowResponse401
from ...models.start_workflow_response_403 import StartWorkflowResponse403
from ...models.start_workflow_response_404 import StartWorkflowResponse404
from ...models.start_workflow_response_500 import StartWorkflowResponse500
from ...types import Response


def _get_kwargs(
    workflow_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/weedremeed-api/start/{workflow_id}".format(
            workflow_id=quote(str(workflow_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    None
    | StartWorkflowResponse400
    | StartWorkflowResponse401
    | StartWorkflowResponse403
    | StartWorkflowResponse404
    | StartWorkflowResponse500
    | None
):
    if response.status_code == 204:
        response_204 = cast(None, response.json())
        return response_204

    if response.status_code == 400:
        response_400 = StartWorkflowResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = StartWorkflowResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = StartWorkflowResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = StartWorkflowResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = StartWorkflowResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    None
    | StartWorkflowResponse400
    | StartWorkflowResponse401
    | StartWorkflowResponse403
    | StartWorkflowResponse404
    | StartWorkflowResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    None
    | StartWorkflowResponse400
    | StartWorkflowResponse401
    | StartWorkflowResponse403
    | StartWorkflowResponse404
    | StartWorkflowResponse500
]:
    """Start workflow

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[None | StartWorkflowResponse400 | StartWorkflowResponse401 | StartWorkflowResponse403 | StartWorkflowResponse404 | StartWorkflowResponse500]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    None
    | StartWorkflowResponse400
    | StartWorkflowResponse401
    | StartWorkflowResponse403
    | StartWorkflowResponse404
    | StartWorkflowResponse500
    | None
):
    """Start workflow

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        None | StartWorkflowResponse400 | StartWorkflowResponse401 | StartWorkflowResponse403 | StartWorkflowResponse404 | StartWorkflowResponse500
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    None
    | StartWorkflowResponse400
    | StartWorkflowResponse401
    | StartWorkflowResponse403
    | StartWorkflowResponse404
    | StartWorkflowResponse500
]:
    """Start workflow

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[None | StartWorkflowResponse400 | StartWorkflowResponse401 | StartWorkflowResponse403 | StartWorkflowResponse404 | StartWorkflowResponse500]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    None
    | StartWorkflowResponse400
    | StartWorkflowResponse401
    | StartWorkflowResponse403
    | StartWorkflowResponse404
    | StartWorkflowResponse500
    | None
):
    """Start workflow

    Args:
        workflow_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        None | StartWorkflowResponse400 | StartWorkflowResponse401 | StartWorkflowResponse403 | StartWorkflowResponse404 | StartWorkflowResponse500
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
        )
    ).parsed
