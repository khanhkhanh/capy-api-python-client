## Capy API Client Library for Python


### 1. Sample implementation for Puzzle CAPTCHA

```
from capy_api.puzzle import PuzzleClient


# Set up a client
client = PuzzleClient(capy_privatekey, yourOptionalTimeoutValueInSecond)

# Verify an answer
result = client.verify(capy_challengekey, capy_answer)
```

Note:
- "capy_privatekey" is an API key used for verifying site ownership. It can be obtained from https://jp.api.capy.me/account/edit/
- "capy_challengekey" is a key used for identifying the CAPTCHA. This key is sent to your server when the visitor submits a form including our CAPTCHA
- "capy_answer" is the visitor's answer sent to your server


=======================================================================


### 2. Sample implementation for Avatar CAPTCHA

```
from capy_api.avatar import AvatarClient


# Set up a client
client = AvatarClient(capy_privatekey, yourOptionalTimeoutValueInSecond)

# Verify an answer
result = client.verify(capy_challengekey, capy_answer)


```

Note:
- "capy_privatekey" is an API key used for verifying site ownership. It can be obtained from https://jp.api.capy.me/account/edit/
- "capy_challengekey" is a key used for identifying the CAPTCHA. This key is sent to your server when the visitor submits a form including our CAPTCHA
- "capy_answer" is the visitor's answer sent to your server


=======================================================================


### 3. Sample implementation for Realtime Blacklist

```
from capy_api.blacklist import BlacklistClient


# Set up a client
client = BlacklistClient(capy_privatekey, yourOptionalTimeoutValueInSecond)

# Evaluate an IP address
result = client.evaluate(blacklist_key, capy_ipaddress)
```

Note:
- "capy_privatekey" is an API key used for verifying site ownership. It can be obtained from https://jp.api.capy.me/account/edit/
- "blacklist_key" is a key you can find here https://jp.api.capy.me/blacklist/
- "capy_ipaddress" is the visitor's IP address


=======================================================================


### 4. Sample implementation for Risk-Based Authentication


```
from capy_api.avatar import RiskbaseClient


# Set up a client
client = RiskbaseClient(capy_privatekey, yourOptionalTimeoutValueInSecond)

# Evaluate a user
result = client.evaluate(riskbase_key, capy_data)

Note:
- "capy_privatekey" is an API key used for verifying site ownership. It can be obtained from https://jp.api.capy.me/account/edit/
- "riskbase_key" is a key you can find here https://jp.api.capy.me/riskbase/
- "capy_data" is the data encrypted on the visitor's browser, and then sent to your server when the visitor submits a form
``` 
