# The New Facebook Pixel “Standard” Setup.html

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
The New Facebook Pixel “Standard” Setup
For the “Standard Setup,” we’re going to be taking full advantage of the new events.
Check out the video here for a complete walkthrough example of the Standard Setup: Using your funnel diagram to build out your sheet and generate your Facebook code, and then how to setup your custom audiences and custom conversions (if needed):
Go ahead and assign your events and parameters in columns G (“New Pixel Event Type”) and H (“New Pixel Parameters”) for each row in your Punch List.
You’ll want to put the parameter name (no spaces, use underscores if necessary), a colon, and then the value of the parameter in single quotes (again, no spaces and avoid special characters).
If you have multiple parameters, put a comma after the value, EXCEPT for the last entry in the list, like so:
content_name: ‘YouTubeOverlayGuide’,
funnel_stage: ‘leadmagnet’
(To go to a new line inside a Google Sheets cell, hit ALT + ENTER)
Once you’ve filled in your events and parameters, it’s time to grab our event code.
I’ve put together a few helper functions that will create the event code for you (output in column M) just be sure that you follow the pattern laid out in the example rows.
A disclaimer here: This Google Sheet does generate the event code for you, but it’s not iron-clad – you’ll want to review the code that’s generated and ensure there’s no syntax errors, etc.
When you copy and paste the code from the Google Sheet, you’ll notice that it wraps the script block in double-quotes. You’ll want to remove those double-quotes before pasting into your site code.
The generated event code in the far-right column will do 2 things:
Fire your new event.
Fire your old conversion pixel using the new Facebook Pixel syntax.
Here’s an example of what this looks like:
You would add this code to the appropriate page BELOW the base tag (or fire it after the base tag completes using Google Tag Manager).
Thus, we’ll have redundancy.
You can continue to use the old conversion pixel as an optimization objective (until Facebook removes them), and you can begin to migrate your conversion objectives over to the new events (or custom conversions based on those events).
A special note here is that you’ll want to remove your old conversion pixel code AND your old remarketing code from your pages when you install this, where appropriate.
Another thing to keep in mind about firing the old conversion pixels using the new syntax: if you have a purchase conversion pixel and you need to pass over value and currency, you can do so like this (covered in column F of the spreadsheet).
Pros of Standard Setup
Scalable, flexible and powerful: Enables several layers of granularity for conversion tracking and audience construction.
Easier reporting, conversion and audience setup.
Cons of Standard Setup
Takes a little more initial setup work.
You’re still placing your code on the page, which is not ideal (using GTM is superior) and requires some attention to ensure future content gets the appropriate event code added.
In what I call the “Optimal Setup,” you would follow the same preparation steps as the Standard Setup, but instead of placing our tagging directly on your website, you would use Google Tag Manager to house everything.
The time to begin planning your migration is now… late 2016 is quickly approaching, as that ominous Facebook Ad Manager message continues to remind us.
Click here to download the Facebook Pixel Migration Worksheet
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
