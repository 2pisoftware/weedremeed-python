from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.register_upload_part_body import RegisterUploadPartBody
from ...models.register_upload_part_register_upload_part_ok import RegisterUploadPartRegisterUploadPartOk
from ...models.register_upload_part_response_400 import RegisterUploadPartResponse400
from ...models.register_upload_part_response_500 import RegisterUploadPartResponse500
from ...types import Response


def _get_kwargs(
    *,
    body: RegisterUploadPartBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/file-multipart/ajax_part",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500 | None:
    if response.status_code == 200:
        response_200 = RegisterUploadPartRegisterUploadPartOk.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RegisterUploadPartResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = RegisterUploadPartResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RegisterUploadPartBody,
) -> Response[RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500]:
    """Register upload part

     Register a multipart upload part

    Args:
        body (RegisterUploadPartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500]
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
    client: AuthenticatedClient | Client,
    body: RegisterUploadPartBody,
) -> RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500 | None:
    """Register upload part

     Register a multipart upload part

    Args:
        body (RegisterUploadPartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RegisterUploadPartBody,
) -> Response[RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500]:
    """Register upload part

     Register a multipart upload part

    Args:
        body (RegisterUploadPartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RegisterUploadPartBody,
) -> RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500 | None:
    """Register upload part

     Register a multipart upload part

    Args:
        body (RegisterUploadPartBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RegisterUploadPartRegisterUploadPartOk | RegisterUploadPartResponse400 | RegisterUploadPartResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
