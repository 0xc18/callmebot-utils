# callmebot-utils

callmebot-utils is a Python module that provides a simple interface to send messages via Facebook, WhatsApp, and Signal using [CallMeBot](https://www.callmebot.com/).

[![PyPI](https://img.shields.io/pypi/v/callmebot-utils.svg)](https://pypi.org/project/callmebot-utils/)
[![Python Version](https://img.shields.io/pypi/pyversions/callmebot-utils.svg)](https://pypi.org/project/callmebot-utils/)
[![License](https://img.shields.io/github/license/SAKIB-SALIM/callmebot-utils)](https://github.com/SAKIB-SALIM/callmebot-utils/blob/main/LICENSE)

---

## Installation

You can install this module using pip:

```sh
pip install callmebot-utils
```

---

## Usage

### Sending a Message via WhatsApp

```python
from callmebot_utils import Whatsapp

api_key = "YOUR_API_KEY"
phone = "PHONE_NUMBER"

whatsapp = Whatsapp(api_key, phone)

response = whatsapp.send_text("Hello from CallMeBot!")
print(response)
```

### Sending a Message via Facebook

```python
from callmebot_utils import Facebook

api_key = "YOUR_API_KEY"

facebook = Facebook(api_key)

response = facebook.send_text("Hello from CallMeBot!")
print(response)

response = facebook.send_image_by_url("https://avatars.githubusercontent.com/u/144510317")
print(response)

response = facebook.send_image("./your_image_path.png")
print(response)

```

### Sending a Message via Signal

```python
from callmebot_utils import Signal

api_key = "YOUR_API_KEY"
phone = "PHONE_NUMBER"

signal = Signal(api_key, phone)

response = signal.send_text("Hello from CallMeBot!")
print(response)
```

## License

This project is licensed under the MIT License.

---

## Author

Developed by **Sakib Salim**  
GitHub: [sakib-salim](https://github.com/SAKIB-SALIM)  


