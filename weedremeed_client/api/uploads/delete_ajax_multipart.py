from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_ajax_multipart_response_400 import DeleteAjaxMultipartResponse400
from ...models.delete_ajax_multipart_response_500 import DeleteAjaxMultipartResponse500
from ...types import Response


def _get_kwargs(
    upload_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/file-multipart/ajax_multipart/{upload_id}".format(
            upload_id=quote(str(upload_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None | None:
    if response.status_code == 200:
        response_200 = cast(None, response.json())
        return response_200

    if response.status_code == 400:
        response_400 = DeleteAjaxMultipartResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = DeleteAjaxMultipartResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None]:
    """Abort a multipart upload

     Abort a multipart upload

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None]
    """

    kwargs = _get_kwargs(
        upload_id=upload_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None | None:
    """Abort a multipart upload

     Abort a multipart upload

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None
    """

    return sync_detailed(
        upload_id=upload_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None]:
    """Abort a multipart upload

     Abort a multipart upload

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None]
    """

    kwargs = _get_kwargs(
        upload_id=upload_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    upload_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None | None:
    """Abort a multipart upload

     Abort a multipart upload

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAjaxMultipartResponse400 | DeleteAjaxMultipartResponse500 | None
    """

    return (
        await asyncio_detailed(
            upload_id=upload_id,
            client=client,
        )
    ).parsed
