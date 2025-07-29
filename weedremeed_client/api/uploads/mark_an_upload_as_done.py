from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.mark_an_upload_as_done_mark_an_upload_as_done_ok import MarkAnUploadAsDoneMarkAnUploadAsDoneOk
from ...models.mark_an_upload_as_done_response_400 import MarkAnUploadAsDoneResponse400
from ...models.mark_an_upload_as_done_response_500 import MarkAnUploadAsDoneResponse500
from ...types import Response


def _get_kwargs(
    upload_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/file-multipart/ajax_done/{upload_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]
]:
    if response.status_code == 200:
        response_200 = MarkAnUploadAsDoneMarkAnUploadAsDoneOk.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = MarkAnUploadAsDoneResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = MarkAnUploadAsDoneResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    upload_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]
]:
    """Mark an upload as done

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]]
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
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]
]:
    """Mark an upload as done

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]
    """

    return sync_detailed(
        upload_id=upload_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    upload_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]
]:
    """Mark an upload as done

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]]
    """

    kwargs = _get_kwargs(
        upload_id=upload_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    upload_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]
]:
    """Mark an upload as done

    Args:
        upload_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MarkAnUploadAsDoneMarkAnUploadAsDoneOk, MarkAnUploadAsDoneResponse400, MarkAnUploadAsDoneResponse500]
    """

    return (
        await asyncio_detailed(
            upload_id=upload_id,
            client=client,
        )
    ).parsed
