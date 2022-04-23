# Wallapi

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Definitive Wallapop Crawler using the API and send URLs in your Telegram channel group,
additionaly you can add the command in your cron file to specify when to search.

The search saves the URL ids, for later in another search, not resend the same 
URL to your Telegram channel group.

<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
    $ git clone https://github.com/github_username/repo_name.git
   ```
2. Install packages
   ```sh
   $ virtualenv venv
   $ source venv/bin/activate
   $ pip3 install -r requirements
   ```
3. Enter your Telegram credentials in `config/telegram.yaml`

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

```bash
$ python main.py -search "ps4" -min-price 200 -max-price 500
```

Additionaly you can add the script to your cron server, so you can choose when
repeat the search.


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
