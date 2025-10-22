from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.upload_file_body import UploadFileBody
from ...models.upload_file_response_400 import UploadFileResponse400
from ...models.upload_file_response_401 import UploadFileResponse401
from ...models.upload_file_response_403 import UploadFileResponse403
from ...models.upload_file_response_404 import UploadFileResponse404
from ...models.upload_file_upload_file_ok import UploadFileUploadFileOk
from ...types import Response


def _get_kwargs(
    collection_id: str,
    *,
    body: UploadFileBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/weedremeed-api/upload/{collection_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        UploadFileResponse400,
        UploadFileResponse401,
        UploadFileResponse403,
        UploadFileResponse404,
        UploadFileUploadFileOk,
    ]
]:
    if response.status_code == 200:
        response_200 = UploadFileUploadFileOk.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = UploadFileResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = UploadFileResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = UploadFileResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = UploadFileResponse404.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        UploadFileResponse400,
        UploadFileResponse401,
        UploadFileResponse403,
        UploadFileResponse404,
        UploadFileUploadFileOk,
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UploadFileBody,
) -> Response[
    Union[
        UploadFileResponse400,
        UploadFileResponse401,
        UploadFileResponse403,
        UploadFileResponse404,
        UploadFileUploadFileOk,
    ]
]:
    """Upload file

    Args:
        collection_id (str):
        body (UploadFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UploadFileResponse400, UploadFileResponse401, UploadFileResponse403, UploadFileResponse404, UploadFileUploadFileOk]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UploadFileBody,
) -> Optional[
    Union[
        UploadFileResponse400,
        UploadFileResponse401,
        UploadFileResponse403,
        UploadFileResponse404,
        UploadFileUploadFileOk,
    ]
]:
    """Upload file

    Args:
        collection_id (str):
        body (UploadFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UploadFileResponse400, UploadFileResponse401, UploadFileResponse403, UploadFileResponse404, UploadFileUploadFileOk]
    """

    return sync_detailed(
        collection_id=collection_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UploadFileBody,
) -> Response[
    Union[
        UploadFileResponse400,
        UploadFileResponse401,
        UploadFileResponse403,
        UploadFileResponse404,
        UploadFileUploadFileOk,
    ]
]:
    """Upload file

    Args:
        collection_id (str):
        body (UploadFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UploadFileResponse400, UploadFileResponse401, UploadFileResponse403, UploadFileResponse404, UploadFileUploadFileOk]]
    """

    kwargs = _get_kwargs(
        collection_id=collection_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    collection_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UploadFileBody,
) -> Optional[
    Union[
        UploadFileResponse400,
        UploadFileResponse401,
        UploadFileResponse403,
        UploadFileResponse404,
        UploadFileUploadFileOk,
    ]
]:
    """Upload file

    Args:
        collection_id (str):
        body (UploadFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UploadFileResponse400, UploadFileResponse401, UploadFileResponse403, UploadFileResponse404, UploadFileUploadFileOk]
    """

    return (
        await asyncio_detailed(
            collection_id=collection_id,
            client=client,
            body=body,
        )
    ).parsed
