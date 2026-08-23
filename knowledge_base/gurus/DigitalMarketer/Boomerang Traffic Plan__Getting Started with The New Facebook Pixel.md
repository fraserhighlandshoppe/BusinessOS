# Getting Started with The New Facebook Pixel.html

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
Getting Started with The New Facebook Pixel
Now that we understand the strengths of the new pixel, let’s get down to brass tacks and set up.
First, the term pixel is a bit of a misnomer in this situation. The reason it’s still referred to as a singular pixel is because there’s really only one pixel ID we will be using for everything, but, in practice, there are 2 components to the new pixel:
The base tag, which looks like this:
And events, which look like this:
If you’re not a programmer, or you just hate coding, don’t let the code above put you off. We can actually get by with editing very little from the 2 examples presented above.
Now, the base tag is the code snippet that you’ll want to place on every page of your website. This tag alone provides you the ability to do URL-based segmentation, and also serves as a “setup tag” that will allow us to use events.
It might seem obvious that we can use events to track conversions, but we can also use them to create segmentation rules in a Custom Audience build out.
Here’s an example where I want to create a segment of users who have become leads, but not purchased in the last 60 days:
One thing I want to make clear before we move on: Events are very powerful, but not mandatory, and in some situations they might be overkill.
We’ll talk through some different implementation scenarios momentarily, but if you have a very linear website, where you drive traffic through a single funnel, you could just apply the base pixel on each of your pages and then use URL rules to track conversions and segment your audience for retargeting.
Where events really come in handy is when you have a larger website, with multiple funnels and/or personas that you would like to optimize for.
So, let’s talk about a few scenarios that you’d be using events. For this example I can’t think of a better guinea pig than DigitalMarketer.
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
