from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachment import Attachment
from ...models.get_attachment_response_400 import GetAttachmentResponse400
from ...models.get_attachment_response_401 import GetAttachmentResponse401
from ...models.get_attachment_response_403 import GetAttachmentResponse403
from ...models.get_attachment_response_404 import GetAttachmentResponse404
from ...models.get_attachment_response_500 import GetAttachmentResponse500
from ...types import Response


def _get_kwargs(
    attachment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/weedremeed-api/attachment/{attachment_id}".format(
            attachment_id=quote(str(attachment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Attachment
    | GetAttachmentResponse400
    | GetAttachmentResponse401
    | GetAttachmentResponse403
    | GetAttachmentResponse404
    | GetAttachmentResponse500
    | None
):
    if response.status_code == 200:
        response_200 = Attachment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetAttachmentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetAttachmentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetAttachmentResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetAttachmentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetAttachmentResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Attachment
    | GetAttachmentResponse400
    | GetAttachmentResponse401
    | GetAttachmentResponse403
    | GetAttachmentResponse404
    | GetAttachmentResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Attachment
    | GetAttachmentResponse400
    | GetAttachmentResponse401
    | GetAttachmentResponse403
    | GetAttachmentResponse404
    | GetAttachmentResponse500
]:
    """Get attachment

     Returns an Attachment. You may only fetch user-uploaded attachments via this endpoint. For tool
    output, you must paginate /weedremeed-api/content/{collection_id}

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attachment | GetAttachmentResponse400 | GetAttachmentResponse401 | GetAttachmentResponse403 | GetAttachmentResponse404 | GetAttachmentResponse500]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Attachment
    | GetAttachmentResponse400
    | GetAttachmentResponse401
    | GetAttachmentResponse403
    | GetAttachmentResponse404
    | GetAttachmentResponse500
    | None
):
    """Get attachment

     Returns an Attachment. You may only fetch user-uploaded attachments via this endpoint. For tool
    output, you must paginate /weedremeed-api/content/{collection_id}

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Attachment | GetAttachmentResponse400 | GetAttachmentResponse401 | GetAttachmentResponse403 | GetAttachmentResponse404 | GetAttachmentResponse500
    """

    return sync_detailed(
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    Attachment
    | GetAttachmentResponse400
    | GetAttachmentResponse401
    | GetAttachmentResponse403
    | GetAttachmentResponse404
    | GetAttachmentResponse500
]:
    """Get attachment

     Returns an Attachment. You may only fetch user-uploaded attachments via this endpoint. For tool
    output, you must paginate /weedremeed-api/content/{collection_id}

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attachment | GetAttachmentResponse400 | GetAttachmentResponse401 | GetAttachmentResponse403 | GetAttachmentResponse404 | GetAttachmentResponse500]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attachment_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> (
    Attachment
    | GetAttachmentResponse400
    | GetAttachmentResponse401
    | GetAttachmentResponse403
    | GetAttachmentResponse404
    | GetAttachmentResponse500
    | None
):
    """Get attachment

     Returns an Attachment. You may only fetch user-uploaded attachments via this endpoint. For tool
    output, you must paginate /weedremeed-api/content/{collection_id}

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Attachment | GetAttachmentResponse400 | GetAttachmentResponse401 | GetAttachmentResponse403 | GetAttachmentResponse404 | GetAttachmentResponse500
    """

    return (
        await asyncio_detailed(
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
