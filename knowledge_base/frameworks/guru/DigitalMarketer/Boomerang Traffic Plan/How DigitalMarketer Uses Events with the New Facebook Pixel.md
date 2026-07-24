# How DigitalMarketer Uses Events with the New Facebook Pixel.html

```markdown
DigitalMarketer Lab
Plus
My Profile
My Favorites
Support
kevin@fraserhighlandshoppe.ca
Log Out
Plus
My Profile
My Favorites
Support
kevin@fraserhighlandshoppe.ca
Log Out
Dashboard
Library
Execution Plans
Jumpstart Packs
Courses
Workshops
Office Hours
Saved
My Purchases
Toolbox
Deals
Community
Getting Started
Boomerang Traffic Plan
Previous Step
Next Step
1. Start Here
Note From The Author
How to Get the Most Out of Your Execution Plan
What is Retargeting?
What to Expect
2. Understanding the New Facebook Pixel
Ready for Primetime
New Facebook Pixel vs. Old Facebook Pixel
Getting Started with The New Facebook Pixel
How DigitalMarketer Uses Events with the New Facebook Pixel
Setting Up Custom Conversions
Optimization Objective: When To Use Events vs. Custom Conversions
Your Migration Process: Building Temporary Redundancy and Minimizing Damage
The New Facebook Pixel “Standard” Setup
The New Facebook Pixel “Easy” Setup
3. Facebook WCA—Getting Started
What is Facebook WCA?
Installing the Code
Using Content to Segment Your WCA's
Set Up WCA for Your Content
Running Ads to These Audiences
Give Us Your Feedback
How DigitalMarketer Uses Events with the New Facebook Pixel
But first, a warning: This is at the far end of the complexity spectrum. Don’t let the perceived amount of work in building something like this scare you off. This is how the most full-fledged and sophisticated Facebook tagging system would work, and also demonstrates how your tagging should be based on your funnel architecture.
As you probably know, DigitalMarketer has several Core Offers available on their site, and they all have Tripwires and Lead Magnets associated with each Core Offer.
This structure is built around the Customer Value Optimization system. If you’re not familiar with how this works, stop right here and go read it now.
So, let’s look at a diagram of one of DigitalMarketer’s funnels using their Paid Traffic Mastery certification.
As you can see, each Core Offer has a logical “downstream flow.” Core Offers have one or many associated Tripwires, each Tripwire has one or many associated Lead Magnets, and each Lead Magnet has one or many blog posts.
Traffic would “flow up” the diagram above.
Now, DigitalMarketer wants to be able to track conversions and create segmented audiences for all of these Core Offers and funnel stages all the way down to the blog visit level.
(RELATED: How to Write Blog Posts That Sell)
In order to accomplish this objective, they can use the new Facebook Pixel in conjunction with events to track conversions and build these detailed audiences. The standard events that you can use with the new Facebook pixel include things like:
ViewContent
Lead
AddToCart
InitiateCheckout
Purchase
Etc.
You can see a full listing of standard events here in the Facebook Tag docs.
As you can see, these events map nicely to the typical customer journey for a customer to purchase.
To illustrate, let’s take this excellent recent blog post from Tom Breeze as an example: Aducational Video + Remarketing: A Winning Ad Formula.
This post is focused on YouTube advertising and falls under the Core Offer of the Paid Traffic Mastery certification.
There’s an inline CTA in the post for a Tripwire called “The YouTube Retargeting System.”
I’m assuming that eventually DM will upsell the Tripwire purchasers to their Paid Traffic Mastery core offer.
(RELATED TRAINING: Become a Customer Acquisition Specialist)
Thus, our funnel looks something like this:
Clearly, we can’t just use plain-old events like View Content and Purchase to track the people who view this content and take action…
How would you differentiate the between conversions/audience from our other funnels in the Facebook ad backend?
How would you differentiate a Tripwire purchase from a Core Offer purchase?
We need to include some additional information with our Facebook events so that the Facebook ad platform can understand exactly what types of content-views and purchases are occurring.
This is where events really shine through, because events can also have tracking parameters associated with them that provide more detail about the event.
Typical parameters include content_name, content_category, value, etc.
You can see a full list of suggested standard parameters here from Facebook.
You’ll also be able to use custom parameters with your events, which we’ll show momentarily.
Parameters are inserted in your event code as the third parameter of the fbq function call, like this:
As you can see above, for the folks who purchase the Tripwire, we’re using the following parameters:
Content_name: To pass the name of the course/content.
Currency: Self explanatory.
Value: Purchase value.
Content_category: The overarching funnel that this Tripwire is part of.
Funnel_stage: Custom parameter that helps us differentiate Tripwire purchases from Core Offer purchases. This parameter name is completely arbitrary, it could be whatever makes sense to you, but ideally something you keep consistent across other similar events.
Note that this event must fire AFTER the base pixel has already loaded on the page.
You can do this by placing the event code just after the base tag in the page code, or by using a tool like Google Tag Manager, which enables you to control the sequencing of your tag fires more explicitly.
(RELATED: The Beginner’s Guide to Google Tag Managers: Parts, Setup, and Creation)
Continuing our example, let’s go ahead and plot out all of the Facebook events/tagging that we would use for this YouTube Advertising funnel.
Check out the video below to get the full walkthrough.
And check out the diagram below for the full summary…
Keep in mind that one of the goals of this type of event setup is to make our life easier when we’re creating our retargeting audiences.
Here’s an example audience we could create in Facebook Ad Manager (Found under Tools → Audiences → Create Audience → Custom Audience → Website Traffic) to retarget visitors who have bought the Tripwire but not bought the Core Offer.
If you watched the video above, you’ll have seen the steps to take to build out the audiences for the full funnel.
So, as you can see, events and parameters combine to provide a powerful way to target broad or precise audiences.
Remember that you DON'T HAVE to use parameters in your audience logic.
In our example above, we’re getting very granular (people who bought a specific Tripwire who have not bought a specific Core Offer), but we could just as easily do something like this to target ALL leads who haven’t bought anything:
We’ve now seen how to use parameters in our audience creation process… but what about for conversion tracking?
What if you want to optimize your campaign spend for a specific type of purchase?
If you’ve created campaigns with the objective Website Conversions before, you know that there’s no box to specify parameter values like we did in the WCA setup above:
This is where custom conversions come into the picture.
© 2019 DigitalMarketer.com
Privacy Policy
Support
Welcome to DigitalMarketer
×
Thank you for joining DM Lab! We'd like to officially welcome you with a quick tour PLUS a few insider tips for how to take full advantage of the platform and community.
Get Started
Join Lab Elite
×
Workshops and the Elite Commons Facebook Group are exclusive content for Lab Elite members. Click below to join Lab Elite!
Join Today!
Black Friday Bootcamp 2017
×
Black Friday Bootcamp is exclusive content. Click below to join!
Join Today!
Join DM Lab
×
Lab and the DM Engage Facebook Group are exclusive content for Lab members. Click below to join!
Join Today!
Join Lab to access our execution plans and more
Join the Premier Online Community for Digital Marketers and get full access to our execution plan library.
×
What Do You Actually Get?
36 business "checklists on steroids" and execution plans
Access to our private, member-only community
Weekly office hour sessions
Special "DM Deals" on our favorite software and services
$ 49/month
Try Lab FREE for 9 Days
Join Lab+ to access our courses and more
With Lab+, you can access all 11 of our acclaimed marketing certification & mastery courses PLUS everything Lab has to offer...
×
What Do You Actually Get?
36 business "checklists on steroids" and execution plans
Access to our 11 core marketing certifications and all future updates
Access to 3 elective certifications PLUS all future electives
Access to our private, members-only community
Badges and certifications for all completed trainings
Weekly office hour sessions
Up-to-date training with continuing education credits
Monthly "What’s Working Now" live webinars
Special "DM Deals" on our favorite software services
Complete access to our LMS to track your (or your team's) progress
$ 95/month
Your Current Plan
Join Elite to access our workshops and more
Includes monthly workshops, group coaching & accountability, access to our certifications, and everything else Lab has to offer. When you Join Lab ELITE, you're done.
×
What Do You Actually Get?
Live, 1-Day Virtual Workshops that kick off every month
Workshops are followed by "ELITE Office Hours" to get your most important questions answered & remove obstacles.
An ELITE Critique session to grade your project using our diagnostic tool and instructor to get your project ready to ship
Mastermind with fellow members and the DM team via the private, Members-Only Facebook Group
Rinse and repeat every month
FOCUSED training COMBINED with group coaching and masterminding (so stuff actually gets done)
Tap into high-level network of founder and executives all aligned to the exact same goals and on the exact same journey as you
The latest tips and tricks, along with the advice and feedback to know you’re executing the right way… the first time.
Under-the-hood visibility into what's going on in my other businesses
All the benefits that come with Lab (including its size) PLUS a smaller, tight-knit "community within a community"
$ 295/month
Try Elite FREE for 9 Days
Setup your billing details
×
Customer Information
First Name *
Last Name *
Email *
Phone *
Billing Information
Street Address *
Apt., ste., bldg. (optional)
City *
Country *
Select CountryAaland IslandsAfghanistanAlbaniaAlgeriaAmerican SamoaAndorraAngolaAnguillaAntarcticaAntigua and BarbudaArgentinaArmeniaArubaAustraliaAustriaAzerbaijanBahamasBahrainBangladeshBarbadosBelarusBelgiumBelizeBeninBermudaBhutanBoliviaBosnia and HerzegowinaBotswanaBouvet IslandBrazilBritish Indian Ocean TerritoryBrunei DarussalamBulgariaBurkina FasoBurundiCambodiaCameroonCanadaCape VerdeCayman IslandsCentral African RepublicChadChileChinaChristmas IslandCocos (Keeling) IslandsColombiaComorosCongoCook IslandsCosta RicaCroatiaCubaCyprusCzech RepublicDenmarkDjiboutiDominicaDominican RepublicEast TimorEcuadorEgyptEl SalvadorEquatorial GuineaEritreaEstoniaEthiopiaFalkland Islands (Malvinas)Faroe IslandsFijiFinlandFranceFrench GuianaFrench PolynesiaFrench Southern TerritoriesGabonGambiaGeorgiaGermanyGhanaGibraltarGreeceGreenlandGrenadaGuadeloupeGuamGuatemalaGuernseyGuineaGuinea-bissauGuyanaHaitiHeard and Mc Donald IslandsHondurasHong KongHungaryIcelandIndiaIndonesiaIran (Islamic Republic of)IraqIrelandIsle of ManIsraelItalyJamaicaJapanJerseyJordanKazakhstanKenyaKiribatiKorea, Democratic People's Republic ofKorea, Republic ofKuwaitKyrgyzstanLao People's Democratic RepublicLatviaLebanonLesothoLiberiaLibyan Arab JamahiriyaLiechtensteinLithuaniaLuxembourgMacauMacedonia, The Former Yugoslav Republic ofMadagascarMalawiMalaysiaMaldivesMaliMaltaMarshall IslandsMartiniqueMauritaniaMauritiusMayotteMexicoMoldova, Republic ofMonacoMongoliaMontenegroMontserratMoroccoMozambiqueMyanmarNamibiaNauruNepalNetherlandsNew CaledoniaNew ZealandNicaraguaNigerNigeriaNiueNorfolk IslandNorthern Mariana IslandsNorwayOmanPakistanPalauPanamaPapua New GuineaParaguayPeruPhilippinesPitcairnPolandPortugalPuerto RicoQatarReunionRomaniaRussian FederationRwandaSaint Kitts and NevisSaint LuciaSaint Vincent and the GrenadinesSamoaSan MarinoSao Tome and PrincipeSaudi ArabiaScotlandSenegalSerbiaSeychellesSierra LeoneSingaporeSlovakia (Slovak Republic)SloveniaSolomon IslandsSomaliaSouth AfricaSouth Georgia and the South Sandwich IslandsSpainSri LankaSt. HelenaSt. Pierre and MiquelonSudanSurinameSvalbard and Jan Mayen IslandsSwazilandSwedenSwitzerlandSyrian Arab RepublicTaiwanTajikistanTanzania, United Republic ofThailandTogoTokelauTongaTrinidad and TobagoTunisiaTurkeyTurkmenistanTurks and Caicos IslandsTuvaluUgandaUkraineUnited Arab EmiratesUnited KingdomUnited StatesUruguayUzbekistanVanuatuVatican City State (Holy See)VenezuelaViet NamVirgin Islands (British)Virgin Islands (U.S.)Wallis and Futuna IslandsWestern SaharaYemenYugoslaviaZaireZambiaZimbabwe
State *
Select State
Zip Code *
Payment Information
Card Number *
Expiry Month *
Select Month(01) Jan02 (Feb)03 (Mar)04 (Apr)05 (May)06 (Jun)07 (Jul)08 (Aug)09 (Sept)10 (Oct)11 (Nov)12 (Dec)
Expiry Year *
Select Year201920202021202220232024202520262027202820292030203120322033
CVV *
Submit Order
Upgrade now and become a Digital Marketing expert
Choose the plan that's best for you and your team.
×
Ideal for solo marketers looking for tools and community
1 User
36 marketing checklists and turnkey execution plans
Access to our 10,000+ private, member-only community
Special “DM Deals” on our favorite software and services (save up to 60% on the tools you’re already using)
$49/month
Try Lab FREE for 9 Days
$490/year
Try Lab FREE for 9 Days
Training and Certification Get Everything in Lab PLUS…
1 User
Includes everything in Lab
Access to our 11 master classes and certifications Plus all future master classes we add while you’re a member
Weekly “What’s Working Now Trainings” and Office Hours
Badges and certifications for all completed trainings
Up-to-date training with continuing education credits
Premium Support
$95/month
Your Current Plan
$950/year
Try Lab+ FREE for 9 Days
Coaching and Execution Get Everything in Lab and…
Up to 5 Users
Includes everything in Lab Basic & Lab+
Live 1-Day Virtual Workshops Every Month
Instructor Office Hours to help launch your monthly projects
Focused training COMBINED with group coaching and masterminding
A private, members-only community to hold you accountable each month
Access to our Growth Playbook
PLUS Two BONUS trainings
$295/month
Try Lab Elite FREE for 9 Days
$2995/year
Try Lab Elite FREE for 9 Days
Lab ELITE TEAM
Coaching and Execution for you AND your team
Live 1-Day Virtual Workshops Every
Month
Instructor Office Hours to help launch your monthly project
Focused training COMBINED with group coaching and mastermindin
A private, members-only community to hold you accountable each
month
Access to our Growth Playbook
PLUS Two BONUS trainings ($4,535 value)
$495/mo
Choose Plan
.
0 people are viewing this site
0
people
viewed this page
in the last
```
