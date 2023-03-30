import time
from typing import Optional, List, Dict, Any

from openai import util
from openai.api_resources.abstract.engine_api_resource import EngineAPIResource
from openai.error import TryAgain


class ChatCompletion(EngineAPIResource):
    engine_required = False
    OBJECT_NAME = "chat.completions"

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        request_id: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        timeout: Optional[float] = None,
        model: Optional[str] = None,
        messages: Optional[List[Dict[str, Any]]] = None,
        **params,
    ):
        """
        Creates a new chat completion for the provided messages and parameters.

        See https://platform.openai.com/docs/api-reference/chat-completions/create
        for a list of valid parameters.
        """
        start = time.time()

        while True:
            try:
                return super().create(
                    api_key=api_key,
                    api_base=api_base,
                    api_type=api_type,
                    api_version=api_version,
                    request_id=request_id,
                    organization=organization,
                    model=model,
                    messages=messages,
                    **params
                )
            except TryAgain as e:
                if timeout is not None and time.time() > start + timeout:
                    raise

                util.log_info("Waiting for model to warm up", error=e)

    @classmethod
    async def acreate(
        cls,
        api_key: Optional[str] = None,
        api_base: Optional[str] = None,
        api_type: Optional[str] = None,
        request_id: Optional[str] = None,
        api_version: Optional[str] = None,
        organization: Optional[str] = None,
        timeout: Optional[float] = None,
        model: Optional[str] = None,
        messages: Optional[List[Dict[str, Any]]] = None,
        **params,
    ):
        """
        Creates a new chat completion for the provided messages and parameters.

        See https://platform.openai.com/docs/api-reference/chat-completions/create
        for a list of valid parameters.
        """
        start = time.time()

        while True:
            try:
                return await super().acreate(
                    api_key=api_key,
                    api_base=api_base,
                    api_type=api_type,
                    api_version=api_version,
                    request_id=request_id,
                    organization=organization,
                    model=model,
                    messages=messages,
                    **params
                )
            except TryAgain as e:
                if timeout is not None and time.time() > start + timeout:
                    raise

                util.log_info("Waiting for model to warm up", error=e)
