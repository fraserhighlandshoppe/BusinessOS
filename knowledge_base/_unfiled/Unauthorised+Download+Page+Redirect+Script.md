# Unauthorised+Download+Page+Redirect+Script.pdf

```markdown
Unauthorised Download Page Redirect Script
By Dave Lucas
Acknowledgements:
I would like to thank Russ Ayres, for donating this script to the DM
Engage Facebook community. He can be contacted at:
http://www.motivatewellness.com

This little script is useful for the following scenario:
You setup an opt-in page where you request a visitor’s email address in exchange for a lead magnet.
The visitor is then redirected to a download page. The user then decides to share the download link
for your download page on Twitter or Facebook and you get thousands of visitors downloading your
lead magnet without subscribing.
What the Script Does
The script is designed to redirect the visitor to the opt-in page if they have not subscribed to your
list. It works as follows:
1. Visitor visits your opt-in page. A cookie is put on their computer which is unique to your optin page. They can only get this cookie if they have visited your opt-in page.
2. Opt-in page redirects the visitor to the download page. The download page checks if the
cookie from your opt-in page is present. If it is, then it displays the download page.
3. If the visitor visits the download page without having opted-in they are redirected to the
opt-in page.
If you want to be a little more secure, you can load the cookie on a separate thank-you page after
the visitor opts-in. Then the visitor would have to visit this thank you page, before they can visit the
download page1.
How to Install the Script
The script runs in in Javascript. It has a main body which you install on your opt-in and download
pages. You then run certain functions to do what you need on each of the pages.
In html it works as follows:
<head>
{Put Main Script Here}
</head>
<body>
{Run functions. Put straight after body}
</body>

1

Thanks Russ Ayres for this suggestion.
© Copyright Dave Lucas 2015 – Script is Open Source. Free to use and modify. Usage instructions may
only be shared via this document.

1

Those of you that are more technically orientated may want to adapt the script to your needs.
Alternatively, if you have a special request I can help.
Here is the script:
Main Script – Install on both opt-in and download page
<head>
<script>
function setCookie(cname, cvalue, exdays) {
var d = new Date();
d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
var expires = "expires=" + d.toUTCString();
document.cookie = cname + "=" + cvalue + "; " + expires + "; path=/";
}
function getCookie(cname) {
var name = cname + "=";
var ca = document.cookie.split(';');
for (var i = 0; i < ca.length; i++) {
var c = ca[i];
while (c.charAt(0) == ' ') c = c.substring(1);
if (c.indexOf(name) == 0) return c.substring(name.length,
c.length);
}
return "";
}
function cookieRedirect(cname) {
var previous_visitor = getCookie(cname);
alert ("cookie_value = "+previous_visitor);
if (previous_visitor == "yes") {
//alert ("Cookie is Yes");
} else {
//alert ("Cookie is not Yes");
window.location.assign("http://optinurl.com");
}
}
</script>

.
.
.
</head>

Note: Change http://optinurl.com to whatever your optin url is.

© Copyright Dave Lucas 2015 – Script is Open Source. Free to use and modify. Usage instructions may
only be shared via this document.

2

Functions to run:
On Opt-in Page
<body>
<script>
setCookie("optinpage1","yes",360);
</script
.
.
.

</body>
On Download Page
<body>
<script>
cookieRedirect("optinpage1");
</script>
.
.
.

</body>
Note: Change optinpage1 to whatever you want to name your tracking cookie. Also remember that
each unique opt-in page has to have its own unique cookie name.
If this is a bit technical for you, then please feel free to get in touch with me. I’m happy to install the
script for you at a reasonable fee.

Do You Need Some Help with Your Website Scripting?
I am here to help you with your web site scripting.
I have been setting up web sites since 2001. I can program in Javascript, JQuery, PHP & MYSQL. I
also know Wordpress, Optimizepress, Active Campaign etc… I have also studied Computer
Science. So if you deal with me, you know you are dealing with a competent and friendly person.
Sometimes it can be very difficult to make basic things work on a typical Wordpress installation.
Maybe you want to have offers that expire after a certain time period, or you need to make a
form work, or pass custom information between applications, or you need to install Adwords
tracking code. Or a whole host of other frustrating technical challenges.
These simple tasks can end up being crazy complicated, and have you pulling your hair out, even
if you are quite technical.
Why feel frustrated, when there is someone who is technically competent and trustworthy to
help you out? Get some help today.
Message Dave Lucas on Facebook for a free quote:
https://www.facebook.com/davidanthonylucas
Or email: scriptquote@dawningtruth.com

© Copyright Dave Lucas 2015 – Script is Open Source. Free to use and modify. Usage instructions may
only be shared via this document.

3
```
