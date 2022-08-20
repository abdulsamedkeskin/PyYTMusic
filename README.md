# PyYTMusic

Youtube Music API for Python

# Installation

```python
pip install PyYTMusic
```

# Example

```python
from PyYTMusic import PyYTMusic

ytmusic = PyYTMusic()
search_results = ytmusic.search("we're good", ["songs"], limit=2)
print(search_results)
```

### Output :

```json
{
  "results": [
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
      "playerUrl": "https://rr8---sn-u0g3jxaa-n5fl.googlevideo.com/videoplayback?expire=1661038670&ei=7hsBY82hJJem1gLj-Z-QCg&ip=176.234.231.93&id=o-AOEhm9JYdeOLNoZscjOcOtuIPzKdYxzaNthTT1owifut&itag=249&source=youtube&requiressl=yes&mh=1K&mm=31%2C29&mn=sn-u0g3jxaa-n5fl%2Csn-nv47lns6&ms=au%2Crdu&mv=m&mvi=8&pl=22&gcr=tr&initcwndbps=876250&vprv=1&mime=audio%2Fwebm&ns=E3EB36kJMMcvHHxbFqro9jEH&gir=yes&clen=1082461&dur=165.521&lmt=1623555310521291&mt=1661016796&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&rbqsm=fr&txp=5532434&n=UIsx5rzN4vEpSATIDY&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAO8c708ff0bSp_w1V5flIywCCEm9Ct5N9r8O_puUCOSBAiEA-4p4gGi2OZbOv19k1E8vSYlvK6_AbMexfXHzi9TcXIA%3D&sig=AOq0QJ8wRQIgWfWcGY2b520USzp2gxAZJ4je1vQ_DUQQT8phHSWlzt0CIQCQdaQvjp_cXm4X_4f2PtXuVMaeg45Ohf4AZg6FMrqvDQ==",
      "duration": "2:46",
      "browseId": "sNLYDmaJpcI"
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
      "playerUrl": "https://rr7---sn-u0g3jxaa-n5fe.googlevideo.com/videoplayback?expire=1661038671&ei=7xsBY8DEDoyygAeClo3wBQ&ip=176.234.231.93&id=o-ACD_idiO1A2k47rTa2YlAFtlB5ctD2Xg45aas7zrHuaQ&itag=249&source=youtube&requiressl=yes&mh=hR&mm=31%2C29&mn=sn-u0g3jxaa-n5fe%2Csn-nv47lnl6&ms=au%2Crdu&mv=m&mvi=7&pcm2cms=yes&pl=22&gcr=tr&initcwndbps=876250&vprv=1&mime=audio%2Fwebm&ns=q7jZVQ6AzMRn_h69uQQVv4cH&gir=yes&clen=1085260&dur=165.521&lmt=1624363536758656&mt=1661016796&fvip=6&keepalive=yes&fexp=24001373%2C24007246&c=WEB&rbqsm=fr&txp=5411222&n=LSFLe0_ZB7axm8CfOs&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cgcr%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpcm2cms%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAIqo9FwdlhXakCt_6CMDa1bxPT5taBjh2eWjR9ZCBMl3AiEAs-U0tHkvYTyOV7WwGC1wTOrEFWjXxMdtUnkilF0LBQ4%3D&sig=AOq0QJ8wRAIgKjCpNGmIvwAQr0CFBAOCi8qQvczB8cq9yyA34e15qvcCIE2gDp7LvGSqS2V1ggsO8uS2hU81-kGdbV7lB_idXv1o",
      "duration": "2:46",
      "browseId": "KTYZfne5SOa"
    }
  ]
}
```

### You can fetch lyrics with lyrics method

```python
from PyYTMusic import PyYTMusic

ytmusic = PyYTMusic()

results = ytmusic.search("we're good", ['songs'], limit=1)
name = results['results'][0]['name']
browse_id = results['results'][0]['browseId']
lyrics = ytmusic.lyrics(name, browse_id)
print(lyrics['result'])
```

### Output :

```
I'm on an island
Even when you're close
Can't take the silence
I'd rather be alone
I think it's pretty plain and simple
We gave it all we could
It's time I wave goodbye from the window
Let's end this like we should and say we're good

We're not meant to be like sleeping and cocaine
So let's at least agree to go our separate ways
Not gonna judge you when you're with somebody else
As long as you swear you won't be pissed when I do it myself
Let's end it like we should and say we're good

No need to hide it
Go get what you want
This won't be a burden if we both don't hold a grudge
I think it's pretty plain and simple
We gave it all we could
It's time I wave goodbye from the window
Let's end this like we should and say we're good

We're not meant to be like sleeping and cocaine
So let's at least agree to go our separate ways
Not gonna judge you when you're with somebody else
As long as you swear you won't be pissed when I do it myself
Let's end it like we should and say we're good

Now you're holding this against me
Like I knew you would
I'm trying my best to make this easy
So don't give me that look, just say we're good

We're not meant to be like sleeping and cocaine
So let's at least agree to go our separate ways
Not gonna judge you when you're with somebody else
As long as you swear you won't be pissed when I do it myself
Let's end it like we should and say we're good
```

## Methods

```python
search('song name', ['filters'], limit)
lyrics('song_name', 'browseId')
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
