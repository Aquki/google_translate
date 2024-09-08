# google_translate
simple google translate library that allows you to use googletrans library in just one line of codes

# requierments:
install the google trans libary
```bash
$ pip install googletrans
```
# How to use
1, Import the google_translate function.

2, Call the function with the text to translate, specifying the target language (dest) and the source language (src) if needed.

```python
import google_translate

output = google_translate("おはよう！", des="en", src="ja")
print(output)
```
and that's it!
