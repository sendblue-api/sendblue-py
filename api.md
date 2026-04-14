# Messages

Types:

```python
from sendblue_api.types import (
    MessageContent,
    MessageResponse,
    MessageRetrieveResponse,
    MessageListResponse,
)
```

Methods:

- <code title="get /api/v2/messages/{message_id}">client.messages.<a href="./src/sendblue_api/resources/messages.py">retrieve</a>(message_id) -> <a href="./src/sendblue_api/types/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="get /api/v2/messages">client.messages.<a href="./src/sendblue_api/resources/messages.py">list</a>(\*\*<a href="src/sendblue_api/types/message_list_params.py">params</a>) -> <a href="./src/sendblue_api/types/message_list_response.py">MessageListResponse</a></code>
- <code title="get /api/status">client.messages.<a href="./src/sendblue_api/resources/messages.py">get_status</a>(\*\*<a href="src/sendblue_api/types/message_get_status_params.py">params</a>) -> <a href="./src/sendblue_api/types/message_response.py">MessageResponse</a></code>
- <code title="post /api/send-message">client.messages.<a href="./src/sendblue_api/resources/messages.py">send</a>(\*\*<a href="src/sendblue_api/types/message_send_params.py">params</a>) -> <a href="./src/sendblue_api/types/message_response.py">MessageResponse</a></code>

# Groups

Types:

```python
from sendblue_api.types import GroupModifyResponse
```

Methods:

- <code title="post /api/modify-group">client.groups.<a href="./src/sendblue_api/resources/groups.py">modify</a>(\*\*<a href="src/sendblue_api/types/group_modify_params.py">params</a>) -> <a href="./src/sendblue_api/types/group_modify_response.py">GroupModifyResponse</a></code>
- <code title="post /api/send-group-message">client.groups.<a href="./src/sendblue_api/resources/groups.py">send_message</a>(\*\*<a href="src/sendblue_api/types/group_send_message_params.py">params</a>) -> <a href="./src/sendblue_api/types/message_response.py">MessageResponse</a></code>

# MediaObjects

Types:

```python
from sendblue_api.types import MediaObjectUploadResponse
```

Methods:

- <code title="post /api/upload-media-object">client.media_objects.<a href="./src/sendblue_api/resources/media_objects.py">upload</a>(\*\*<a href="src/sendblue_api/types/media_object_upload_params.py">params</a>) -> <a href="./src/sendblue_api/types/media_object_upload_response.py">MediaObjectUploadResponse</a></code>

# Lookups

Types:

```python
from sendblue_api.types import LookupLookupNumberResponse
```

Methods:

- <code title="get /api/evaluate-service">client.lookups.<a href="./src/sendblue_api/resources/lookups.py">lookup_number</a>(\*\*<a href="src/sendblue_api/types/lookup_lookup_number_params.py">params</a>) -> <a href="./src/sendblue_api/types/lookup_lookup_number_response.py">LookupLookupNumberResponse</a></code>

# TypingIndicators

Types:

```python
from sendblue_api.types import TypingIndicatorSendResponse
```

Methods:

- <code title="post /api/send-typing-indicator">client.typing_indicators.<a href="./src/sendblue_api/resources/typing_indicators.py">send</a>(\*\*<a href="src/sendblue_api/types/typing_indicator_send_params.py">params</a>) -> <a href="./src/sendblue_api/types/typing_indicator_send_response.py">TypingIndicatorSendResponse</a></code>

# Contacts

Types:

```python
from sendblue_api.types import (
    Contact,
    ContactCreateResponse,
    ContactRetrieveResponse,
    ContactUpdateResponse,
    ContactListResponse,
    ContactDeleteResponse,
    ContactCountResponse,
    ContactOptOutResponse,
    ContactVerifyResponse,
)
```

Methods:

