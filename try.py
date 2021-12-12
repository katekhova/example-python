url = "hi.jpg"

print('Content-Type:text/html')
print('\n')
print('<html><body>\
<a id="do" href="%s" download="img">do</a>\
<script>document.getElementById("do").click();</script>\
</body></html>' %url)