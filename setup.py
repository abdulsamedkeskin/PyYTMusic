import setuptools


long_description = """# PyYTMusic

Youtube Music API for Python

# Installation

```python
pip install PyYTMusic
```

# Example

```python
from PyYTMusic import PyYTMusic

ytmusic = PyYTMusic()
search_results = ytmusic.search("we're good", ["songs"])
print(search_results)


```

### Output :

```json
{
  "results": [
    {
      "type": "top result",
      "name": "We're Good",
      "thumbnails": [
        {
          "url": "https://i.ytimg.com/vi/jr47YisIsz8/sddefault.jpg?sqp=-oaymwEWCJADEOEBIAQqCghqEJQEGHgg6AJIWg&rs=AMzJL3nwkTmeRwXHiFfKUdq5rT3JEKjQ9A",
          "width": 400,
          "height": 225
        }
      ],
      "author": "Dua Lipa",
      "videoId": "jr47YisIsz8",
      "playerUrl": "https://rr8---sn-u0g3jxaa-n5fs.googlevideo.com/videoplayback?expire=1660326601&ei=aT72YuSAKJDegAeR8pmgBw&ip=176.234.226.113&id=o-ALl4XZK3QhUJqDc8nSIUyU243TKDW_gN3sJ4wLtmVHF1&itag=249&source=youtube&requiressl=yes&mh=Tw&mm=31%2C29&mn=sn-u0g3jxaa-n5fs%2Csn-nv47lnsk&ms=au%2Crdu&mv=m&mvi=8&pl=22&initcwndbps=761250&spc=lT-Khh9dmVplSupsl1KJjpGqbF5NlwI&vprv=1&mime=audio%2Fwebm&ns=N1cnr6P2nBML9kpVLNhgLhcH&gir=yes&clen=1219315&dur=191.681&lmt=1646363055152298&mt=1660304234&fvip=4&keepalive=yes&fexp=24001373%2C24007246&c=WEB&rbqsm=fr&txp=4532434&n=s_tdI5CVZqmKAoxuo6&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAKJcfGq0OlHSZpABjQCrsALdjO8XKdLLb1LehNBh6ln1AiEA-INLGcH4WNaKL3yiQawk7MoUZCj4KHSHQqLy6hXdWEc%3D&sig=AOq0QJ8wRgIhALgO9zc9uDMNXC-YzucaUu-sfgkHZsLiG3AmsZutN54dAiEA9b1n5zEEy-Lw5yqwVbdIlFWHaCJ9Byvx5Ma0SY3tG6I=",
      "duration": "3:12"
    },
    {
      "type": "songs",
      "name": "We're Good",
      "thumbnails": [
        {
          "url": "https://lh3.googleusercontent.com/14fZepfSfYQcY_klVgZwFNTiJ9_2iMf4865CQMLWQ6rY4r3wPa8BaDMqexKixCn3h1ik2ybxys5MTTHzmg=w60-h60-l90-rj",
          "width": 60,
          "height": 60
        },
        {
          "url": "https://lh3.googleusercontent.com/14fZepfSfYQcY_klVgZwFNTiJ9_2iMf4865CQMLWQ6rY4r3wPa8BaDMqexKixCn3h1ik2ybxys5MTTHzmg=w120-h120-l90-rj",
          "width": 120,
          "height": 120
        }
      ],
      "author": "Dua Lipa",
      "videoId": "CBjtouAePhM",
      "playerUrl": "https://rr8---sn-u0g3jxaa-n5fl.googlevideo.com/videoplayback?expire=1660326602&ei=aj72YvfwGoS91gL61an4Cw&ip=176.234.226.113&id=o-AIUubV5ttJJiIEKHFQSAr-yl_IsB7v7rGSp9jN15tLeU&itag=249&source=youtube&requiressl=yes&mh=1K&mm=31%2C29&mn=sn-u0g3jxaa-n5fl%2Csn-nv47lns6&ms=au%2Crdu&mv=m&mvi=8&pl=22&gcr=tr&initcwndbps=731250&spc=lT-Khj-QgZhf7VoBoEXGS1SnT5iZl54&vprv=1&mime=audio%2Fwebm&ns=nQ8lpKlGXkdV6VY19w_2uEkH&gir=yes&clen=1082461&dur=165.521&lmt=1623555310521291&mt=1660304234&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&rbqsm=fr&txp=5532434&n=d77b4xVTJCTGHE4lmV&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRQIhAPxqgbNxQZ376O_nt59mf1AdNTuYbkElYXYfb8E7kssuAiATeN-zMUEgF7AeQG5LpZlatSnYg4dayCtsSGv4wDB2hw%3D%3D&sig=AOq0QJ8wRQIgaNMMxwwd5lQjibIGDnVF_x7ovVWrEUr2e2ZCldyEEqoCIQCAsPs-0cgICUtLXheHKITQ7UCSTZjH0luqLXbUVKevag==",
      "duration": "2:46"
    },
    {
      "type": "songs",
      "name": "We're Good",
      "thumbnails": [
        {
          "url": "https://lh3.googleusercontent.com/T6Vx6KKmZsLLEoT2SEe0LUGa8JQioIs3yDRMg4LdaoeNpJjSCSzxYa9alV8J5zfKk_t6A8VrrWnKIQ-TEw=w60-h60-l90-rj",
          "width": 60,
          "height": 60
        },
        {
          "url": "https://lh3.googleusercontent.com/T6Vx6KKmZsLLEoT2SEe0LUGa8JQioIs3yDRMg4LdaoeNpJjSCSzxYa9alV8J5zfKk_t6A8VrrWnKIQ-TEw=w120-h120-l90-rj",
          "width": 120,
          "height": 120
        }
      ],
      "author": "Dua Lipa",
      "videoId": "hLzo1ZZu76w",
      "playerUrl": "https://rr7---sn-u0g3jxaa-n5fe.googlevideo.com/videoplayback?expire=1660326603&ei=az72YtvNCcaj1gKUvqjQAQ&ip=176.234.226.113&id=o-AI9sk6OhFOgR6ofZNWNYQ9iiPniOA9lIUnQ9bv8UJRXa&itag=249&source=youtube&requiressl=yes&mh=hR&mm=31%2C29&mn=sn-u0g3jxaa-n5fe%2Csn-nv47lnl6&ms=au%2Crdu&mv=m&mvi=7&pl=22&gcr=tr&initcwndbps=753750&spc=lT-KhiavbuQbica-r4--FJW1IGHNfVA&vprv=1&mime=audio%2Fwebm&ns=_0dy3jRs5Ylohs9z-Oo9-rUH&gir=yes&clen=1085260&dur=165.521&lmt=1624363536758656&mt=1660304234&fvip=6&keepalive=yes&fexp=24001373%2C24007246&c=WEB&rbqsm=fr&txp=5411222&n=tZ3Dn5vMI70-IE0uIp&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgBAvr3xcAFgFcGDQRhbI_XXhSF-WvuuT8k3Bf34ZKkK4CIHCAHkwWM2C11QwxKtgBdTcmz9E5dUZcZDG53B5T0dac&sig=AOq0QJ8wRQIhANMNwD2xE9O5ANfGL1THtS57ynlVCuRuYu1lmUfN5ZMVAiAc-KtFJOu0d939FYEGhzIB_9JGJAKS8OkW1Kt2Hwkd6A==",
      "duration": "2:46"
    },
    {
      "type": "songs",
      "name": "We're Good (Originally Performed By Dua Lipa) (Karaoke Version)",
      "thumbnails": [
        {
          "url": "https://lh3.googleusercontent.com/jrhyRmvkogMgeBStijcMf0xLstqFXRZzIgtdCGJoMj8iTTtWQ29yWsty_2ME5JSmDSFe-d3T4dBceVWe=w60-h60-l90-rj",
          "width": 60,
          "height": 60
        },
        {
          "url": "https://lh3.googleusercontent.com/jrhyRmvkogMgeBStijcMf0xLstqFXRZzIgtdCGJoMj8iTTtWQ29yWsty_2ME5JSmDSFe-d3T4dBceVWe=w120-h120-l90-rj",
          "width": 120,
          "height": 120
        }
      ],
      "author": "Hit The Button Karaoke",
      "videoId": "ZkjBFWKtDrc",
      "playerUrl": "https://rr6---sn-u0g3jxaa-n5fs.googlevideo.com/videoplayback?expire=1660326603&ei=az72YtCkMZyR1gLX5ajABA&ip=176.234.226.113&id=o-AKm2VFMxffoUQhn3ZU01uZVIlAb3GLp59S2KlzKFI417&itag=249&source=youtube&requiressl=yes&mh=Ae&mm=31%2C29&mn=sn-u0g3jxaa-n5fs%2Csn-nv47lnl6&ms=au%2Crdu&mv=m&mvi=6&pl=22&gcr=tr&initcwndbps=761250&spc=lT-KhmoeUZmHYOG9VkZoSpmOFNnqwBY&vprv=1&mime=audio%2Fwebm&ns=A3LprjV3lobATq099pLv1vsH&gir=yes&clen=1108906&dur=164.121&lmt=1616590294521237&mt=1660304234&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&rbqsm=fr&txp=2311224&n=CkRGkBWhVWnMWdnXPv&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgSZztskVnesBpfu2bnCQQyZBkVcqiGbnk0TJ8ThT5Cr0CICLYptv7yomXck9Vv5di5FWiC5csuI4J6E16Qj3-P9Xe&sig=AOq0QJ8wRAIgc5B1hztcAHxqjQjFpRYccFc9nHAk9m3nHl0cY0ueD2wCIDiIG0Z7CbAdBPCT7ZjlEygV2c33DmYKl22MWOfleIBL",
      "duration": "2:45"
    }
  ]
}
```

## Methods

```python
search('song name', ['filters'])
```

# License

MIT License

Copyright (c) 2022 Abdulsamet Keskin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

setuptools.setup(
    name='PyYTMusic',
    packages=setuptools.find_packages(),
    version='0.1.2',
    license='MIT',
    description='Python Youtube Music API',
    author='Samet Keskin',
    author_email='sametkeskin.py@gmail.com',
    url='https://github.com/abdulsamedkeskin/PyYTMusic',
    keywords=['PyYTMusic', 'Youtube', 'Music', 'API'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