- <code title="post /api/v2/contacts">client.contacts.<a href="./src/sendblue_api/resources/contacts/contacts.py">create</a>(\*\*<a href="src/sendblue_api/types/contact_create_params.py">params</a>) -> <a href="./src/sendblue_api/types/contact_create_response.py">ContactCreateResponse</a></code>
- <code title="get /api/v2/contacts/{phone_number}">client.contacts.<a href="./src/sendblue_api/resources/contacts/contacts.py">retrieve</a>(phone_number) -> <a href="./src/sendblue_api/types/contact_retrieve_response.py">ContactRetrieveResponse</a></code>
- <code title="put /api/v2/contacts/{phone_number}">client.contacts.<a href="./src/sendblue_api/resources/contacts/contacts.py">update</a>(phone_number, \*\*<a href="src/sendblue_api/types/contact_update_params.py">params</a>) -> <a href="./src/sendblue_api/types/contact_update_response.py">ContactUpdateResponse</a></code>
- <code title="get /api/v2/contacts">client.contacts.<a href="./src/sendblue_api/resources/contacts/contacts.py">list</a>(\*\*<a href="src/sendblue_api/types/contact_list_params.py">params</a>) -> <a href="./src/sendblue_api/types/contact_list_response.py">ContactListResponse</a></code>
- <code title="delete /api/v2/contacts/{phone_number}">client.contacts.<a href="./src/sendblue_api/resources/contacts/contacts.py">delete</a>(phone_number) -> <a href="./src/sendblue_api/types/contact_delete_response.py">ContactDeleteResponse</a></code>
- <code title="get /api/v2/contacts/count">client.contacts.<a href="./src/sendblue_api/resources/contacts/contacts.py">count</a>() -> <a href="./src/sendblue_api/types/contact_count_response.py">ContactCountResponse</a></code>
- <code title="post /api/v2/contacts/opt-out">client.contacts.<a href="./src/sendblue_api/resources/contacts/contacts.py">opt_out</a>(\*\*<a href="src/sendblue_api/types/contact_opt_out_params.py">params</a>) -> <a href="./src/sendblue_api/types/contact_opt_out_response.py">ContactOptOutResponse</a></code>
- <code title="post /api/v2/contacts/verify">client.contacts.<a href="./src/sendblue_api/resources/contacts/contacts.py">verify</a>(\*\*<a href="src/sendblue_api/types/contact_verify_params.py">params</a>) -> <a href="./src/sendblue_api/types/contact_verify_response.py">ContactVerifyResponse</a></code>

## Bulk

Types:

```python
from sendblue_api.types.contacts import BulkCreateResponse, BulkDeleteResponse
```

Methods:

- <code title="post /api/v2/contacts/bulk">client.contacts.bulk.<a href="./src/sendblue_api/resources/contacts/bulk.py">create</a>(\*\*<a href="src/sendblue_api/types/contacts/bulk_create_params.py">params</a>) -> <a href="./src/sendblue_api/types/contacts/bulk_create_response.py">BulkCreateResponse</a></code>
- <code title="delete /api/v2/contacts">client.contacts.bulk.<a href="./src/sendblue_api/resources/contacts/bulk.py">delete</a>(\*\*<a href="src/sendblue_api/types/contacts/bulk_delete_params.py">params</a>) -> <a href="./src/sendblue_api/types/contacts/bulk_delete_response.py">BulkDeleteResponse</a></code>

# Webhooks

Types:

```python
from sendblue_api.types import (
    WebhookConfiguration,
    WebhookCreateResponse,
    WebhookUpdateResponse,
    WebhookListResponse,
    WebhookDeleteResponse,
)
```

Methods:

- <code title="post /api/account/webhooks">client.webhooks.<a href="./src/sendblue_api/resources/webhooks.py">create</a>(\*\*<a href="src/sendblue_api/types/webhook_create_params.py">params</a>) -> <a href="./src/sendblue_api/types/webhook_create_response.py">WebhookCreateResponse</a></code>
- <code title="put /api/account/webhooks">client.webhooks.<a href="./src/sendblue_api/resources/webhooks.py">update</a>(\*\*<a href="src/sendblue_api/types/webhook_update_params.py">params</a>) -> <a href="./src/sendblue_api/types/webhook_update_response.py">WebhookUpdateResponse</a></code>
- <code title="get /api/account/webhooks">client.webhooks.<a href="./src/sendblue_api/resources/webhooks.py">list</a>() -> <a href="./src/sendblue_api/types/webhook_list_response.py">WebhookListResponse</a></code>
- <code title="delete /api/account/webhooks">client.webhooks.<a href="./src/sendblue_api/resources/webhooks.py">delete</a>(\*\*<a href="src/sendblue_api/types/webhook_delete_params.py">params</a>) -> <a href="./src/sendblue_api/types/webhook_delete_response.py">WebhookDeleteResponse</a></code>

