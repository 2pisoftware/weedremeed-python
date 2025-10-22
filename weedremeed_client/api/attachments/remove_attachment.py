from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_attachment_response_400 import RemoveAttachmentResponse400
from ...models.remove_attachment_response_401 import RemoveAttachmentResponse401
from ...models.remove_attachment_response_403 import RemoveAttachmentResponse403
from ...models.remove_attachment_response_404 import RemoveAttachmentResponse404
from ...models.remove_attachment_response_500 import RemoveAttachmentResponse500
from ...types import Response


def _get_kwargs(
    attachment_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/weedremeed-api/attachment/{attachment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        None,
        RemoveAttachmentResponse400,
        RemoveAttachmentResponse401,
        RemoveAttachmentResponse403,
        RemoveAttachmentResponse404,
        RemoveAttachmentResponse500,
    ]
]:
    if response.status_code == 204:
        response_204 = cast(None, response.json())
        return response_204

    if response.status_code == 400:
        response_400 = RemoveAttachmentResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RemoveAttachmentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = RemoveAttachmentResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = RemoveAttachmentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = RemoveAttachmentResponse500.from_dict(response.json())

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
        RemoveAttachmentResponse400,
        RemoveAttachmentResponse401,
        RemoveAttachmentResponse403,
        RemoveAttachmentResponse404,
        RemoveAttachmentResponse500,
    ]
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
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        None,
        RemoveAttachmentResponse400,
        RemoveAttachmentResponse401,
        RemoveAttachmentResponse403,
        RemoveAttachmentResponse404,
        RemoveAttachmentResponse500,
    ]
]:
    """Delete attachment

     Delete an Attachment. You may only delete user-uploaded Attachments. For deleting tool output, you
    must delete the Collection which results in deleting all Attachments within.

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[None, RemoveAttachmentResponse400, RemoveAttachmentResponse401, RemoveAttachmentResponse403, RemoveAttachmentResponse404, RemoveAttachmentResponse500]]
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
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        None,
        RemoveAttachmentResponse400,
        RemoveAttachmentResponse401,
        RemoveAttachmentResponse403,
        RemoveAttachmentResponse404,
        RemoveAttachmentResponse500,
    ]
]:
    """Delete attachment

     Delete an Attachment. You may only delete user-uploaded Attachments. For deleting tool output, you
    must delete the Collection which results in deleting all Attachments within.

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[None, RemoveAttachmentResponse400, RemoveAttachmentResponse401, RemoveAttachmentResponse403, RemoveAttachmentResponse404, RemoveAttachmentResponse500]
    """

    return sync_detailed(
        attachment_id=attachment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[
        None,
        RemoveAttachmentResponse400,
        RemoveAttachmentResponse401,
        RemoveAttachmentResponse403,
        RemoveAttachmentResponse404,
        RemoveAttachmentResponse500,
    ]
]:
    """Delete attachment

     Delete an Attachment. You may only delete user-uploaded Attachments. For deleting tool output, you
    must delete the Collection which results in deleting all Attachments within.

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[None, RemoveAttachmentResponse400, RemoveAttachmentResponse401, RemoveAttachmentResponse403, RemoveAttachmentResponse404, RemoveAttachmentResponse500]]
    """

    kwargs = _get_kwargs(
        attachment_id=attachment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    attachment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[
        None,
        RemoveAttachmentResponse400,
        RemoveAttachmentResponse401,
        RemoveAttachmentResponse403,
        RemoveAttachmentResponse404,
        RemoveAttachmentResponse500,
    ]
]:
    """Delete attachment

     Delete an Attachment. You may only delete user-uploaded Attachments. For deleting tool output, you
    must delete the Collection which results in deleting all Attachments within.

    Args:
        attachment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[None, RemoveAttachmentResponse400, RemoveAttachmentResponse401, RemoveAttachmentResponse403, RemoveAttachmentResponse404, RemoveAttachmentResponse500]
    """

    return (
        await asyncio_detailed(
            attachment_id=attachment_id,
            client=client,
        )
    ).parsed
