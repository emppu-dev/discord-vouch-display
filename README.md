## discord-vouch-display
Display your discord vouches on your website.
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Femppu-dev%2Fdiscord-vouch-display&count_bg=%23000000&title_bg=%23000000&icon=&icon_color=%23000000&title=Views&edge_flat=false)](https://hits.seeyoufarm.com)

## To Do
- [ ] Clean up the code
- [ ] Enhance the visual appeal
- [x] Display vouches in real time
- [ ] Implement a user-friendly function to easily remove vouches from the list
- [x] Provide an set-up tutorial

## Installation
config.json
```json
{
    "token":"Discord token here",
    "channel": "Discord channel ID",
    "path":"Path to receive.php for example https://example.com/system/receive.php",
    "key":"Your secret key"
}
```
system/receive.php
```php
$validKey = "Your secret key"; # YOUR KEY HERE
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