# SendCarousel

Types:

```python
from sendblue_api.types import SendCarouselSendResponse
```

Methods:

- <code title="post /api/send-carousel">client.send_carousel.<a href="./src/sendblue_api/resources/send_carousel.py">send</a>(\*\*<a href="src/sendblue_api/types/send_carousel_send_params.py">params</a>) -> <a href="./src/sendblue_api/types/send_carousel_send_response.py">SendCarouselSendResponse</a></code>

# V2

## Totp

Types:

```python
from sendblue_api.types.v2 import TotpGetCodeResponse
```

Methods:

- <code title="get /api/v2/totp/code/{secret_id}">client.v2.totp.<a href="./src/sendblue_api/resources/v2/totp/totp.py">get_code</a>(secret_id) -> <a href="./src/sendblue_api/types/v2/totp_get_code_response.py">TotpGetCodeResponse</a></code>

### Secrets

Types:

```python
from sendblue_api.types.v2.totp import (
    SecretCreateResponse,
    SecretListResponse,
    SecretDeleteResponse,
)
```

Methods:

- <code title="post /api/v2/totp/secrets">client.v2.totp.secrets.<a href="./src/sendblue_api/resources/v2/totp/secrets.py">create</a>(\*\*<a href="src/sendblue_api/types/v2/totp/secret_create_params.py">params</a>) -> <a href="./src/sendblue_api/types/v2/totp/secret_create_response.py">SecretCreateResponse</a></code>
- <code title="get /api/v2/totp/secrets">client.v2.totp.secrets.<a href="./src/sendblue_api/resources/v2/totp/secrets.py">list</a>() -> <a href="./src/sendblue_api/types/v2/totp/secret_list_response.py">SecretListResponse</a></code>
- <code title="delete /api/v2/totp/secrets/{secret_id}">client.v2.totp.secrets.<a href="./src/sendblue_api/resources/v2/totp/secrets.py">delete</a>(secret_id) -> <a href="./src/sendblue_api/types/v2/totp/secret_delete_response.py">SecretDeleteResponse</a></code>

# Lines

## CallForwarding

Types:

```python
from sendblue_api.types.lines import (
    CallForwardingRetrieveResponse,
    CallForwardingUpdateResponse,
    CallForwardingDeleteResponse,
)
```

Methods:

- <code title="get /api/lines/{sendblue_number}/call-forwarding">client.lines.call_forwarding.<a href="./src/sendblue_api/resources/lines/call_forwarding.py">retrieve</a>(sendblue_number) -> <a href="./src/sendblue_api/types/lines/call_forwarding_retrieve_response.py">CallForwardingRetrieveResponse</a></code>
- <code title="put /api/lines/{sendblue_number}/call-forwarding">client.lines.call_forwarding.<a href="./src/sendblue_api/resources/lines/call_forwarding.py">update</a>(sendblue_number, \*\*<a href="src/sendblue_api/types/lines/call_forwarding_update_params.py">params</a>) -> <a href="./src/sendblue_api/types/lines/call_forwarding_update_response.py">CallForwardingUpdateResponse</a></code>
- <code title="delete /api/lines/{sendblue_number}/call-forwarding">client.lines.call_forwarding.<a href="./src/sendblue_api/resources/lines/call_forwarding.py">delete</a>(sendblue_number) -> <a href="./src/sendblue_api/types/lines/call_forwarding_delete_response.py">CallForwardingDeleteResponse</a></code>
