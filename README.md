# My Blog 

[![Build Status](https://travis-ci.org/theskumar/blog.svg?branch=master)](https://travis-ci.org/theskumar/blog)

Built with [Pelican][1]

## Setup

### Quick Setup (Recommended)

The easiest way to get started is using the setup script:

```shell
git clone --recursive git@github.com:theskumar/blog.git theskumar-blog && cd theskumar-blog
./setup.sh
source .venv/bin/activate
```

### Manual Setup with uv

```shell
git clone --recursive git@github.com:theskumar/blog.git theskumar-blog && cd theskumar-blog

# Install uv (https://github.com/astral-sh/uv)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -e .
```

### Legacy Setup (pip)

```shell
git clone --recursive git@github.com:theskumar/blog.git theskumar-blog && cd theskumar-blog

# activate virtualenv
virtualenv venv && source venv/bin/activate

# install the dependencies
pip install -r requirements.txt
```

## Development

Start the development server with:

```shell
make devserver
```

This will start a server at http://localhost:8000 and automatically regenerate the site when files change.

## Publishing

To build the site for production:

```shell
make publish
```

To deploy to GitHub Pages:

```shell
make github
```

The blog uses [pelican-svbtle-responsive][2] theme.

## License

<section class="license" align=center>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
<br />
This <span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" rel="dct:type">work</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Saurabh Kumar</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/deed.en_US">Creative Commons Attribution 4.0 International License</a>.
</section>


  [1]: http://docs.getpelican.com/
  [2]: https://github.com/theskumar/pelican-svbtle-responsive
