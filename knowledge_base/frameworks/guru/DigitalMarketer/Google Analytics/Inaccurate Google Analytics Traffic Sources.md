# Inaccurate Google Analytics Traffic Sources.pdf

```markdown
Inaccurate Google Analytics Traffic Sources

1 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Analytics

100

CATEGORIES

Google Analytics: 21
Inaccurate Traffic
Sources, Setup Mistakes
…and Fixes

Analytics

Digital Strategy

Inside Orbit

SEO & Content Marketing

Social Media

Web Development

by Andy Crestodina
Website Design & Usability

SEARCH BLOG

POPULAR

COMMENTS

03/19
The Ideal Length for Blog
Posts, Tweets, and
Everything Else in Your
Marketing ›

It’s very clever. Google Analytics combines Javascript with cookies to track all kinds of
data about visitors. You don’t need to install anything on your server, and they don’t need
to look at your log files. It’s brilliant, but it has its issues.
Here are 21 ways in which Google Analytics is inaccurate…

06/25
Survey of 1000+ Bloggers:
How to Be in the Top 5% ›

02/06
Google Analytics: 21
Inaccurate Traffic Sources,
Setup Mistakes …and Fixes ›

Let’s start with traffic sources
Google Analytics’ Traffic Sources report is notoriously problematic. Traffic Sources is

supposed to show you how people got to your website. The three main categories are
Search, Referral, and Direct. Here’s what the traffic sources are supposed to mean:

04/25
Google URL Builder: How to
Track Campaigns in
Analytics ›

Search Traffic: Visitors who found you through a search engine, either by clicking

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

2 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Direct Traffic: Visitors who typed your address directly into a browser
But there are all kinds of reasons why this data is inaccurate. Much of the Traffic Sources

who receive bi-weekly
web marketing tips.

report is incorrectly categorized, mislabeled, and incomplete.

Search Traffic
Although we’d like to believe that search traffic is everyone who discovered us through a
keyword search, there are two problems here: branded searches and hidden keyword
data.

1. Branded keywords appearing in search traffic
Search traffic includes “brand keywords” such as the company name. Although this is
technically still search traffic, these visitors knew you already. They may have accidentally
searched for your web address rather than entering it into the address bar.

Ideally, visitors who find websites by searching for the brand would be categorized as
direct traffic.
I’ve seen Analytics accounts where 80% of the search traffic was searches for the brand.
At a glance, it looks like a healthy amount of visitors were discovering them through
search engines. In fact, the company didn’t rank for anything but their own name.

Fix: You can set up Analytics so that branded keywords, such as your company’s name,
show up as direct traffic. To do this, use the _addIgnoredOrganic() method. More info
here.

2. Keyword data is hidden

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

3 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

in the address bar of the browser, the phrase for which you searched will not be shared
with the website owner if you click on a link in Google search results. The keyphase will
appear as “(not provided).”
Keyword data is hidden for anyone using the search field in the Firefox browser, anyone
using the Chrome “Omnibox” (the combination address bar, search field), and anyone
logged into any Google product. That’s a lot of people. It’s no wonder that within a year,
39% of keyword data is (not provided).

Fix: There is no fix for this problem, except to consider using AdWords, which shows more
data.

Referral Traffic
In theory, referral traffic shows visitors who came from other websites. But in practice, it
often includes traffic driven from social media efforts, email and in some cases, traffic
from one page on your site to another.

3. Traffic from social sources
Social media marketing takes time and energy, so you’ll want to measure the
effectiveness of those efforts separately in Analytics. But social traffic is actually
categorized as referral or direct. Any clicks on tweets or posts without tracking code and
within a browser will appear as referral traffic.
Google is working on better segmentation of social traffic, but so far, social traffic isn’t
even part of the traffic sources overview report!

Fix 1 : Some social media tools can be set up to add campaign tracking code to shortened

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

4 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Analytics. This will help GA correctly segment social traffic from other referrers.

4. Traffic from web mail
If you send out an email newsletter with a link to your site, and the recipient opens and
clicks it from within a browser, such as Gmail or Yahoo! Mail, the traffic is recorded as a
referral, even though the real traffic source was a newsletter, something you’d like to
track separately. This is always true unless you add campaign tracking code.

Fix: Use the URL Builder to add campaign tracking code to every link to your site in your
emails. This will keep your direct traffic clean, but also allow you to track what visitors
from emails are doing. Your email service provider may have a feature that makes this
easy or you can use this guide on how to use the Google Analytics URL builder.

5. Traffic from your own site: full URL links vs.
relative links
Link issues often lead to inaccurate referral traffic data. When you create a link from one
page to another, you can add the full address (www.site.com/page) or just add the
relative address (/page without the www.site.com).
It turns out that this little decision affects the accuracy of the data in your referral traffic.
Links with full URLs may record as referral traffic in Analytics, even if the visit was from
another page on your site. That’s bad.

Fix: Look at your referral traffic report. If pages from your own site are there, check the
links on those pages. Links should not include the main web address, only the relative
page.

Direct Traffic
Here is the true definition of direct traffic:

All traffic for which a referrer wasn’t specified.
In other words, direct traffic isn’t just people who entered your address into a browser,
it’s any visit that isn’t from a link on a website or search engine and doesn’t
have campaign code. This includes any visit that isn’t from a website.
Really, direct traffic is a catch-all bucket for “everything else.” So there’s a lot of weird
stuff in here. Let’s take a look.

6. Traffic from social sources and mobile apps
Lots of social activity happens within apps. But links in apps don’t always pass a
“referrer,” so it looks like direct traffic in your Google Analytics.

Fix: Some apps will automatically shorten links, adding a referrer by redirecting the visitor
through another address (official Twitter apps sent traffic through t.co address). This

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

5 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

7. Traffic from email programs like Outlook
As with the referral traffic / web mail problem, some of the traffic from that newsletter
you sent will be opened in email programs like Outlook or Mail. This is because desktop
software doesn’t pass referral data like browsers do.

Fix: Add campaign tracking code to email marketing.

8. Traffic that started offline: links in PDFs, Word
Docs, Powerpoint, etc.
Visits from links in non-web page files are recorded as direct traffic, unless they have
campaign tracking code. PDF files are the biggest culprit.

Fix: Move content from these files to web pages, then share the page, not the file. Resist
the urge to add lots of PDFs to your website. Not only is traffic from links in PDFs harder
to track, but “visits” to PDF files don’t appear in your stats at all.

9. Traffic from bad campaign code
If Analytics sees campaign tracking code, it ignores the referrer. But if the tracking code
has problems, it doesn’t put the visit back into referring traffic, it puts it into direct traffic.

Fix: If you set up tracking code manually, do it carefully and double check your work.

10. Traffic from page with missing Javascript
code
If there is a page on your website that doesn’t have ga.js (the Analytics Javascript code)
properly installed, traffic from this page to other pages will appear as direct traffic. Yet
another example of how direct traffic is really a mixture of all your traffic leftovers.

Fix: Use a tool like Google Analytics Debugger or Screaming Frog to scan your site
for improper or missing code.

11. Traffic from you: companies affect their own
stats
If you don’t have filters properly set up, it’s possible that a significant portion of your
traffic is coming from you, your office, or your team. If even a handful of employees set
the website as their homepage, it will skew direct traffic over the long run.

Fix: Set up a filter so traffic from your own network’s IP address is removed from your
stats. Hopefully, you have an internet connection with a static IP address. Most offices do.

More Inaccurate and Misleading Analytics
2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

6 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

problems.

12. In-page analytics
This report shows what percentage of visitors clicked on which links and buttons. But
have you ever noticed that the percentages add up to more than 100%? It happens when
there is more than one way to get to a page.
It’s because Google Analytics knows if a visitor went to another page, but not which link
they clicked. So the same percentage is shown for all the links to that page. It’s a gap in
the data on this report.

Fix: You can now add special code which will improve the accuracy of In-Page Analytics.
It’s called Enhanced Link Attribution, and it will give you better data on which link or
button was clicked.
Note: Even with this fix, some actions will still not be recorded. A form “submit” buttons
or a play button in a video player won’t show up, because these don’t send the visitor to
another page where the next bit of Javascript can run.

13. No cookie? No data
Unlike old-school webstats that analyze the log files on your server, Google Analytics
needs cookies to work properly. If the visitor’s computer (or firewall) rejects cookies, it’s a
hole in your data.
Every time a previous visitor clears their cookies, they look like a new unique visitor next
time they visit. To Google, they might as well be a newborn baby.

Fix: None

14. No Javascript? No data
Here’s an even bigger problem: not everyone enables Javascript. Current data on
Javascript disabled rates is hard to find, but it’s likely that between 1 and 2% of
visitors don’t allow Javascript to run for security, privacy, or accessibility reasons. If a
visitor who is visually impaired uses a screen reader to access the site, Google Analytics is
blind to them.

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

7 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Fix: Make sure the code is installed. Javascript tracking code should be added at the top
of the page, before the </head> tag. If the Javascript is at the bottom of the page and
doesn’t have time to execute before the visitor leaves the page, no data will be recorded.

15. Ridiculously low bounce rate? Too much
analytics code!
If your bounce rate is in the low single digits, check to see if Google Analytics Javascript is
on the page twice. If so, very few bounces will record since a visit to only one page
(which is a “bounce”) triggers the Javascript twice.

Fix: Stop celebrating, put away the champagne and remove the extra code.

16. Time on page? Or time on tab?
The page loads, you read a bit, then switch to a different tab, planning to finish reading
later…
Google has no idea you left. When a tab is open, Analytics assumes you’re on the page,
even if you minimized the browser or got up to make a sandwich. Even though Analytics
will “time out” after 30 minutes, the “Average Visit Duration” report is unreliable.

Fix: None. It’s a problem that’s common to all web stats tools and may be unsolvable!

17. Different visitor, same device
If two people visit the same site for the first time from the same computer, Analytics only
noticed one unique visitor. Imagine 100 people visiting from the same computer at a
library. It’s just one visitor to Analytics. It’s no wonder libraries are underfunded.

Fix: None

18. Different device, same visitor
Again, “unique visitor” isn’t an honest way to say it. It’s really unique computer, so if one

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

8 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

on your list opens the email on their laptop and on their phone, your open rate will be
200%. Great job!

19. Too many goals
It’s nice to see double digit conversion rates, but only if they’re accurate. If you set up too
many goals, including event tracking goals, you’ll artificially inflate your overall conversion
rate.

Fix: Only set up goals and events for things that are important, or you’ll need to start
ignoring the main Goal Conversion Rate.

20. Too many profiles
New profiles permanently remove data from the default profile. This data can never be
recombined with the original profile, so use them wisely. If, for example, you separate all
mobile traffic to a separate profile, you can’t easily compare it to your other traffic data.
You just screwed up your stats.

Fix: Use Advanced Segments or Advanced Filters to view specific types of users in a
specific report. Profiles are meant to segment out completely different types of visits from
your normal marketing stats, such as traffic within a login area.

21. Time delay
One last reason why Google Analytics isn’t giving you the full picture: lag. Except for the
limited (but beautiful) Real Time reports, GA data is typically at least 6 hours behind. The
delay in the Search Engine Optimization section is even worse. That data is often 48 hours
behind.

Fix: Be patient.

TL;DR (Too Long; Didn’t Read)
Analytics is an amazing tool. It can do incredible things, and it’s constantly getting better.
But these are huge challenges. Traffic sources are diverse and complicated. Tracking stats
with Javascript and cookies means Analytics has inherent limitations. Finally, improper
setup can make things even worse.
But even with imperfect data, you can still use Analytics to support great marketing
decisions.
You can help by making sure things are set up properly:
Check your GA Javascript. It should appear once at the top of the code for every
page.

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

9 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Google Analytics.

Did we miss anything?
We’re hoping to make this article a comprehensive list of problems with traffic sources. If
you know of something we missed, please let us know with a comment below, and we’ll
add it. We appreciate the input!

SHARE

Andy Crestodina is the Strategic
Director of Orbit Media. He’s also the
author of Content Chemistry: An
Illustrated Guide to Content Marketing.
You can find Andy on Google+,
LinkedIn and Twitter.

Have Something to Say?

Notify me of new comments via email.

Post Comment

Notify me of new posts via email.

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

10 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Excellent overview of GA’s challenges – and why you need to supplement it with
other sources. Our search traffic is approaching 50% “encrypted” which presents big
challenges. Besides driving people to use paid seach, is there any other reason
Google is doing this?
Reply to DanKaplan

crestodina 3/07/13 @ 7:24AM
@DanKaplan Hmm. I think (not provided) gives Google some legal cover
and good PR when it comes to privacy. Whenever things go to court, they
can more easily say that they are protecting the privacy of their users.
They’ve got more data than anybody, so they’ve got more liability for
privacy complaints. This gives them a way to say “we value privacy over
data sharing” …Maybe that’s why?
Reply to crestodina

PayAus 4/20/13 @ 6:01AM
@crestodina @DanKaplan From a statistical point of you do you
think this a big concern, assuming the data not collected is
relatively randomised.
Reply to PayAus

PayAus 4/20/13 @ 6:18AM
@crestodina @DanKaplan From a statistical point of view do you
think this a big concern, assuming the data not collected is
relatively randomised.
Reply to PayAus

crestodina 4/20/13 @ 9:26AM
@PayAus @DanKaplan I do think it’s a big concern. If we could
see all that data, we’d have a better chance of discovering
effective keywords that we hadn’t thought to target. These little
gems might not get much traffic, but they might be highly relevant
phrases I hadn’t thought of. I really do wish I had more keyword
data…
Reply to crestodina

tacimala 3/07/13 @ 9:53AM
Regarding #5, this primarily happens as a result of the analytics code being
improperly set up across multiple domains or subdomains, or in worse cases,

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

11 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

report. Once on that report, below the graph and above the table data is a link for
Hostname. Nice and easy to find, huh? This will show you all of the URLs that
triggered your GA code and help diagnose what is going on.
Perhaps one of the biggest inaccuracies within GA is time on page and time on site.
It’s not just what you pointed out in #16 that people will leave a page open, but
unless you visit a second page of the website, GA doesn’t calculate the time on the
page or the time on the site and will use 0:00. This obviously skews the information
downwards for time on page/time on site, especially if a site is high in blog traffic
(people that tend to visit a single page and go on their merry way).
As you pointed out, bounce rate can be screwy as well and many people look at
bounce rate as a problem, whereas something like a phone call would count as a
conversion and a bounce if the site visitor only visited one page (also time on
page/site would be 0:00 as well). I’ll take 100% conversion and 100% bounce rate
any day of the week! Including bounce rate across an entire website and across all
mediums could realistically be considered an inaccuracy of GA.
Andy – I’m not sure I’d agree with #20. It’s definitely true that you can’t get data
back if you have filtered it out, but best practices for setting up multiple profiles
within an account is to keep 1 profile unfiltered and including all of the data. Then
create new profiles and apply those filters only to those specific profiles. That way if
you wanted to share specific pieces of data with certain departments or people, while
hiding other data from them, that could be done. I’ve not heard of that data being
removed from the master profile to fill the new profile.
Awesome idea for an article.
Reply to tacimala

crestodina 3/08/13 @ 8:01AM
@tacimalaThanks for the input, Taylor! Great stuff. I’ll be adding some of
these details to the article.
Yes, I know of two cases where a client’s website was stolen (copied) and
the plagiarists copied the GA code. Crazy, right? We discovered that the site
had been copied by looking at the Analytics. “Wait, what’s this traffic?”
Thanks again for the input and clarification. Appreciated.
Reply to crestodina

Patrick Larsen 3/07/13 @ 6:53PM
Andy. Awesome post. Thanks for the great info. It’s so critical to have clean data if
you are going to run analytics on your marketing.
Reply to Patrick Larsen

crestodina 3/08/13 @ 8:05AM
@Patrick Larsen I’m glad this was useful, Patrick!
Reply to crestodina

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

12 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

ramkichn 3/14/13 @ 12:09AM
I created seperate profile for Mobile WAP Site. Google Analytics shows 26% of the
traffic from Desktop Version, When analyzing the 26% of the traffic data with
Browser, 95% of the browser are mobile Compatabile browser (like Opera Mini,
Mozilla compatabile agent, Safari, etc).
http://www.digitalmarketinganalytics.net/google-analytics-mobiledevice-mapping-accuracy/
Reply to ramkichn

formerly-the-angriest-man-in-advertising 3/14/13 @ 2:34PM
Hey Andy @crestodina, can I come work for you? You’re the smartest man in the
room. Thanks for the peek behind the curtain.
Reply to formerly-the-angriest-man-in-advertising

lisamayer 4/08/13 @ 11:13AM
Hey Andy
You are really good at explaining things – I’m less than a novice and have a question
about tracking PDF downloads – an outside source linked directly to a pdf on our site
– can we see how traffic spikes?
ps – do you teach a course in google analytics – i really need some training.
Reply to lisamayer

crestodina 4/08/13 @ 1:15PM
@lisamayer Thank you for the positive feedback, Lisa! Traffic from PDF files
will be mixed in with all the other direct traffic unless you add campaign
tracking code using the URL Builder. I suggest you set the Source to “PDF,”
the Medium to “offline” and the Name to be whatever the PDF is all about.
Now traffic from links in PDF files will be available in Traffic Sources >
Campaigns.
We do teach at events here at Orbit. It’s a monthly event called “Wine &
Web” The invite is in the newsletter. I also recommend the book, which has
a lot more information on these topics…
http://www.orbitmedia.com/contentchemistry
Hope this is all helpful!
Reply to crestodina

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

13 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

match. Is this a common issue? Or am I misinterpreting something?
Reply to ngweileen

quocnguyen 5/06/13 @ 4:54AM
Are you sure “Links with full URLs may record as referral traffic in Analytics” ? There
are a lot of articles out there suggest the use absolute link, for
example http://yoast.com/relative-urls-issues/
Reply to quocnguyen

Smbatyan 5/20/13 @ 9:29AM
Hi, I’ve found some strange thing in my reports. For my Facebook ads tracking I used
campaign tracking URL made by Google’s URL builder. Campaign source was
Facebook and Medium was cpc. In Campaign reports of GA all data id fine. But
unfortunately all FB ads traffic is also shown in Paid Search section. I guess this is
because of “cpc” medium. Do you have any idea on how ti fix this ?
Reply to Smbatyan

tacimala 5/20/13 @ 10:12AM
@Smbatyan Yes, marking the medium as cpc is a feature in GA that allows
the data to be included in the Paid Search section. Cost data won’t be
included outside of AdWords though. If you don’t want it to show up in Paid
Search (even though one would argue that it still is a form of paid search),
simply change cpc to something else.
Reply to tacimala

Smbatyan 5/20/13 @ 10:37AM
@tacimala And what will happen if I’ll use “ppc” ? Will it be
mixed with AdWord traffic? Or AdWords uses “cpc” ?
Reply to Smbatyan

tacimala 5/20/13 @ 1:00PM
@Smbatyan If you use “ppc” then you will see facebook / ppc in
the All Traffic Sources report and the data will not be included in
the Advertising/Paid Search section of the reporting.
Reply to tacimala

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

14 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

I also have a separate profile (called raw data) which doesn’t have that filter. I
wanted to be able to compare the two and get an indication of how inaccurate my
figures were before introducing the filter.
When I look at the data from the past year, I find that the number of visits and
visitors is indeed lower in the filtered data set. But I’m confused – why does this filter
mean that the number of unique visitors is reduced by over 1200? Wouldn’t it just be
one (as I’m only filtering out one IP address?) And why are most of these filtered out
visitors in a different location from where my workplace is?
Similarly, why are any of the 3000 filtered out visits made by people outside of the
city where my workplace is?
Most strangely of all, when I compare the results for a custom report, looking at a
specific set of pages on the website, I find that there were 11 fewer unique visitors in
the filtered data than in the raw data, but when I specify the city, this difference is
19! How can this be?
I’m obviously either doing something wrong with the set up or interpreting the data
wrongly? Can you help me?
Reply to info21

Adrienne Whole New Mom 6/11/13 @ 2:36PM
Hi. I was wondering if you could help or direct me somewhere. My GA traffic used
to be greater than Statcounter traffic, but now it has dropped suddenly and I have no
idea why. My Statcounter is normal and my Adsense traffic (page views) appear very
close to the Statcounter #s, but the GA traffic is about 1/3 or more less. Any ideas
what could be causing this? I did have a problem with an installed plugin a few
weeks ago…it was WP Touch. It wasn’t tracking mobile viewers to either SC or GA,
but I removed it. GA seemed to be tracking fine, but now the numbers are really
low. Thanks in advance.
Reply to Adrienne Whole New Mom

Smbatyan 6/12/13 @ 3:22AM
@Adrienne Whole New Mom Did you checked all your pages for having GA
tracking code? May be you’ve done some change and removed tracking
code from some part of pages ?
Reply to Smbatyan

dschmeikal 7/05/13 @ 11:17AM
How do you track efficiently If your conversion process has your users going off site
(for example to paypal) and then back again to a final landing page.
Reply to dschmeikal

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

15 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Hope this helps!
Reply to crestodina

KenWarr 7/11/13 @ 12:13PM
We code our outgoing marketing emails using the code builder and the traffic is still
showing up as “direct/none”. Any advice or suggestions on how we can fix this? It
seems like sometimes it works properly and other times it does not.
Reply to KenWarr

AnthonyWoodcock 7/19/13 @ 10:28PM
Killer resource… Good to know.. I was always wondering why my direct traffic
seemed so high. Really did not make sense that it was so high. I mean, higher than
Google even. I don’t think I am that popular.
Reply to AnthonyWoodcock

jonsnow1 7/23/13 @ 7:45AM
Its sometimes important to record important business phone calls. I tend to use
Recordator, http://www.recordator.com to record phone calls to my pc .
Reply to jonsnow1

Steve Billings 8/06/13 @ 5:00PM
We have also seen that Google is lumping organic search traffic from mobile
browsers (e.g. safari for iphone) into direct traffic.
Reply to Steve Billings

dcivinelli 8/06/13 @ 5:11PM
Hey there – the sentence:
“If a visitor who is visually impaired uses a screen reader to access the site, Google
Analytics is blind to them.”
…is incorrect, as screen readers (such as JAWS) sit on top of the browser, so the GA
javascript will still activate. However, Google Analytics is unable to distinguish screen
readers *because* they sit on top of the browser, and do not have their own user
agent. There is a thread here that touches on this topic here: http://webaim.org
/discussion/mail_thread?thread=5259
Reply to dcivinelli

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

16 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Reply to chess

crestodina 8/08/13 @ 7:46AM
@chess This is true. If you use a URL shortener, GA can’t track the original source.
Not all bit.ly links are social traffic, so Google doesn’t assume that it was from a
social source…
Reply to crestodina

The Rust Belt Chronicles 4/09/15 @ 4:53PM
Will using the Google provided link shortener in Facebook or Twitter show in
Google Analytics? If not, what do I use in FB Insights or Twitter to give
accurate website hits?
Reply to The Rust Belt Chronicles

Smbatyan 8/08/13 @ 10:17AM
@chess
Actually you can do something to avoid this. Before shortening , add campaign
tracking parameters to your URL. It could be something like:
http://www.yoursite.com/pagename/?utm_source=facebook&
utm_medium=social&utm_campaign=campaignName
In this case GA will still track this traffic as social after shortening.
Reply to Smbatyan

chess 8/08/13 @ 12:47PM
@Smbatyan Thanks for your response. I am tagging all links with utm codes, but that
is not exactly the question. The question is whether I will see referrals from
facebook.com when Time Magazine shares a bit.ly link to my site on their Facebook
page.
Thanks so much for your help.
Reply to chess

chess 8/08/13 @ 12:48PM
@crestodina Wonderful, thanks. Actually, that totally sucks, but good to know.
Reply to chess

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

17 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Reply to levipage

wittywoman 8/14/13 @ 11:01AM
@Smbatyan @KenWarr Are you saying reporting of utm codes is unreliable in
Google Analytics?? How common is this?
Reply to wittywoman

Smbatyan 8/15/13 @ 6:32AM
@wittywoman If you are reffering to my answer, I was telling a little bit other thing.
utm codes are working fine, but some e-mail marketing systems as well as some
banner management systems automatically change “&” symbol by it’s encoded
version, i.e. “;&amp” and as a result utm codes are not working anymore. So to avoid
this, I recommend to shorten the url which contains utm codes.
Reply to Smbatyan

wittywoman 8/15/13 @ 12:45PM
@Smbatyan Thanks. Our e-mail codes are generated by MailChimp so I think we’re
safe.
Reply to wittywoman

j_librizzi 8/21/13 @ 2:34PM
Great post, thanks for the insights. But can you please clarify point #20? Are you
suggesting that, if the default profile is collecting all traffic totaling 100 visits, and
you create another profile that accounts for 20 visits, the default profile will be
reduced to 80? I’m certain that’s inaccurate.
Or are you saying that once the second profile is created, you can never add the
other 80 back in to it? That makes more sense, but I just want to make sure.
Reply to j_librizzi

SarahWelstead 8/22/13 @ 2:36AM
I use Google URL shortener when posting links on Twitter, and I’ve noticed that
sometimes there can be quite a disparity between the number of clickthroughs goo.gl
reports and the traffic stats Google Analytics reports. So goo.gl might report 143
clickthroughs on a given link in a given time period, but Google Analytics reports
only 32 visitors or 46 pageviews. This happens about once a week: goo.gl says
such-and-such link is getting a huge spike in traffic (sometimes from some random
source), but Analytics reports no spike in traffic in the same time period.
Do you know what’s going on? Is this a dumb question? (I’ve been using Analytics
for a while now but only at a beginner level.)

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

18 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Reply to amandag

levipage 8/27/13 @ 1:31PM
@amandag @levipage Yes, it’s not as feature rich as Google but great as a live tool
and has some things Google doesn’t. I use both for different reasons.
Reply to levipage

amandag 8/27/13 @ 4:43PM
@levipage Thanks!
Reply to amandag

KyleAkerman 9/22/13 @ 12:52PM
j_librizzi He is saying the second part of your statement.
The best practice is to keep a default unfiltered profile that contains all the raw data.
If you add another profile that accounts for 20 visits, it will only ever show 20 visits.
If you create the 20 visit filter without having a default unfiltered profile you will have
permanently altered your data set.
Reply to KyleAkerman

Ana 10/17/13 @ 4:23AM
Great Article!
I am having some troubles when i want to create a filter and i was wondering if you
could help me out with this. i would like to get the data coming from the medium
organic search coming as an organic. and also, in my account, it appears
configuration which i would like to filter it as Organic as well. could you please, lead
me on how to do it please? thank you!
Reply to Ana

Maryann Mueller 10/18/13 @ 11:17AM
Yes, is there any way to get some help on this….my analytics are way off, my twitter
posts don’t seem to be recognized and what twitter has done is infused my personal
with my business and I don’t want to lose my followers – when I put my personal
name it my business profile comes up…what a mess…dashboard shows 190,000 hits
in 16 weeks yet the hits show 20,000 way off. The amount of people coming in are
no where near the article hit count…how can I get this straightened out?
Reply to Maryann Mueller

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

19 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Reply to Perfect Homes

Zach 11/01/13 @ 4:09PM
Good stuff. I knew there was a less obvious reason for the amount of (direct)/(no
data) I was seeing.
Reply to Zach

Alan 11/02/13 @ 9:57AM
I had one of my sites “stolen” right down to to the GA and found out through the GA
traffic reports too! Thankfully this let me track to the site and “developer” whom I
promptly had take down the site.
Reply to Alan

Andy Crestodina 11/02/13 @ 10:48AM
I’ve seen this too, Alan! A plagiarist copies a site and takes the GA code
along with it. Unbelievable.
We had our site copied once too. You can read the entire story, including
our response, here…
http://www.orbitmedia.com/blog/web-content-plagiarism/
Reply to Andy Crestodina

Gus 11/04/13 @ 8:09AM
You actually missed all the reports that are supposed to be accurate, but they are
not, such as location. So in effect the post is a little misleading when it stops to
technicalities.
Reply to Gus

Andy Crestodina 11/04/13 @ 8:16AM
Yes, that’s true. I should add location to this post, since location data is
rarely accurate. But I don’t think this post is misleading because of that
omission.
Thank you for your input, Gus. I may add your suggestion to a future
version of this!
Reply to Andy Crestodina

Alexia 11/12/13 @ 11:36AM
Great article, I found it while searching for a solution to an issue we are having with
our site. We had a sponsored content article hosted on another site, with a link to

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

20 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Reply to Alexia

Andy Crestodina 11/12/13 @ 2:37PM
As long as the visits to the landing page aren’t zero, it’s probably tracking
properly. It’s possible that visitors are actually changing your address in
their address bar to access the home page. We’ve all done it!
If you use the Google URL builder to add campaign tracking code to those
links, you’ll be able to see how many visitors came from the sponsored
content link, to the landing page to the home page. Here’s an article that
explains how:
http://www.orbitmedia.com/blog/google-analytics-url-builder/
Hope this is helpful, Alexia!
Reply to Andy Crestodina

Jane 11/20/13 @ 10:29AM
Hi Andy, thanks for this article, did you try maybe to promote your website and get
visitors by using some profitable phrases/keywords on your website (title, headlines,
content). By using good niche keywords you can position your page in the first
results of Google and get many new visitors. There are even some tools which help
to find such keywords like Metrics11
Reply to Jane

Binford Boxe 11/21/13 @ 2:36PM
Very nice and useful article. You wrote “If Analytics sees campaign tracking code, it
ignores the referrer.”
Is there any way to have both – use campaign tracking code AND see referrer?
Thanks, Bin
Reply to Binford Boxe

Mark Focas 12/02/13 @ 4:19PM
Thanks for this great article. Do you have any idea of how many people might be
using plugins to block Google Analytics? In the light of the Snowden revelations and
ongoing NSA issues, clearly a lot more people are trying to block tracking of their
web activities. I have no idea what percentage of visitors this may be affecting.
I assume the most reliable way to detect this would be to add custom javascript in
the page to look for the presence of the Google Analytics object and if not present
make a server call to register that the GA code was not found. Do you know of any
stats, or way of determining how many users may have such plugins?
Reply to Mark Focas

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

21 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

But then again, if you’re worried about NSA wiretapping, you’ve got bigger
issues than Google Analytics…
Reply to Andy Crestodina

Mark Focas 12/02/13 @ 5:21PM
LOL, thanks Andy for your comment. I’m not so concerned about
this, but I’m thinking more of the people who are using these
plugins, and the numbers are growing.
If an end user uses such a plugin then pages can still work
successfully, they just aren’t tracked. If instead they block cookies
then all sorts of mayhem can occur with websites not behaving
correctly, so it is only the hard core who will do that.
If I do find any stats I’ll make sure to come back and post a
comment.
Reply to Mark Focas

Dan 12/11/13 @ 2:46PM
Just what I was looking for.
We have both GA and Statcounter(visit length set at 1 hour) installed with quite a
difference in Unique visitors.
I realise they track differently but have to give the stats to some advertisers.
Think its ok to add the 2 together and then take the average as accrding to some of
the forums GA under reports and SC over reports!
Page views for both are actually more consistant, just need to have the answers
ready.
Thanks Dan
Reply to Dan

Android 1/22/14 @ 3:53AM
Very nice and useful article.
Reply to Android

Nico Caramella (@NicoCaramella) 1/25/14 @ 4:49AM
Hey Andy! Great post! I still have one very basic question I couldn’t answer until
now.
Are links that are open in a new window/tab counted as referral traffic?
For example, let’s say I link to your homepage from my blog but I set it so that users
open it in a new tab. How does Google Analytics count the traffic source for that
news article? Is it direct because it is the first page navigated to in a new tab, or is it

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

22 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Andy 1/25/14 @ 10:47AM
Hello, Nico! Even if the link opens the site in a new window, Google will
know that the visitor was referred from another site. That information is still
passed through the browser.
So no worries! If you link to my home page and a visitor clicks, I’ll see that
you were the referrer in my Analytics…
Reply to Andy

Tiaan Van Zyl 1/27/14 @ 5:57AM
I have either a very good questions or a dumb questions:
We discovered that the tracking code to GA has been copied and placed underneath
each other. This equaled to a big spike in visits, which also showed a similar spike in
direct traffic. Our traffic doubled since that second tracking code got implemented.
Could the fact that there was two similar tracking codes, lead to GA picking the
second visit up as a direct?
We have taken out the second tracking code, so looks like the numbers are coming
down.
Reply to Tiaan Van Zyl

Sebastian 1/28/14 @ 1:49AM
Sorry but I must strongly disagree with Issue #5. This has in no way anything to do
with relative or full URL links. This is more related to a bad tracker configuration…
Reply to Sebastian

karen 2/21/14 @ 4:23PM
that is all very well and good, but what is the fix?
Reply to karen

Richard Chumbley 3/09/14 @ 7:28AM
This isn’t a field with which I’m very familiar with but aren’t a lot of Google Adwords
purchasers paying for visits they would have got anyway, and are unaware of this
fact? For example, if I search for Netflix, they will come up as a sponsored result at
the top of the page and, because we’re lazy, it’s that link that we will probably click,
not the organic result below. But if Netflix HADN’T been paying for Adwords, we still
would have visited the Netflix site through the organic link if we are actually looking
for ‘netflix’. Thus, particularly where a brandname is used as a search term and
would thus give a high ranking for a site in the organic listings, the advertiser ends
up believing that adwords is giving them all these wonderful results, when actually a
big chunk of those clicks are actually ‘stolen’ organic results. I haven’t been able to
find people discussing this rather misleading feature of adwords online. Am I wrong?

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

23 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

#1 for their brand name in organic search results, but they still buy the
pay-per-click ad for their name so they can “own” more of the search
results page.
Few companies other than Netflix would bid on the phrase “Netflix” so
competition is low for the phrase, so the ad probably only costs them $.05
per click. That’s the minimum. Also, Netflix only pays when people click on
the ad, and studies show that more people click on the organic listings than
the ads.
Combine those two factors and you can see how it’s not very expensive. But
think of all the people who see it! I bet a lot of people see that ad, so
there’s a big branding benefit.
If you’re doing any PPC at all, might as well bid on your own brand name.
Most experts recommend this. I’m not a PPC guy, but I can see how the
math would work.
Reply to Andy Crestodina (@crestodina)

Dominic Hurst 4/25/14 @ 4:27AM
I have a new one to add under “direct traffic”. For our main site we have one GA
account with several properties for each state of the site (test, beta, live). at the
moment we have released beta to the public via a link on the live site (and through
social, email etc). Traffic from live to beta is showing as direct rather than referral.
Reply to Dominic Hurst

Peggy 5/08/14 @ 2:04PM
Hi Andy – Great article. Question for you. We have a client who has a significant
amount of traffic coming to their site from Twitter on one specific date. They don’t
have a Twitter account. Is there any way we can find out where that traffic is coming
from on Twitter?
Reply to Peggy

Andy Crestodina (@crestodina) 5/08/14 @ 2:55PM
Sure, Peggy! Try this: for whichever page got all the Twitter traffic, put the
address into Topsy.com. That will show you the tweets to that page. Now
you can see who shared it and when. If the entire social storm was kicked
off by one or two influencers, it might be worth the time to connect with
them, thank them and offer to collaborate with them…
Hope this helps! It’s fun when that happens. One of my recent posts on this
site was shared 1000+ times on Facebook …and I don’t really use
Facebook.
Reply to Andy Crestodina (@crestodina)

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

24 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

icaine 6/13/14 @ 12:30PM
Hello guys, i have a quite big problem with GA. I have a site where i count clicks to
external pages. The problem is that GA at external pages (via referal) and by us (via
events) shows difference up to -40%/+70% (depends on POV) difference in visits
from our internal server logs. I am aware of crawlers that doesnt count to GA and
thus to count a click by us it must come from a visitor that previously moved his
mouse (via js/ajax touch) on the site. So i am asking you, dont you have any idea
why the difference is so high?
Reply to icaine

Tamar Ben-Moshe 6/17/14 @ 10:34AM
Wow! This blog was a great discovery for me, other than the Google analytics help.
Andy, I want to learn so much more from you.
Reply to Tamar Ben-Moshe

Lydia Anthony (@Lydia_Anthony) 6/17/14 @ 4:07PM
Hi Andy, this is a great list, but I am looking for reasons why Google would give
inaccurate landing page data for campaign traffic. My campaign data is littered with
all sorts of landing pages I never intentionally linked to, while the links I used the
campaign tracking tags on get little or no visits. Any thoughts?
Reply to Lydia Anthony (@Lydia_Anthony)

Andy Crestodina 6/19/14 @ 11:08AM
Hmm. I’m really not sure, Lydia! I’m looking at my reports and the reports
of my clients and I can’t find a single example of a campaign report
showing any landing pages except the landing pages the links were created
for.
If you’d like to connect with me on a social network, maybe we can find a
time to look at yours more closely. I’m curious about how your generating
the code and how Analytics is setup…
Reply to Andy Crestodina

sonalidheririya 7/02/14 @ 7:52AM
Hi Andy,
I have one query regarding the traffic stats on sub-domains. We
are using view filters to see data on sub-domains. But, it is
showing value of traffic more than in default profile.
For e.g. we have a website http://www.xyz.com/ and a
sub-domain abc.xyz.com. We have created a separate profile
using view filter to see the data on sub-domain (abc.xyz.com).

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

25 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

suggest some solution for this problem?
Priya
Reply to sonalidheririya

Susan 7/02/14 @ 11:50AM
This was good information. I’m still wondering why GA isn’t showing some visitors
when I can see through both Zopim and Mouseflow at the same time that someone
is going through the site. If both of those show it, why doesn’t GA show it in live
overview? (I’m assuming it’s not registering as a visit since it’s not showing live.)
Reply to Susan

Susan 7/02/14 @ 11:52AM
I forgot to mention that if I myself go on to the site, it shows live in Google
Analytics, as well as the other two.
Reply to Susan

cole mckussic 7/09/14 @ 8:23PM
Hi Andy,
Thank you so much for your post. I have a question about direct traffic:
Current customers visit my homepage in order to log-in to my portal… and (I’m
assuming) a ton of my direct traffic comes from these people – perhaps they have
the page bookmarked or they type the URL in, show up at the homepage, log-in, and
vanish.
My assumption is that this is seriously skewing my data. (My direct traffic numbers
are disproportionately huge.) I can ~sort of~ come to grips with this manually by
subtracting the direct traffic that only hits the homepage and then immediately
bounces. However, is there a better way to exclude this traffic from GA?
Thank you!
Reply to cole mckussic

Andy Crestodina (@crestodina) 7/10/14 @ 7:41AM
Hi, Cole. This is common for a lot of sites. One quick way to get a more
accurate look is to select “returning users” as a segment.
Also, it should be possible to put event tracking on the link, so you can
measure them without counting them all as bounces. Then it might be
possible to pull them out as a separate, more accurate, segment.
Let me know how it goes!

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

26 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Reply to David Geer (@geercom)

David 7/28/14 @ 10:22AM
Andy, have you heard of referral traffic coming from payment gateways? For
example I’ve got our payment gateway as Authipay (and PayPal) and redirects to our
order confirmation page. Code is correct as far as I can see, but within Analytics it
tracks this conversion as a referral conversion (coming from another domain) which it
doesnt? Have you heard of this before?
Reply to David

Melle 10/15/14 @ 4:53AM
H David, I can help you. Within Universal Analytics you need to exclude the
payment referral main urls (see: https://support.google.com
/analytics/answer/2795830?hl=en) You can find it under propery –
Trackinginfo. Hope this helps.
Reply to Melle

Amy 10/20/14 @ 7:19PM
You rock! Thank you so much for sharing this info. I was trying to figure out why I
kept getting “not provided” and this article answered questions I didn’t even know I
had. I definitely need to reassess how I use Google Analytics
Reply to Amy

Rosh Edwardd 12/02/14 @ 8:59AM
The blog was absolutely fantastic! Lot of great information which can be helpful in
some or the other way. Keep updating the blog, looking forward for more
contents…Great job, keep it up..
Reply to Rosh Edwardd

Daria 1/09/15 @ 4:29AM
Hi Andy, thank you for an article! Quick question, if I have auto-refresh on my sports
live blog, would it break referrer tracking of PageViews? I mean if a person came
from google, but then the page auto-refreshed, would the second page view still go
under organic or under direct? what are the ways around it? Thanks!
Reply to Daria

Andy Crestodina (@crestodina) 1/09/15 @ 7:59AM
Yes, an auto-refresh is definitely going to cause problems for your Analytics,
since it’s going to trigger the Javascript twice for each visit. It’s going to

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

27 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

your visitors…
Reply to Andy Crestodina (@crestodina)

siammandalay 1/18/15 @ 8:55PM
Hey Andy,
Great article. I have a constant wrestle with GA. The large proportion of my analytics
data is now not provided – although i know i can guesstimate via webmaster tools.
This among numerous other headaches, some of which you have mentioned.
Is Google Analytics still the best tool out there?
Reply to siammandalay

Andy Crestodina (@crestodina) 1/21/15 @ 12:00PM
Yes, I highly recommend GA. Let me put it this way: I can’t think of a
reason to NOT use Google Analytics!
Reply to Andy Crestodina (@crestodina)

john58975 5/21/15 @ 11:32PM
Its a nice article about GA. Well, It sum up all the things why GA is not good to use. I
was suffered from a same problem. GA collect a huge data where it is difficult to
know what are the unique visitors, bounce rate & so on. Now I’m working with
GoStats & it provide me accurate report, Each & every piece of information related to
website.
Reply to john58975

GenericPuzzles 6/30/15 @ 11:12PM
If nobody clicks on a link GA – provides the duration time as 0.00 always – is this
correct?
This creates problems for me when directing traffic to product pages from AdWords.
Reply to GenericPuzzles

Karel Koes Hiranjgarbh Missier Paragh 7/31/15 @ 3:52PM
Thank you for the information! Compliments, Karel Koes Hiranjgarbh Missier Paragh
Reply to Karel Koes Hiranjgarbh Missier Paragh

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

28 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

Andy Crestodina (@crestodina) 8/10/15 @ 6:31PM
I didn’t either until the designers chose that image. Who knew?
Reply to Andy Crestodina (@crestodina)

Dave Ruch 9/17/15 @ 1:23PM
@Andy, I’ve seen so many conflicting reports over the past few
months relative to best practices for dealing with referral or ghost
spam in GA, and it seems that the spammers are getting more
sophisticated all the time. Have you written on this recently, or is
there a method that you subscribe to in terms of minimizing the
appearance/effect of these numbers in the GA reports?
Thanks so much for all of your thoughtful writing – – it’s
immensely helpful.
Reply to Dave Ruch

Greg Moore 10/13/15 @ 1:35PM
Thank you!
I’m working on a site with 17 Google Analytics conversion Goals, some more
important than others.
Your tip about “ignoring the main conversion rate” is a great idea. Better to break out
the Goals and report on them individually.
Duh! Sounds obvious in retrospect, but I hadn’t thought about it clearly until reading
this. Thanks!
Reply to Greg Moore

Jo-Pierre 10/20/15 @ 6:05AM
Hi Andy … if I use a 3rd party mail system (SendGrid) and a user came to my site via
facebook, then has to register and I send a confirmation email via SendGrid (with
campaign url with source and medium specified eg. sendgrid / email) … how can I
make sure that this does not actually impact the facebook referral and I can still see
the ecommerce conversion as a facebook transaction. Would this campaign url
impact the original referral?
Reply to Jo-Pierre

Similar Posts

2015-11-14 12:31 PM

Inaccurate Google Analytics Traffic Sources

29 of 29

http://www.orbitmedia.com/blog/inaccurate-google-analytics-traffic-sources/

STAY CONNECTED

COMMITTED TO CHICAGO

NAVIGATE

Join over 10,500 people who receive bi-weekly web

Orbit is a proud member of the

Portfolio ›

Events ›

marketing tips.

Chicago community. We strive to

Web Design &
Development ›

Support ›

educate and collaborate with
like-minded businesses to make a
difference environmentally and socially.
Let's collaborate.
More About Our BCorp Status ›

About Us ›
Our Team ›

Hosting ›
Careers ›
Contact Us ›

Blog ›

Orbit Media Studios • 4043 N Ravenswood Ave, Suite 316, Chicago, IL 60613
• Map • Main (773) 348.4581 • Support (773) 353.8314
Privacy Policy / Sitemap / © 2015 Orbit Media Studios

2015-11-14 12:31 PM
```
