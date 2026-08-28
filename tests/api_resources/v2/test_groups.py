# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from sendblue_api import SendblueAPI, AsyncSendblueAPI
from sendblue_api.types.v2 import GroupRenameResponse, GroupRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: SendblueAPI) -> None:
        group = client.v2.groups.retrieve(
            "sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
        )
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: SendblueAPI) -> None:
        response = client.v2.groups.with_raw_response.retrieve(
            "sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: SendblueAPI) -> None:
        with client.v2.groups.with_streaming_response.retrieve(
            "sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupRetrieveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.v2.groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_rename(self, client: SendblueAPI) -> None:
        group = client.v2.groups.rename(
            group_id="sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
            group_name="Project Falcon",
        )
        assert_matches_type(GroupRenameResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_rename(self, client: SendblueAPI) -> None:
        response = client.v2.groups.with_raw_response.rename(
            group_id="sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
            group_name="Project Falcon",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupRenameResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_rename(self, client: SendblueAPI) -> None:
        with client.v2.groups.with_streaming_response.rename(
            group_id="sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
            group_name="Project Falcon",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupRenameResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_rename(self, client: SendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            client.v2.groups.with_raw_response.rename(
                group_id="",
                group_name="Project Falcon",
            )


class TestAsyncGroups:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        group = await async_client.v2.groups.retrieve(
            "sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
        )
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.v2.groups.with_raw_response.retrieve(
            "sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupRetrieveResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.v2.groups.with_streaming_response.retrieve(
            "sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupRetrieveResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.v2.groups.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_rename(self, async_client: AsyncSendblueAPI) -> None:
        group = await async_client.v2.groups.rename(
            group_id="sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
            group_name="Project Falcon",
        )
        assert_matches_type(GroupRenameResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_rename(self, async_client: AsyncSendblueAPI) -> None:
        response = await async_client.v2.groups.with_raw_response.rename(
            group_id="sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
            group_name="Project Falcon",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupRenameResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_rename(self, async_client: AsyncSendblueAPI) -> None:
        async with async_client.v2.groups.with_streaming_response.rename(
            group_id="sb_group_608acc54-d0d7-4b41-8092-9ff6e1e70455",
            group_name="Project Falcon",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupRenameResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_rename(self, async_client: AsyncSendblueAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_id` but received ''"):
            await async_client.v2.groups.with_raw_response.rename(
                group_id="",
                group_name="Project Falcon",
            )
